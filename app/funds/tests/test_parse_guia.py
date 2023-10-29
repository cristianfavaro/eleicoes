
from django.test import TestCase
from funds.parsers.guia import get_quarter
from funds.models import Fund, Guia
import pandas as pd
import json

def create_funds(file, table):
    excel = pd.ExcelFile(file)
    df = excel.parse(table)
    df = df[["Fund Legal Name", "CNPJ of the Fund"]]
    values = df.values.tolist()

    funds = []
    for name, cnpj in values:
        funds.append(
            Fund(denom_social=name, cnpj_fundo=cnpj)
        )

    Fund.objects.bulk_create(funds)


class TestParseGuia(TestCase):
    """test the authorized user tags api"""
    
    def test_quarter_RF_DI(self):
        file, table = "/app/funds/tests/data/guia_data/GuiaMar23_Atualizado.xlsx", 'RF DI'

        create_funds(file, table)
        get_quarter(file, table)
        
        funds = Fund.objects.all()
        self.assertEqual(len(funds), 149)
        self.assertEqual(len(Guia.objects.all()), 149)

    def test_label(self):
        """
            Validando se a label está correta depois que o código de definicao das metrics é rodado
        """
        file, table = "/app/funds/tests/data/guia_data/GuiaMar23_Atualizado.xlsx", 'RF DI'
        create_funds(file, table)
        fund = Fund.objects.get(cnpj_fundo="17.898.543/0001-70")
        self.assertEqual(fund.classe_valor, 0)
        get_quarter(file, table)
        fund.refresh_from_db()
        self.assertEqual(fund.classe_valor, 6)
        
    def test_quarter_JuroReal(self):
        """
            Separei para arrumar o erro que dava com o int64, convertendo para python int e assim transformar em json
        """
        file, table = "/app/funds/tests/data/guia_data/GuiaMar23_Atualizado.xlsx", 'JuroReal'
        
        create_funds(file, table)
        get_quarter(file, table)
        
        funds = Fund.objects.all()
        self.assertEqual(len(funds), 61)
        self.assertEqual(len(Guia.objects.all()), 61)

    def test_quarter_Multi(self):
        """ 
            Teste para arrumar o seguinte erro:
            ValueError: invalid literal for int() with base 10: '-'
            O erro é quando alguma das variáveis de Data estão vazias. Adicionei null como true na DB e tratei o next.
        """        
        file, table = "/app/funds/tests/data/guia_data/GuiaMar23_Atualizado.xlsx", 'Multi'
        
        create_funds(file, table)
        get_quarter(file, table)
        
        funds = Fund.objects.all()
        self.assertEqual(len(funds), 137)
        self.assertEqual(len(Guia.objects.all()), 137)

    def test_update_metric(self):
        """
            validando se ele atualiza a metrica pela nova
        """
        file, table = "/app/funds/tests/data/guia_data/GuiaMar23_Atualizado.xlsx", 'RF DI'
        create_funds(file, table)       
        get_quarter(file, table)
        fund = Fund.objects.get(cnpj_fundo="17.898.543/0001-70")
        content = json.loads(fund.guia.get().content)
        self.assertEqual(content["Fund Size - aggr from share classes (Daily) 2023-04-28 Base Currency"], 1695494759.0)
        
        file, table = "/app/funds/tests/data/guia_data/GuiaMar23_Updated.xlsx", 'RF DI'
        get_quarter(file, table)
        fund.refresh_from_db()
        content_updated = json.loads(fund.guia.get().content)
        self.assertEqual(content_updated["Fund Size - aggr from share classes (Daily) 2023-04-28 Base Currency"], 16954.0)
