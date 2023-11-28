from .state import GovParser, MunParser
from eleicoes.parsers.utils import load
from eleicoes.models import Index
import itertools

def create_url_config(ele, local, url="https://resultados.tse.jus.br/oficial/ele2022"):
    return f"{url}/{ele}/config/{local.lower()}/{local.lower()}-e000544-i.json"


def get_gov_data(ele, local, url, validators=[GovParser, MunParser]): 
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
                parser = Parser(update["nm"], url)
                parser.parse()
                
        #processa tudo 

    index.arq = arq
    index.save()    

    return updates
