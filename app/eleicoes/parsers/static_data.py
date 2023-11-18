
from eleicoes.models import Mun
from .utils import load


def parse_mun(file):

    data = load(file)
    items = data["abr"]
    for item in items:

        uf = item.get("cd")
        municipalities = [
            Mun(
                cd=mun.get("cd"),
                cdi=mun.get("cdi"),
                nm=mun.get("nm"),
                c = True if mun.get("c") == "S" else False,
                z=mun.get("z"),
                uf=uf,
            ) for mun in item.get("mu")
        ]

        Mun.objects.bulk_create(
            municipalities,
            update_conflicts=True,
            unique_fields=["cd"],
            update_fields=[
                "cdi", "nm", "c", "z"
            ],
            batch_size=500,
        )
