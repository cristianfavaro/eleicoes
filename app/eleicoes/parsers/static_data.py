import requests
import json
from eleicoes.models import State, Municipality
def load(file):
    pass

def parse_data(file, election=1):
    if "http" in file:
        data = requests.get(file).json()
    else:
        with open(file) as f:
            data = json.load(f)

    for item in data:
        state = State.objects.create(
            election_id=election,
            code=data.get("cd"),
            name=data.get("ds"),
        )
        municipalities = data.get("mu")

        for mun in municipalities:
            Municipality.objects.create(
                code=mun.get("cd"),
                code_i=mun.get("cdi"),
                name=mun.get("nm"),
                is_capital=mun.get("c"),
                zones=mun.get("z"),
                state=state,
            )
