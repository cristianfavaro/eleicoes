from django.test import TestCase
from eleicoes.parsers.candidates import parse_candidates
from eleicoes.parsers.state import PresParser
from eleicoes.models import BRData, Index
from rest_framework.test import APIClient
from eleicoes.parsers.index import get_gov_data


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




class TestGov(TestCase):
    """
        Testando aqui os dados sendo inseridos considerando o governo e eles sendo enviados para o State do BR
    """

    def setUp(self):
        self.updates = get_gov_data("/app/eleicoes/tests/files/arquivos-originais/544/config/df/df-e000544-i.json")
        
    def test_create(self):        
        self.assertTrue(Index.objects.filter(cdabr="DF").exists())        
        self.assertEquals(len(self.updates), 8)

        # print(self.updates, ' vendo')

    def test_no_update(self):     
        updates = get_gov_data("/app/eleicoes/tests/files/arquivos-originais/544/config/df/df-e000544-i.json")
        self.assertEquals(len(updates), 0)

    def test_update(self):     
        index = Index.objects.get(cdabr="DF")
        index.arq[0]["dh"] = "14/09/2022 16:22:03"
        index.save()

        updates = get_gov_data("/app/eleicoes/tests/files/arquivos-originais/544/config/df/df-e000544-i.json")
        self.assertEquals(len(updates), 1)
        
        index = Index.objects.get(cdabr="DF")
        index.arq[0]["nm"] = "df-c0001-e000544-002-f.json"
        index.arq[0]["dh"] = '26/09/2022 15:36:33'


    def test_create_mun(self):
        pass

    def test_create_gov(self):
        pass

    #     self.assertTrue(Index.objects.filter(cdabr="DF").exists())


    #     response = self.c.get('/api/eleicoes/544/br/')
    #     data = response.json()[0]
        
    #     self.assertEquals(data["values"][0]["nm"], 'LUIZ INÁCIO LULA DA SILVA')
    #     self.assertEquals(data["values"][0]["vap"], '57259504')
    #     # #brief
    #     self.assertEquals(data["brief"]["vb"], '1964779')
        
    # def test_update(self):              
    #     #mudando o cara
    #     brData = BRData.objects.get(cdabr="BR", ele=544)
    #     brData.brief["vb"] = 1000      
    #     brData.save()

    #     response = self.c.get('/api/eleicoes/544/br/')          
    #     data = response.json()[0]
        
    #     self.assertEquals(data["brief"]["vb"], 1000)
        
    #     # Rodando de novo para ver se ele muda.
    #     parser = PresParser("/app/eleicoes/tests/files/arquivos-originais/544/dados/br/br-c0001-e000544-v.json")
    #     parser.parse()

    #     response = self.c.get('/api/eleicoes/544/br/')          
    #     data = response.json()[0]

    #     self.assertEquals(data["brief"]["vb"], "1964779")

    # def test_mun(self):
    #     #MG
    #     response = self.c.get('/api/eleicoes/544/state/mg/')
    #     data = response.json()
    #     self.assertEquals(data["brief"]["vb"], "229425")
    #     self.assertEquals(data["values"][0]["vap"], "5802571")

    #     #RJ
    #     response = self.c.get('/api/eleicoes/544/state/rj/')
    #     data = response.json()
    #     self.assertEquals(data["brief"]["vb"], "159773")
    #     self.assertEquals(data["values"][0]["vap"], "3847143")

    #     #SP
    #     response = self.c.get('/api/eleicoes/544/state/sp/')
    #     data = response.json()
    #     self.assertEquals(data["brief"]["vb"], "571257")
    #     self.assertEquals(data["values"][0]["vap"], "10490032")

    #     # Vendo se criou o resumo no BR
    #     response = self.c.get('/api/eleicoes/544/br/')
    #     state = response.json()[0]["states"]
    #     self.assertEquals(len(state), 4)

