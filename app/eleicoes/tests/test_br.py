from django.test import TestCase
from eleicoes.parsers.candidates import parse_candidates
from eleicoes.parsers.state import GeneralParser
from eleicoes.models import BRData
from rest_framework.test import APIClient

class Test(TestCase):
    """
        Testando aqui os dados sendo inseridos considerando o governo e eles sendo enviados para o State do BR
    """

    def setUp(self):
        ##primeiro eu preciso criar os candidatos para ele conseguir usar.
        
        parse_candidates("/app/eleicoes/tests/files/arquivos-originais/544/dados/br/br-c0001-e000544-001-f.json")

        #Parser
        parser = GeneralParser("/app/eleicoes/tests/files/arquivos-originais/544/dados/br/br-c0001-e000544-v.json")
        parser.parse()
    
        self.c = APIClient()        

    def test_create_data(self):        
        response = self.c.get('/api/eleicoes/544/br/')
        data = response.json()[0]
        
        self.assertEquals(data["values"][0]["nm"], 'LUIZ INÁCIO LULA DA SILVA')
        self.assertEquals(data["values"][0]["vap"], '57259504')
        # #brief
        self.assertEquals(data["brief"]["vb"], '1964779')
        
        
    def test_update(self):              
        #mudando o cara
        brData = BRData.objects.get(cdabr="BR")
        
        brData.brief["vb"] = 1000      
        brData.save()

        response = self.c.get('/api/eleicoes/544/br/')          
        data = response.json()[0]

        self.assertEquals(data["brief"]["vb"], 1000)
        
        # Rodando de novo para ver se ele muda.
        parser = GeneralParser("/app/eleicoes/tests/files/arquivos-originais/544/dados/br/br-c0001-e000544-v.json")
        parser.parse()

        response = self.c.get('/api/eleicoes/544/br/')          
        data = response.json()[0]

        self.assertEquals(data["brief"]["vb"], "1964779")

