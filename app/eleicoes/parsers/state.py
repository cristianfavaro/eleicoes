
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
        self.code = self.data["abr"][0]["cdabr"]
        self.position = self.data["carper"]
        
        cands = Candidates.objects.filter(election=self.election, code=self.code, position=self.position).get()
        self.cands = {
            item["n"]: {"nm": item["nm"], "par": item["par"]} for item in cands.value
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
 
    def parse_state(self, data):
        brief = {
            "psa": data["abr"][0]["psa"],   
            "a": data["abr"][0]["a"],   
            "pa": data["abr"][0]["pa"],   
            "vb": data["abr"][0]["vb"],   
            "pvb": data["abr"][0]["pvb"],  
            "vn": data["abr"][0]["vn"],   
            "pvn": data["abr"][0]["pvn"],   
        }
        #### preciso por agora o resumo dos dados também. total, brancos, nulos etc.

        value = self.add_cand_names(data)

        stateData, created = StateData.objects.update_or_create(
            election=self.election,
            code=self.code, 
            defaults={
                "brief": brief,
                "value": value,
                "updated_at": timezone.datetime.strptime(
                    f"{data['dg']} {data['hg']}", '%d/%m/%Y %H:%M:%S'
                ),
            }
        )

        return stateData
    
    def parse(self):
        stateData = self.parse_state(self.data)

        self.add_resume(stateData)
