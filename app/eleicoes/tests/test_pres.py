from django.test import TestCase
from eleicoes.parsers.candidates import parse_candidates
from eleicoes.parsers.state import PresParser, GovParser
from eleicoes.models import BRData
from rest_framework.test import APIClient

url = "/app/eleicoes/tests/files/arquivos-originais/"

class Test(TestCase):
    """
        Testando aqui os dados sendo inseridos considerando o governo e eles sendo enviados para o State do BR
    """

    def setUp(self):
        ##primeiro eu preciso criar os candidatos para ele conseguir usar.
        
        parse_candidates("/app/eleicoes/tests/files/arquivos-originais/544/dados/br/br-c0001-e000544-001-f.json")

        #Parser - Dados Brasil
        parser = PresParser("br-c0001-e000544-v.json", url)
        parser.parse()

        ### Dados Presidente em estados
        GovParser("es-c0001-e000544-v.json", url).parse()
        GovParser("mg-c0001-e000544-v.json", url).parse()
        GovParser("rj-c0001-e000544-v.json", url).parse()
        GovParser("sp-c0001-e000544-v.json", url).parse()

        self.c = APIClient()        

    def test_create_data(self):        
        response = self.c.get('/api/eleicoes/544/br/')
        data = response.json()[0]
        
        self.assertEquals(data["values"][0]["nmu"], 'LULA')
        self.assertEquals(data["values"][0]["vap"], '57259504')
        # #brief
        self.assertEquals(data["brief"]["vb"], '1964779')
        
    def test_update(self):              
        #mudando o cara
        brData = BRData.objects.get(cdabr="BR", ele=544)
        brData.brief["vb"] = 1000      
        brData.save()

        response = self.c.get('/api/eleicoes/544/br/')          
        data = response.json()[0]
        
        self.assertEquals(data["brief"]["vb"], 1000)
        
        # Rodando de novo para ver se ele muda.
        parser = PresParser("br-c0001-e000544-v.json", url)
        parser.parse()

        response = self.c.get('/api/eleicoes/544/br/')          
        data = response.json()[0]

        self.assertEquals(data["brief"]["vb"], "1964779")

    def test_mun(self):
        #MG
        response = self.c.get('/api/eleicoes/544/state/mg/')
        data = response.json()
        self.assertEquals(data["brief"]["vb"], "229425")
        self.assertEquals(data["values"][0]["vap"], "5802571")

        #RJ
        response = self.c.get('/api/eleicoes/544/state/rj/')
        data = response.json()
        self.assertEquals(data["brief"]["vb"], "159773")
        self.assertEquals(data["values"][0]["vap"], "3847143")

        #SP
        response = self.c.get('/api/eleicoes/544/state/sp/')
        data = response.json()
        self.assertEquals(data["brief"]["vb"], "571257")
        self.assertEquals(data["values"][0]["vap"], "10490032")

        # Vendo se criou o resumo no BR
        response = self.c.get('/api/eleicoes/544/br/')
        state = response.json()[0]["states"]
        self.assertEquals(len(state), 4)

