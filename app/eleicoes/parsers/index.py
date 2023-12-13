from eleicoes.parsers.state import GovParser, MunParser
from eleicoes.parsers.utils import load
from eleicoes.models import Index
import itertools
from eleicoes.parsers.candidates import parse_candidates

def create_url_config(ele, local, url):
    return f"{url}/{ele}/config/{local.lower()}/{local.lower()}-e000{ele}-i.json"


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

def get_candidates(ele, local, url="https://resultados.tse.jus.br/oficial/ele2022"):
    import re
    print(f"--Iniciando {local}")
    data = load(
        create_url_config(ele, local, url)
    )
    regex = r"-c(\d*?)-"

    arq = [item for item in data["arq"] if any( i in item["nm"] for i in ["-f.json"])]
    
    codes = set(re.findall(regex, str(arq)))

    for code in codes: 
        print(f"Pegando código {code}")
        last_one = sorted([item["nm"] for item in arq if "c0003" in item["nm"]])[-1]
        link = f"{url}/{ele}/dados/{local.lower()}/{last_one}"
        parse_candidates(link)

    

def get_gov_data(ele, local, url="https://resultados.tse.jus.br/oficial/ele2022", validators=[GovParser, MunParser]): 
    data = load(
        create_url_config(ele, local, url)
    )
    arq = [item for item in data["arq"] if not any( i in item["nm"] for i in [ ".sig", "mun-", "cert-", "ele-", "c0005", "c0006", "c0007", "c0008"] )]

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
