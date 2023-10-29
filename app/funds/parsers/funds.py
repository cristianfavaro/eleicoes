import pandas as pd
from funds.models import Fund
import numpy as np
from funds.choices import SituacaoChoices, ClasseAnbimaChoices, ClasseChoices

def get_data(file="https://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv"):
    df = pd.read_csv(file, encoding="latin1", sep=";", low_memory=False)
    df.columns = [ column.lower() for column in df.columns ]

    # limpando a base
    # ordenei por sit para cancelado sempre ficar no fim. 
    # Pega o primeiro, com preferência o em funcionamento, que é 1

    df = df\
        .replace(r'^\s*$', np.nan, regex=True)\
        .sort_values("sit")\
        .drop_duplicates(subset="cnpj_fundo", keep='first')   

    #mudando o valor das colunas para bater com o formato na DB.   
    mapping = {'S': 1, 'N': 0} #neste caso o none é válido
    #Usando o map para evitar erro quando chegar uma chave nao conhecida
    
    df = df.assign(
        entid_invest = df["entid_invest"].map(mapping),
        fundo_cotas = df["fundo_cotas"].map(mapping),
        fundo_exclusivo = df["fundo_exclusivo"].map(mapping),
        invest_cempr_exter = df["invest_cempr_exter"].map(mapping),
        trib_lprazo = df["trib_lprazo"].map(mapping),
        sit = df["sit"].map(SituacaoChoices.mapping()).fillna(0).astype(int), #aqui eu não quero None, embora o db aceite
        classe_anbima = df["classe_anbima"].map(ClasseAnbimaChoices.mapping()).fillna(0).astype(int),
        classe = df["classe"].map(ClasseChoices.mapping()).fillna(0).astype(int),
    )   
     
    #transforma nan em None para o DB.
    df = df\
        .replace({np.nan: None})

    funds = [
        Fund(**row) for i, row in df.iterrows()
    ]

    return Fund.objects.bulk_create(
        funds,
        update_conflicts=True,
        unique_fields=["cnpj_fundo"],
        update_fields=[
            "classe", "classe_anbima", 
            "denom_social", "diretor", "dt_cancel", "dt_const", "dt_fim_exerc", 
            "dt_ini_ativ", "dt_ini_classe", "dt_ini_exerc", "dt_ini_sit", "dt_patrim_liq", 
            "dt_reg", "entid_invest", "fundo_cotas", "fundo_exclusivo", 
            "inf_taxa_adm", "inf_taxa_perfm", "invest_cempr_exter", 
            "publico_alvo", "rentab_fundo", "sit", "taxa_adm", "taxa_perfm", "tp_fundo",
            "trib_lprazo", "vl_patrim_liq",
        ],
        batch_size=500,
    )
