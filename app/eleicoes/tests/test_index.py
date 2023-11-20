from django.test import TestCase
from eleicoes.parsers.candidates import parse_candidates
from eleicoes.parsers.state import PresParser
from eleicoes.models import BRData, Index
from rest_framework.test import APIClient
from eleicoes.parsers.index import get_gov_data


["AL", 
"AC",
"AP", 
"AM", 
"BA", 
"CE", 
"DF", 
"ES", 
"GO", 
"MA", 
"MT", 
"MS", 
"MG", 
"PA", 
"PB", 
"PR", 
"PE", 
"PI", 
"RJ", 
"RN", 
"RS", 
"RO", 
"RR", 
"SC", 
"SP", 
"SE", 
"TO"]

class TestBR(TestCase):
    """
        Testando aqui os dados sendo inseridos considerando o governo e eles sendo enviados para o State do BR
    """
    pass

    # def setUp(self):
    #     self.updates = get_data("/app/eleicoes/tests/files/arquivos-originais/544/config/df/df-e000544-i.json")
        
    # def test_create_data(self):        
    #     self.assertTrue(Index.objects.filter(cdabr="DF").exists())
        
    #     self.assertEquals(len(self.updates), 8)

    # def test_no_update(self):     
    #     updates = get_data("/app/eleicoes/tests/files/arquivos-originais/544/config/df/df-e000544-i.json")
    #     self.assertEquals(len(updates), 0)

    # def test_update(self):     
    #     index = Index.objects.get(cdabr="DF")
    #     index.arq[0]["dh"] = "14/09/2022 16:22:03"
    #     index.save()

    #     updates = get_data("/app/eleicoes/tests/files/arquivos-originais/544/config/df/df-e000544-i.json")
    #     self.assertEquals(len(updates), 1)
        
        
    #     index = Index.objects.get(cdabr="DF")
    #     index.arq[0]["dh"] = '26/09/2022 15:36:33'


ele = 544
local = "df"
url = "/app/eleicoes/tests/files/arquivos-originais"


class TestGov(TestCase):
    """
        Testando aqui os dados sendo inseridos considerando o governo e eles sendo enviados para o State do BR
    """

    def setUp(self):
        parse_candidates("/app/eleicoes/tests/files/arquivos-originais/544/dados/br/br-c0001-e000544-001-f.json")
        self.updates = get_gov_data(ele, local, url)

        self.c = APIClient()  
        
    def test_create(self):        
        self.assertTrue(Index.objects.filter(cdabr="DF").exists())        
        self.assertEquals(len(self.updates), 8)

        # print(self.updates, ' vendo')

    def test_no_update(self):     
        updates = get_gov_data(ele, local, url)
        self.assertEquals(len(updates), 0)

    def test_update(self):     
        index = Index.objects.get(cdabr="DF")
        index.arq[0]["dh"] = "14/09/2022 16:22:03"
        index.save()

        updates = get_gov_data(ele, local, url)
        self.assertEquals(len(updates), 1)
        
        index = Index.objects.get(cdabr="DF")
        index.arq[0]["nm"] = "df-c0001-e000544-002-f.json"
        index.arq[0]["dh"] = '26/09/2022 15:36:33'


    def test_create_mun(self):
        response = self.c.get(f'/api/eleicoes/{ele}/mun/97012/')
        data = response.json()
        self.assertEquals(data["values"][0]['pvap'], '0,09')

    def test_create_gov(self):
        response = self.c.get(f'/api/eleicoes/{ele}/state/df/')
        data = response.json()
        self.assertEquals(data["values"][0]['pvap'], '36,85')


