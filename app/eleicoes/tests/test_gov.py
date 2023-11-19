from django.test import TestCase
from eleicoes.parsers.candidates import parse_candidates
from eleicoes.parsers.static_data import parse_mun
from eleicoes.parsers.state import GovParser, MunParser, MunData
from eleicoes.models import StateData
from rest_framework.test import APIClient

class Test(TestCase):
    """
        Testando aqui os dados sendo inseridos considerando o governo e eles sendo enviados para o State do BR
    """

    def setUp(self):
        ##primeiro eu preciso criar os candidatos para ele conseguir usar.
        parse_candidates("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df-c0003-e009579-081-f.json")
        parse_candidates("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/rn/rn-c0003-e009579-083-f.json")

        # depois criar os municipios tbm. 
        parse_mun("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/config/mun-e009579-cm.json")

        #Parser
        parser = GovParser("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df-c0003-e009579-v.json")
        parser.parse()

        self.c = APIClient()        

    def test_create_data(self):        
        response = self.c.get('/api/eleicoes/9579/state/df/')          
    
        values = response.json()["values"]

        self.assertEquals(values[0]["nm"], "CANDIDATO 15")
        self.assertEquals(values[0]["vap"], 192240)
        self.assertEquals(values[0]["pvap"], "13,14")

    def test_update(self):              
        #mudando o cara
        stateData = StateData.objects.get(cdabr="DF")
        stateData.values[0]["vap"] = 1000      
        stateData.save()

        response = self.c.get('/api/eleicoes/9579/state/df/')          
        values = response.json()["values"]

        self.assertEquals(values[0]["vap"], 1000)
        
        # Rodando de novo para ver se ele muda.
        parser = GovParser("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df-c0003-e009579-v.json")
        parser.parse()

        response = self.c.get('/api/eleicoes/9579/state/df/')          
        values = response.json()["values"]

        self.assertEquals(values[0]["vap"], 192240)

    def test_br_states_update(self):
        response = self.c.get('/api/eleicoes/9579/br/')
        data = response.json()[0]
        self.assertEquals(data["states"]["DF"]["c"][0]["vap"], 192240)

        ##Adicionando RN
        parser = GovParser("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/rn/rn-c0003-e009579-v.json")
        parser.parse()

        response = self.c.get('/api/eleicoes/9579/br/')
        data = response.json()[0]
        self.assertEquals(data["states"]["RN"]["c"][0]["vap"], 64247) #vendo o número de votos
    
        
### Testando agora os dados Municipais da Eleição estadual.
class TestMun(TestCase):
    """
        Testando aqui os dados sendo inseridos considerando os números dos municípios, que são enviados para o governo e também pra o BR.
    """

    def setUp(self):
        ##primeiro eu preciso criar os candidatos para ele conseguir usar.
        parse_candidates("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df-c0003-e009579-081-f.json")
        parse_candidates("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/rn/rn-c0003-e009579-083-f.json")

        # depois criar os municipios tbm. 
        parse_mun("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/config/mun-e009579-cm.json")

        #Parser
        parser = MunParser("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df97012-c0003-e009579-v.json")
        parser.parse()

        self.c = APIClient()                

    def test_created(self):

        response = self.c.get('/api/eleicoes/9579/mun/97012/')      
        
        values = response.json()["values"]

        self.assertEquals(values[0]["nm"], "CANDIDATO 14")
        self.assertEquals(values[0]["vap"], 180079)
        self.assertEquals(values[0]["pvap"], "12,31")

    def test_br_mun_update(self):
        response = self.c.get('/api/eleicoes/9579/br/')
        data = response.json()[0]
        self.assertEquals(data["muns"]["97012"]["c"][0]["vap"], 180079)
