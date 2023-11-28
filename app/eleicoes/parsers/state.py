
from eleicoes.models import Candidates, StateData, BRData, MunData
from .utils import load
from django.utils import timezone
import re

def get_election(file):
    regex = r'e([\d]+)'
    return int(re.findall(regex, file, re.MULTILINE)[0])

def get_state(file=False):        
    regex = r"([a-zA-Z]{2})[-|\d+]{0}"
    return str(re.findall(regex, file, re.MULTILINE)[0]).upper()
 
def create_url(file, url):
    local = get_state(file)
    ele = get_election(file)

    return f"{url}/{ele}/dados/{local.lower()}/{file}"



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
    
        self.updated_at = timezone.datetime.strptime(
            f"{self.data['dg']} {self.data['hg']}", '%d/%m/%Y %H:%M:%S'
        )

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
            int(item["n"]): {"nmu": item["nmu"], "par": item["par"]} for item in cands.values
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
                "p": self.cands[int(item["n"])]["par"]
            } for item in data["abr"][0]["cand"]
        ]   


    def add_state_resume(self):
        simplified = self.simplify()
        
        obj, created = StateData.objects.get_or_create(
            ele=self.ele, cdabr=get_state(self.data["nadf"])
        )
        obj.muns[self.cdabr] = simplified            
        obj.save()

    def add_br_resume(self, type_data="states"):

        simplified = self.simplify()

        obj, created = BRData.objects.get_or_create(ele=self.ele, cdabr="BR")

        if type_data == "states":
            obj.states[self.cdabr] = simplified
        elif type_data == "muns":
            obj.muns[self.cdabr] = simplified
            
        obj.save()

    @staticmethod
    def validate(nm):
        return False
    


class PresParser(Parser):
    def __init__(self, file, url):
        super().__init__(file, url)

    def parse(self):
        
        element = {
            "ele": self.ele,
            "cdabr": self.cdabr, 
            "brief": self.brief,
            "values": self.values,
        }        

        self.store_data(element)

        
    def store_data(self, element):
        
        object, created = BRData.objects.get_or_create(
            ele=element.pop("ele"),
            cdabr="BR", 
        )

        object.brief = element["brief"]
        object.values = element["values"]
        object.updated_at = self.updated_at
        object.save()         

    @staticmethod
    def validate(nm):
        import re
        text = nm
        regex = r'[a-z]{2}\d+(.*).v.json'
        return True if re.findall(regex, text) else False
          


class GovParser(Parser):
    def __init__(self, file, url):
        super().__init__(file, url)

    def parse(self):
        
        element = {
            "ele": self.ele,
            "cdabr": self.cdabr, 
            "brief": self.brief,
            "values": self.values,
        }        

        self.store_data(element)

    
    def store_data(self, element):
        
        object, created= StateData.objects.get_or_create(
            ele=element.pop("ele"),
            cdabr=self.cdabr, 
        )

        object.brief = element["brief"]
        object.values = element["values"]
        object.updated_at = self.updated_at
        object.save()                   
        
        self.add_br_resume()

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
        
        object, created = MunData.objects.get_or_create(
            ele=element.pop("ele"),
            cdabr=self.cdabr,
        )

        object.brief = element["brief"]
        object.values = element["values"]
        object.updated_at = self.updated_at
        object.save()        

        self.add_state_resume()
        self.add_br_resume("muns")

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