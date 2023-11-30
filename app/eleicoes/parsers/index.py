from eleicoes.parsers.state import GovParser, MunParser
from eleicoes.parsers.utils import load
from eleicoes.models import Index
import itertools

def create_url_config(ele, local, url):
    return f"{url}/{ele}/config/{local.lower()}/{local.lower()}-e000544-i.json"


states = [
    "AL", 
    "AC",
    "AP", 
    "AM", 
    "BA", 
    "CE", 
    "DF", 
    "ES", 
    "GO", 
    "MA", 
    "MT", 
    "MS", 
    "MG", 
    "PA", 
    "PB", 
    "PR", 
    "PE", 
    "PI", 
    "RJ", 
    "RN", 
    "RS", 
    "RO", 
    "RR", 
    "SC", 
    "SP", 
    "SE", 
    "TO"
]

def get_gov_data(ele, local, url="https://resultados.tse.jus.br/oficial/ele2022", validators=[GovParser, MunParser]): 
    data = load(
        create_url_config(ele, local, url)
    )
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
                print('--Pegando esse: ', update["nm"])
                parser = Parser(update["nm"], url)
                parser.parse()
                
        #processa tudo 

    index.arq = arq
    index.save()    

    return updates

def main():
    ele = 544
    for state in states:
        print("=== ", state)
        d = get_gov_data(ele, state)
