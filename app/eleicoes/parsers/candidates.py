from .utils import load 
from eleicoes.models import Candidates


def get_newest_file(index):
    pass

def parse_candidates(file):
    data = load(file)

    election = data["ele"]
    local = data["cdabr"]
    position = data["carg"]["cd"]

    cands = []
    for item in data["carg"]["agr"]:
        cand = item["par"][0]["cand"][0]
        cand["party"] = item["par"][0]["sg"].strip()
        cands.append(cand)

    Candidates.objects.update_or_create(
        local=local,
        position=position,
        defaults={
            "value": cands,
            "election": election,
        }
    )
