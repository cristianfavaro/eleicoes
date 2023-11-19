
from eleicoes.models import Candidates, StateData, BRData, MunData
from .utils import load
from django.utils import timezone
import re

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

        # self.state = self.get_state()
        self.cands = self.get_candidates()
        
        self.brief = self.create_brief(self.data)
        self.values = self.create_values(self.data)

    def get_state(self):        
        regex = r"([a-zA-Z]{2})[-|\d+]{0}"
        return str(re.findall(regex, self.data["nadf"], re.MULTILINE)[0]).upper()

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
            cdabr = self.get_state() if self.tpabr == "MU" else self.cdabr

        cands = Candidates.objects.filter(ele=self.ele, cdabr=cdabr, carper=self.carper).get()      
    
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


    def add_state_resume(self):
        simplified = self.simplify()
        
        obj, created = StateData.objects.get_or_create(
            ele=self.ele, cdabr=self.get_state()
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


# class GeneralParser(Parser):
#     def __init__(self, file):
#         super().__init__(file)
        
#     def store_data(self, element):
        
#         object, created= self.DB.objects.get_or_create(
#             ele=element.pop("ele"),
#             cdabr=self.cdabr, 
#         )

#         object.brief = element["brief"]
#         object.values = element["values"]
#         object.updated_at = self.updated_at
#         object.save()                   

#         if self.tpabr == "UF":          
#             self.add_br_resume()

#         if self.tpabr == "MU":
#             object.muns[self.cdabr] = {
#                 **self.create_brief(self.data), "c": self.create_values(self.data)
#             }

#             object.save()

#             self.add_br_resume("muns")


class PresParser(Parser):
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
        
        object, created = BRData.objects.get_or_create(
            ele=element.pop("ele"),
            cdabr="BR", 
        )

        object.brief = element["brief"]
        object.values = element["values"]
        object.updated_at = self.updated_at
        object.save()                   


class GovParser(Parser):
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
        
        object, created= StateData.objects.get_or_create(
            ele=element.pop("ele"),
            cdabr=self.cdabr, 
        )

        object.brief = element["brief"]
        object.values = element["values"]
        object.updated_at = self.updated_at
        object.save()                   
        
        self.add_br_resume()


class MunParser(Parser):
    def __init__(self, file):
        super().__init__(file)
    
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

        
class MayorParser:
    pass