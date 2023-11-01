
from eleicoes.models import Candidates, StateData
from .utils import load
from datetime import datetime

class Parser:
    def __init__(self, election, local, position):
        self.election = election
        self.local = local
        self.position = position

        self.cands = Candidates.objects.filter(election=election, local=local, position=3).get()


    def simplify(self):
        pass

    def parse(self, file):
        data = load(file)

        #### preciso por agora o resumo dos dados também. total, brancos, nulos etc.
        
        stateData = StateData.objects.update_or_create(
            election=data["ele"],
            code=self.local, 
            defaults={
                "election": data["ele"],
                "code": self.local,
                "updated_at": datetime.strptime(
                    f"{data['dg']} {data['hg']}", '%d/%m/%Y %H:%M:%S'
                ),
            }
        )
        

class StateParser(Parser):
    def __init__(self, election, local):
        super().__init__(election, local, 3)
        
    
    def process(self, file):
        # print(self.cands.value)
        
        self.parse(file)


    # def create_url(self):
        
        # if self.folder == "config":
            
        #     return
        
        # return f"https://resultados.tse.jus.br/oficial/ele2022/{self.election}/{self.folder}/{self.region}/{self.region}-c0001-e000544-r.json"

    

