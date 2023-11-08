
from eleicoes.models import Candidates, StateData, BRData
from .utils import load
from django.utils import timezone

dbs = {
    1: BRData,
    3: StateData,
}

class Parser:
    def __init__(self, file):
        self.data = load(file)
        self.election = self.data["ele"]
        self.tpabr = self.data["abr"][0]["tpabr"]
        self.code = self.data["abr"][0]["cdabr"]
        self.position = self.data["carper"]
        self.updated_at = timezone.datetime.strptime(
            f"{self.data['dg']} {self.data['hg']}", '%d/%m/%Y %H:%M:%S'
        )
        
        cands = Candidates.objects.filter(election=self.election, code=self.code, position=self.position).get()
        self.cands = {
            item["n"]: {"nm": item["nm"], "par": item["par"]} for item in cands.value
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

    def simplify(self, data):
        return {**data.brief, "c": data.value}

    def add_cand_names(self, data):
        return [
            { 
                **item, 
                "nm": self.cands[item["n"]]["nm"],
                "p": self.cands[item["n"]]["par"]
            } for item in data["abr"][0]["cand"]
        ]   

    def add_resume(self, stateData):

        simplified = self.simplify(stateData)

        try:
            brData = BRData.objects.get(election=self.election)
        except BRData.DoesNotExist:
            brData = BRData.objects.create(
                election=self.election,
            )

        if self.position == 3:     
            brData.states[self.code] = simplified
            brData.save()



class StateParser(Parser):
    def __init__(self, file):
        super().__init__(file)

    
    def parse(self):
        
        brief = self.create_brief(self.data)
        value = self.add_cand_names(self.data)
        
        stateData = StateData.objects.get_or_create(
            election=self.election,
            code=self.code, 
        )

        if self.tpabr == "UF":
            
            stateData.brief = brief
            stateData.value = value
            stateData.updated_at = self.updated_at
            stateData.save()                   

            self.add_resume(stateData)

        if self.tpabr == "MU":
            stateData.mun[self.code] = {
                **self.create_brief(self.data), "c": self.add_cand_names(self.data)
            }

            stateData.save()

