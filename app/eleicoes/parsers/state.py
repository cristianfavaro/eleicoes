
from eleicoes.models import Candidates, StateData, BRData, MunData
from .utils import load
import re


def get_election(file):
    regex = r'-e([\d]+)'
    return int(re.findall(regex, file, re.MULTILINE)[0])

def get_state(file=False):        
    regex = r"([a-zA-Z]{2})[-|\d+]{0}"
    return str(re.findall(regex, file, re.MULTILINE)[0]).upper()
 
def create_url(file, url):
    local = get_state(file)
    ele = get_election(file)

    return f"{url}/{ele}/dados/{local.lower()}/{file}"


def local_store(ele, local, cdabr, data):
    import json
    import os

    filename = f'/app/frontend/data/eleicoes/{ele}/{local.lower()}/{str(cdabr).lower()}.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def local_load(ele, local, cdabr):
    import json
    import os

    filename = f'/app/frontend/data/eleicoes/{ele}/{local.lower()}/{str(cdabr).lower()}.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    try:
        with open(filename) as infile:
            return json.load(infile)
    except FileNotFoundError:
        return {}


def store_resume(file, simplified, cdabr, tpabr):
    local = get_state(file)
    ele = get_election(file)
    

    ##BR faz nada

    if tpabr == "BR":
        pass
    elif tpabr == "UF":
        data = local_load(ele, "br", "states")
        data[cdabr] = simplified
        local_store(ele, "br", "states", data)

    elif tpabr == "MU":
        data_br = local_load(ele, "br", "muns")
        data_br[cdabr] = simplified
        local_store(ele, "br", "muns", data_br)

        data_uf = local_load(ele, local, "muns")
        data_uf[cdabr] = simplified
        local_store(ele, local, "muns", data_uf)


def store_data(file, element):
    local = get_state(file)
    ele = get_election(file)

    local_store(ele, local, element["cdabr"], element)


class Parser:
    def __init__(self, file, url="https://resultados.tse.jus.br/oficial/ele2022/"):
        
        self.data = load(
            create_url(file, url)
        )
        self.url = url
        self.ele = self.data["ele"]
        self.tpabr = self.data["abr"][0]["tpabr"]
        self.cdabr = self.data["abr"][0]["cdabr"]
        self.carper = int(self.data["carper"])
    
        self.updated_at = f"{self.data['dg']} {self.data['hg']}"
                
        # timezone.datetime.strptime(
        #     f"{self.data['dg']} {self.data['hg']}", '%d/%m/%Y %H:%M:%S'
        # )

        # self.state = get_state(self.data["nadf"])
        self.cands = self.get_candidates()
        
        self.brief = self.create_brief(self.data)
        self.values = self.create_values(self.data)


    def parse(self):
        
        element = {
            "ele": self.ele,
            "cdabr": self.cdabr, 
            "brief": self.brief,
            "values": self.values,
            "updated_at": self.updated_at
        }        

        self.store_data(element)


    def get_candidates(self):
        """
            validação para quando for um dado municipal para eleicao estadual
            Por exemplo, dados para presidente no ES, devo pesquisar os canditos para presidente, não o cdabr do ES. 
        """
        if self.carper == 1:
            cdabr = "BR"
        elif self.carper == 3:
            cdabr = get_state(self.data["nadf"]) if self.tpabr == "MU" else self.cdabr

        cands = Candidates.objects.filter(ele=self.ele, cdabr=cdabr, carper=self.carper).get()      
    
        return {
            int(item["n"]): {"nmu": item["nmu"], "par": item["par"], "sqcand": item["sqcand"]} for item in cands.values
        }
 
    def create_brief(self, data):
        return {
            "psa": data["abr"][0]["psa"],   
            "a": data["abr"][0]["a"],   
            "pa": data["abr"][0]["pa"],   
            "vb": data["abr"][0]["vb"],   
            "pvb": data["abr"][0]["pvb"],  
            "vn": data["abr"][0]["vn"],   
            "ptvn": data["abr"][0]["ptvn"],   
        }

    def simplify(self):
        return {**self.brief, "c": self.values}

    def create_values(self, data):

        return [
            { 
                **item, 
                "nmu": self.cands[int(item["n"])]["nmu"],
                "p": self.cands[int(item["n"])]["par"],
                "sqcand": self.cands[int(item["n"])]["sqcand"]
            } for item in data["abr"][0]["cand"]
        ]   



    @staticmethod
    def validate(nm):
        return False
    


class PresParser(Parser):
    def __init__(self, file, url):
        super().__init__(file, url)

        
    def store_data(self, element):
        
        store_data(self.data["nadf"], element) #aqui eu nao quero rodar o dado de cada municipio
        # store_resume(self.data["nadf"], self.simplify(), self.cdabr, self.tpabr)

    @staticmethod
    def validate(nm):
        import re
        text = nm
        regex = r'br-(.*).v.json'
        return True if re.findall(regex, text) else False
          

class GovParser(Parser):
    def __init__(self, file, url):
        super().__init__(file, url)

    def store_data(self, element):        
        # store_data(self.data["nadf"], element)
        store_resume(self.data["nadf"], self.simplify(), self.cdabr, self.tpabr)

    @staticmethod
    def validate(nm):
        import re
        text = nm
        regex = r'[a-z]{2}-(.*).v.json'
        return True if re.findall(regex, text) else False


class MunParser(Parser):
    
    def __init__(self, file, url):
        super().__init__(file, url)
        
    def store_data(self, element):
        # store_data(self.data["nadf"], element) #aqui eu nao quero rodar o dado de cada municipio
        store_resume(self.data["nadf"], self.simplify(), self.cdabr, self.tpabr)
        
    @staticmethod
    def validate(nm):
        import re
        text = nm
        regex = r'[a-z]{2}\d+(.*).v.json'
        return True if re.findall(regex, text) else False

        
class MayorParser:
    pass


validators = [
    PresParser, 
    MunParser, 
    GovParser,
]

