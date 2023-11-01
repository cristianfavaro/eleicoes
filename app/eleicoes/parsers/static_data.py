
from eleicoes.models import Mun
from .utils import load


def parse_mun(file):

    data = load(file)
    items = data["abr"]
    for item in items:

        state = item.get("cd")
        municipalities = [
            Mun(
                code=mun.get("cd"),
                code_i=mun.get("cdi"),
                name=mun.get("nm"),
                is_capital= True if mun.get("c") == "S" else False,
                zones=mun.get("z"),
                state=state,
            ) for mun in item.get("mu")
        ]

        Mun.objects.bulk_create(
            municipalities,
            update_conflicts=True,
            unique_fields=["code"],
            update_fields=[
                "code_i", "name", "is_capital", "zones"
            ],
            batch_size=500,
        )
