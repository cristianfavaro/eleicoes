from django.test import TestCase
from funds.parsers.daily_data import parse_data
from funds.models import Fund, DailyReport
from django.utils import timezone

cnpj_test_list = [
    '00.400.490/0001-13', '00.463.569/0001-93', '00.083.181/0001-67', '00.222.725/0001-24', 
    '00.185.259/0001-54', '00.524.617/0001-06', '00.398.561/0001-90', '00.102.322/0001-41', 
    '00.068.305/0001-35', '00.306.278/0001-91', '00.073.041/0001-08', '00.360.293/0001-18', 
    '00.322.699/0001-06', '00.222.816/0001-60', '00.071.477/0001-68', '00.280.302/0001-60', 
    '00.346.750/0001-10', '00.211.294/0001-09', '00.194.256/0001-87', '00.180.995/0001-10', 
    '00.539.553/0001-17', '00.017.024/0001-53', '00.575.922/0001-27', '00.598.452/0001-17', 
    '00.089.915/0001-15',
]

class TestParseDailyReport(TestCase):
    """test the authorized user tags api"""

    def setUp(self):

        for i, item in enumerate(cnpj_test_list):
            Fund.objects.create(
                nome = f'Fundo {i}',
                cnpj_fundo=item,
            )

        self.assertEqual(Fund.objects.count(), 25)

        response = parse_data("/app/funds/tests/data/daily_data/inf_diario_fi_202306_start.csv")
        self.assertEqual(len(response), 8)
        self.assertEqual(DailyReport.objects.count(), 8)

    def test_repeat_data(self):
        response = parse_data("/app/funds/tests/data/daily_data/inf_diario_fi_202306_start.csv")
        self.assertEqual(len(response), 8)
        self.assertEqual(DailyReport.objects.count(), 8)
    
    def test_update_vl_quota(self):
        fund = Fund.objects.get(cnpj_fundo="00.017.024/0001-53")
        daily = fund.daily_data.all()[0]
        self.assertEqual(str(daily.vl_quota), "32.401754800000")

        #testando novo valor
        response = parse_data("/app/funds/tests/data/daily_data/inf_diario_fi_202306_update.csv")        
        
        fund = Fund.objects.get(cnpj_fundo="00.017.024/0001-53")
        daily = fund.daily_data.all()[0]
        self.assertEqual(str(daily.vl_quota), "32.100000000000")
        self.assertEqual(DailyReport.objects.count(), 8)

    def test_decimal(self):
        fund = Fund.objects.get(cnpj_fundo="00.073.041/0001-08")
        daily = fund.daily_data.all()[0]
        self.assertEqual(str(daily.vl_quota), "34.874911400000")        

    def test_date(self):
        fund = Fund.objects.get(cnpj_fundo="00.073.041/0001-08")
        last = fund.daily_data.last()
        self.assertEqual(last.dt_comptc.month, 6)

    def test_add_items(self):
        response = parse_data("/app/funds/tests/data/daily_data/inf_diario_fi_202306_add.csv")
        self.assertEqual(DailyReport.objects.count(), 11)

    def test_filter_daily_data(self):
        response = parse_data("/app/funds/tests/data/daily_data/inf_diario_fi_202306_add.csv", start_date="2023-06-14")
        self.assertEqual(len(response), 3) 
        self.assertEqual(DailyReport.objects.count(), 10)

    def test_funds_same_date_and_fund(self):
        #ajustes para evitar erro com fundos com o mesmo id atualizando a mesma data ao mesmo tempo. Exemplo 202204
        # No caso específico, os dados são todos iguais. Então vamos dropar tudo que foi igual mesmo.
        # A unica diferenca está no tipo fundo, a priemira.
        # Os fundos mantém o mesmo CNPJ, mas com nomes diferentes e repetem a informaçãoe. Bem estrnaho. Exemploos no arquivo

        new_data = [
            '04.894.410/0001-84','04.881.687/0001-72', 
            '02.838.578/0001-47', '03.913.576/0001-38',
            '04.881.676/0001-92',
        ]

        for i, item in enumerate(new_data):
            Fund.objects.create(
                nome = f'Fundo {i}',
                cnpj_fundo=item,
            )
        parse_data("/app/funds/tests/data/daily_data/inf_diario_fi_202204_duplicated.csv")

    def test_start_date_string(self):
        parse_data(
            "/app/funds/tests/data/daily_data/inf_diario_fi_202306_add.csv",
            start_date="2023-06-15"
        )
        self.assertEqual(DailyReport.objects.count(), 9)

    def test_start_date_datetime(self):
        parse_data(
            "/app/funds/tests/data/daily_data/inf_diario_fi_202306_add.csv",
            start_date=timezone.datetime.strptime("2023-06-15", '%Y-%m-%d')
        )
        self.assertEqual(DailyReport.objects.count(), 9)
