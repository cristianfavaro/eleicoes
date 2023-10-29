
from django.test import TestCase
from eleicoes.parsers.static_data import parse_data
from eleicoes.models import State, Municipality

class Test(TestCase):
    """test the authorized user tags api"""

    # def setUp(self):
        
        # get_data("/app/funds/tests/data/funds_info/cad_fi_copy.csv")
        # self.assertEqual(Fund.objects.all().count(), 23)

    def test_boolean_entid_invest_update(self):              
        parse_data("/app/eleicoes/test/files/arquivos-de-exemplo/ele2022/9579/config/mun-e009579-cm.json")
        
        self.assertEquals(2, State.objects.count())
        
    # def test_boolean_fundo_exclusivo_update(self):      
    #     fund = Fund.objects.get(cnpj_fundo="00.000.432/0001-00")
    #     fund.fundo_exclusivo = 0

    #     get_data("/app/funds/tests/data/funds_info/cad_fi_copy.csv")
        
    #     fund.refresh_from_db()
    #     self.assertEqual(fund.fundo_exclusivo, 1)

    # def test_atualiza_sit(self):       
    #     fund = Fund.objects.get(cnpj_fundo="00.000.684/0001-21")
    #     fund.sit = 1
    #     fund.save()
    #     get_data("/app/funds/tests/data/funds_info/cad_fi_copy.csv")
        
    #     fund.refresh_from_db()
    #     self.assertEqual(fund.sit, 7)

    # def test_atualiza_classe_anbima(self):       
    #     fund = Fund.objects.get(cnpj_fundo="00.000.684/0001-21")
    #     fund.classe_anbima = 1
    #     fund.save()
    #     get_data("/app/funds/tests/data/funds_info/cad_fi_copy.csv")
        
    #     fund.refresh_from_db()
    #     self.assertEqual(fund.sit, 7)

    # def test_choices_invalid(self):      
    #     #Criei uma classe que não existe, Fundo Multimercado22, no arquivo 
    #     fund = Fund.objects.get(cnpj_fundo="00.000.432/0001-00")
    #     self.assertEqual(fund.classe, 1)

    #     get_data("/app/funds/tests/data/funds_info/cad_fi_error_choice.csv")
    #     fund.refresh_from_db()
    #     self.assertEqual(fund.classe, 0)

