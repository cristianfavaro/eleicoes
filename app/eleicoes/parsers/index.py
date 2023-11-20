from .state import GovParser, MunParser
from .utils import load
from eleicoes.models import Index
import itertools

def get_gov_data(file, validators=[GovParser, MunParser]): 
    data = load(file)
    arq = [item for item in data["arq"] if not any( i in item["nm"] for i in [ ".sig", "br-", "mun-", "cert-", "ele-"] )]

    index, crated = Index.objects.get_or_create(
        cdabr=data["cdabr"]
    )

    if index.arq:
        updates = list(itertools.filterfalse(lambda x: x in index.arq, arq))
        #Processo aqui
    else:
        updates = arq
        for update in updates:
            Parser = next((Func for Func in validators if Func.validate(update["nm"])), False)
            if Parser:
                # parser = Parser(file=update["nm"])
                print(Parser, ' vendo aqui')
                
        #processa tudo 

    index.arq = arq
    index.save()    

    return updates
