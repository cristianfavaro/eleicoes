import re 
from funds.models import Fund

#Parâmetro de limpeza
def get_most_occur(add=[], exceptions=[]):
    from collections import Counter
    words = list(Fund.objects.values_list("denom_social", flat=True))
    words = "".join(words)
    split_it = words.split()
    Counters_found = Counter(split_it)
    most_occur = Counters_found.most_common(200)
    return [name for name, n in most_occur]

def parse_names():
    funds = Fund.objects.all()
    most_occur = get_most_occur()
    most_occur = [name for name in most_occur if len(name) > 5]
    exceptions = [
        "IBOVESPA", "VANGUARDA", "AMÉRICA", "VOTORANTIM",
        "SANTANDER"
    ]
    #adiciona aqui no futuro []
    filtered = [ fr"(^|\s)({name})(\b|\s)" for name in most_occur if name not in exceptions]
    filtered = filtered + [
        r"(^|\s)(DE)(\b|\s)", 
        r"(^|\s)(EM)(\b|\s)", 
        r"FUNDO", 
        r"(^|\s)(COTAS)(\b|\s)", #match em início ou fim de frase tbm
        r"(^|\s)(COTA)(\b|\s)", 
    ]
    regex = fr"|".join(filtered)

    counter = funds.count()

    for i, fund in enumerate(funds):
        print('\Parsing : ' + f"{i * 100 / counter}", end='\r')
        nome = re.sub(regex, "", fund.denom_social)
        nome = re.sub(' +', ' ', nome)

        if nome != fund.nome:
            fund.nome = nome
            fund.save()
