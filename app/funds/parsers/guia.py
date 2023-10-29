import pandas as pd
from funds.models import Fund, Guia, ClasseValorChoices
import json
import numpy as np
from datetime import datetime

def get_quarter(file, table=False):
    excel = pd.ExcelFile(file)
    tables = excel.sheet_names

    if table: 
        df = excel.parse(table)
        parse_df(df, table)
    else:
        for table_name in tables:
            print(f"\n===Buscando table {table_name}====\n")
            df = excel.parse(table_name)
            parse_df(df, table_name)

#ajuste para converter int64 para python int
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


def parse_df(df, label):    
    
    for i in range(len(df)):
        item = dict(df.iloc[i])
        cnpj_fundo = item.pop("CNPJ of the Fund")
        date = datetime(2023, 3, 1).date()

        try: 
            ###Primeiro eu pego o fundo e vejo se ele mudou de categoria
            fund = Fund.objects.get(cnpj_fundo=cnpj_fundo)

            classe_valor = ClasseValorChoices.get_id_by_label(label)
            if fund.classe_valor != classe_valor:
                fund.classe_valor = classe_valor
                fund.save()
            
            Guia.objects.update_or_create(
                fund = fund,
                date = date,
                defaults = {
                    "content": json.dumps(item, cls=NpEncoder),
                },
            )
        except Fund.DoesNotExist:
            pass
