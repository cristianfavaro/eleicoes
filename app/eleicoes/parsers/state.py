
from eleicoes.models import Candidates, StateData, BRData
from .utils import load
from django.utils import timezone
import re

dbs = {
    1: BRData,
    3: StateData,
}

class Parser:
    def __init__(self, file):
        self.data = load(file)
        self.ele = self.data["ele"]
        self.tpabr = self.data["abr"][0]["tpabr"]
        self.cdabr = self.data["abr"][0]["cdabr"]
        self.carper = int(self.data["carper"])
        self.updated_at = timezone.datetime.strptime(
            f"{self.data['dg']} {self.data['hg']}", '%d/%m/%Y %H:%M:%S'
        )
        self.DB = dbs[self.carper]

        self.state = self.get_state()
        self.cands = self.get_candidates()
        
        self.brief = self.create_brief(self.data)
        self.values = self.create_values(self.data)

    def get_state(self):
        if self.tpabr == "MU":
            regex = r"([a-zA-Z]{2})[-|\d+]{0}"
            cdabr = str(re.findall(regex, self.data["nadf"], re.MULTILINE)[0]).upper()
        else: 
            cdabr = self.cdabr 
        return cdabr

    def get_candidates(self):
        
        #validação para quando for um dado municipal para eleicao estadual
    
        cands = Candidates.objects.filter(ele=self.ele, cdabr=self.cdabr, carper=self.carper).get()      
    
        return {
            int(item["n"]): {"nm": item["nm"], "par": item["par"]} for item in cands.values
        }
 
    def create_brief(self, data):
        return {
            "psa": data["abr"][0]["psa"],   
            "a": data["abr"][0]["a"],   
            "pa": data["abr"][0]["pa"],   
            "vb": data["abr"][0]["vb"],   
            "pvb": data["abr"][0]["pvb"],  
            "vn": data["abr"][0]["vn"],   
            "pvn": data["abr"][0]["pvn"],   
        }

    def simplify(self):
        return {**self.brief, "c": self.values}

    def create_values(self, data):

        return [
            { 
                **item, 
                "nm": self.cands[int(item["n"])]["nm"],
                "p": self.cands[int(item["n"])]["par"]
            } for item in data["abr"][0]["cand"]
        ]   

    def add_br_resume(self, type_data="states"):

        simplified = self.simplify()
        try:
            brData = BRData.objects.get(ele=self.ele)
        except BRData.DoesNotExist:
            brData = BRData.objects.create(
                ele=self.ele,
            )

        if self.carper == 3:     
            if type_data == "states":
                brData.states[self.cdabr] = simplified
            elif type_data == "muns":
                brData.muns[self.cdabr] = simplified
            
        brData.save()



class GeneralParser(Parser):
    def __init__(self, file):
        super().__init__(file)

    def parse(self):
        
        element = {
            "ele": self.ele,
            "cdabr": self.cdabr, 
            "brief": self.brief,
            "values": self.values,
        }        

        self.store_data(element)

        
    def store_data(self, element):

        object, created= self.DB.objects.get_or_create(
            ele=element.pop("ele"),
            cdabr=self.state, 
        )
        
        if self.tpabr in ["UF", "BR"]:          
            object.brief = element["brief"]
            object.values = element["values"]
            object.updated_at = self.updated_at
            object.save()                   

            self.add_br_resume()

        if self.tpabr == "MU":
            object.muns[self.cdabr] = {
                **self.create_brief(self.data), "c": self.create_values(self.data)
            }

            object.save()

            self.add_br_resume("muns")

