
from django.test import TestCase
from funds.models import Fund, Metric, Score, Star
from funds.parsers.metrics import parse_metrics
import pandas as pd

def create_funds(file, table):
    excel = pd.ExcelFile(file)
    df = excel.parse(table)
    df = df[["Name", "CNPJ of the Fund"]]
    values = df.values.tolist()

    funds = []
    for name, cnpj in values:
        funds.append(
            Fund(denom_social=name, cnpj_fundo=cnpj)
        )

    Fund.objects.bulk_create(funds)


class TestParseMetrics(TestCase):
    """test the authorized user tags api"""
    
    def setUp(self):
        ##Vou criar os fundos para o DI Rent e Sharpe
        file, table = "/app/funds/tests/data/metrics/Valor One Rank.xlsx", 'DI_Rent'
        create_funds(file, table)

    def test_quarter_DI_Rent(self):
        file, table = "/app/funds/tests/data/metrics/Valor One Rank.xlsx", 'DI_Rent'

        Metric.create_metrics(file, table, metric_type=2)
        
        funds = Fund.objects.all()
        self.assertEqual(len(funds), 149)
        self.assertEqual(len(Metric.objects.all()), 2384)

        file, table = "/app/funds/tests/data/metrics/Valor One Rank.xlsx", 'DI_Sharpe'

        Metric.create_metrics(file, table, metric_type=1)
        funds = Fund.objects.all()
        self.assertEqual(len(Metric.objects.all()), 4768)

    def test_valid_score(self):
        """Validando os dados de 2 fundos"""
        self.test_quarter_DI_Rent()
        Score.create_scores(16)
        #BB Private do fechamento em 2019-06-30 e 2023-03-31
        self.assertEqual(
            Score.objects.filter(fund__cnpj_fundo="15.037.554/0001-30")[0].value,
            70.0
        )
        self.assertEqual(
            Score.objects.filter(fund__cnpj_fundo="15.037.554/0001-30")[15].value,
            89.6510067114094
        )

        #Caixa TOP fechamento em 2019-06-30 e 2023-03-31
        self.assertEqual(
            Score.objects.filter(fund__cnpj_fundo="19.769.018/0001-80")[4].value,
            66.02836879432624
        )
        self.assertEqual(
            Score.objects.filter(fund__cnpj_fundo="19.769.018/0001-80")[15].value,
            92.59060402684564
        )

    def test_valid_stars(self):
        self.test_valid_score()
        Star.create_stars(16)

        #testando o do Itaú Privilège FIC FI RF Ref DI.
        self.assertEqual(
            Fund.objects.get(cnpj_fundo="26.199.519/0001-34").stars.last().value,
            5
        )
        #testando o do BRAM H Plus FIC FI RF LP.
        self.assertEqual(
            Fund.objects.get(cnpj_fundo="01.114.310/0001-08").stars.last().value,
            2
        )
    
    def test_full_process(self):
        file, retorno_table, sharpe_table = "/app/funds/tests/data/metrics/Valor One Rank.xlsx", 'DI_Rent', 'DI_Sharpe'
        parse_metrics(file, sharpe_table, retorno_table, 16)


        #TEST SCORE
        ##Caixa TOP fechamento em 2019-06-30 e 2023-03-31
        self.assertEqual(
            Score.objects.filter(fund__cnpj_fundo="19.769.018/0001-80")[4].value,
            66.02836879432624
        )

        #TEST STAR
        ###testando o do BRAM H Plus FIC FI RF LP.
        self.assertEqual(
            Fund.objects.get(cnpj_fundo="01.114.310/0001-08").stars.last().value,
            2
        )

    def test_nan(self):
        """Preciso avaliar se vai ser necessário remover o NAN e transformar em Zero. O decimal nao fica como None, entra como NAN."""
        pass
