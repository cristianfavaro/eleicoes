
from django.test import TestCase
from eleicoes.parsers.static_data import parse_mun
from eleicoes.models import Mun

class Test(TestCase):
    """test the authorized user tags api"""

    def setUp(self):       
        parse_mun("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/config/mun-e009579-cm.json")
               
    def test_municipalities(self):      
        acari = Mun.objects.get(cd=16012)
        self.assertEquals(acari.nm, "ACARI")
        self.assertFalse(acari.c)

