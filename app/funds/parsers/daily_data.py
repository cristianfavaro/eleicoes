import pandas as pd
import numpy as np
from funds.models import Fund, DailyReport
from django.utils import timezone

    
def parse_data(file=False, date=False, start_date=False):
    """
        A função pega todos os dados do mês caso nenhum startdate seja passado
        o formato do startdate é yyyy-mm-dd
        do date é yyyymm
    """

    if file: 
        df = pd.read_csv(file, encoding="latin1", sep=";")    
    elif date:        
        
        url = f"https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{date}.zip" 
        df = pd.read_csv(url, compression='zip', encoding="latin1", sep=";")
    
    df.columns = [ column.lower() for column in df.columns ]
    ##limpando a base
    df = df\
        .replace(r'^\s*$', np.nan, regex=True)\
        .replace({np.nan: None})
    
    df["dt_comptc"] = pd.to_datetime(df["dt_comptc"], format="%Y-%m-%d")
    
    ###filtrando
    if start_date:
        if isinstance(start_date, str):
            start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d')
        df = df[df["dt_comptc"] >= start_date]

    ## Vamos trabalhar com o pandas para evitar bater no db o tempo todo
    funds_ids = pd\
        .DataFrame(Fund.objects.values("cnpj_fundo", "id", "sit"))\
        .rename(columns={"id": "fund_id"})

    df = pd.merge(df, funds_ids, on="cnpj_fundo")
    
    #ajuste. Explico nos testes.
    df = df.drop_duplicates(subset=df.columns[1:], keep="first")

    daily_reports = [
        DailyReport(**row) for i, row in  df.drop(["cnpj_fundo", "sit"], axis=1).iterrows()
    ]

    return DailyReport.objects.bulk_create(
        daily_reports,
        update_conflicts=True,
        unique_fields=["dt_comptc", "fund_id"],
        update_fields=[
            "captc_dia", "nr_cotst", "resg_dia",
            "tp_fundo", "vl_patrim_liq", "vl_quota",
            "vl_total"
        ],
        batch_size=500,
    )
