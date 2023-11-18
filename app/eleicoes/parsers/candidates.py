from .utils import load 
from eleicoes.models import Candidates


def get_candidate(item):
    for i in range(len(item["par"])):
        try:
            cand = item["par"][i]["cand"][0]
            cand["par"] = item["par"][0]["sg"].strip()
            return cand
                 
        except IndexError:
            pass

def get_newest_file(index):
    pass

def parse_candidates(file):
    data = load(file)

    ele = data["ele"]
    cdabr = data["cdabr"]
    carper = data["carg"]["cd"]

    cands = []
    for item in data["carg"]["agr"]:
        cand = get_candidate(item)
        if cand: 
            cands.append(cand)

    Candidates.objects.update_or_create(
        cdabr=cdabr,
        carper=carper,
        defaults={
            "values": cands,
            "ele": ele,
        }
    )
