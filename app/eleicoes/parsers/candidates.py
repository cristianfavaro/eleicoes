from .utils import load 
from eleicoes.models import Candidates


def get_newest_file(index):
    pass

def parse_candidates(file):
    data = load(file)

    ele = data["ele"]
    cdabr = data["cdabr"]
    carper = data["carg"]["cd"]

    cands = []
    for item in data["carg"]["agr"]:
        
        if len(item["par"][0]["cand"]) > 0:
            cand = item["par"][0]["cand"][0]
            cand["par"] = item["par"][0]["sg"].strip()
            cands.append(cand)

    Candidates.objects.update_or_create(
        cdabr=cdabr,
        carper=carper,
        defaults={
            "values": cands,
            "ele": ele,
        }
    )
