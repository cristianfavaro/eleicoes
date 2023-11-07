from .utils import load 
from eleicoes.models import Candidates


def get_newest_file(index):
    pass

def parse_candidates(file):
    data = load(file)

    election = data["ele"]
    code = data["cdabr"]
    position = data["carg"]["cd"]

    cands = []
    for item in data["carg"]["agr"]:
        
        if len(item["par"][0]["cand"]) > 0:
            cand = item["par"][0]["cand"][0]
            cand["par"] = item["par"][0]["sg"].strip()
            cands.append(cand)

    Candidates.objects.update_or_create(
        code=code,
        position=position,
        defaults={
            "value": cands,
            "election": election,
        }
    )
