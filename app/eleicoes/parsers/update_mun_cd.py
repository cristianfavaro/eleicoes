import json 
with open("/app/frontend/data/maps/br-mun.json") as fp:
    geojson = json.load(fp)

with open("/app/eleicoes/tests/files/arquivos-originais/544/config/mun-e000544-cm.json") as fp:
    data = json.load(fp)

muns = {}

for item in data["abr"]:
    for mun in item["mu"]:
        muns[mun["cdi"]] = {"nm": mun["nm"], "uf": item["cd"], "cd": mun["cd"]}

for item in geojson["features"]:
    item["properties"] = {**item["properties"], **muns[item["properties"]["codarea"]]}

    
