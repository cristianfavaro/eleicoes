import pandas as pd
from funds.models import Fund, Score, Star, Metric
import re 

def parse_df(df, metric_type, peso):
    #ajuste para o sharpe
    data = df[df["metric_type"]==metric_type]

    pd.options.mode.chained_assignment = None #retirar o alerta
    if metric_type == 1:
        data["value"] = data["value"].apply(lambda x: x if x >= 0 else None)

    data = data.pivot(columns=["date"], index=["fund_id", "fund__cnpj_fundo"], values="value")
    data.columns = [str(column) for column in data.columns]
    
    for column in data.columns:
        data[column] = data[column].argsort().mask(data[column].isnull()).argsort().mask(data[column].isnull()) + 1
        #calculando ponto
        data[column] = data[column].apply(lambda x: (x/data[column].count() * 100) * peso)

    return data


def get_metrics(file, table):
    excel = pd.ExcelFile(file)
    df = excel.parse(table)

    df = pd.melt(df, id_vars=["Name", "CNPJ of the Fund"], var_name="date", value_name="value")

    df = df.rename(columns={
        "CNPJ of the Fund": "cnpj_fundo", 
    })
    #regex para mudar date. 
    regex = r'to\s(\d{4}-\d{2}-\d{2})'
    df["date"] = df.date.apply( lambda x: re.search(regex, x).group(1))
    df["date"] = pd.to_datetime(df["date"])

    funds_ids = pd\
            .DataFrame(Fund.objects.values("cnpj_fundo", "id"))\
            .rename(columns={"id": "fund_id"})

    df = pd.merge(df, funds_ids, on="cnpj_fundo")   
    return df

def parse_metrics(file, sharpe_table, retorno_table, periods, frequency=2):
    ###preciso ver como vou fazer para criar os dados do sharp e retorno ao mesmo tempo
    
    Metric.create_metrics(file, sharpe_table, 1, frequency)
    Metric.create_metrics(file, retorno_table, 2, frequency)

    Score.create_scores(periods)
    Star.create_stars(periods)
    
