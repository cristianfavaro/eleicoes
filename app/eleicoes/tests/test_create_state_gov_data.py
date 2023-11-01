from django.test import TestCase
from eleicoes.parsers.candidates import parse_candidates
from eleicoes.parsers.static_data import parse_mun
from eleicoes.parsers.state import StateParser

class Test(TestCase):
    """test the authorized user tags api"""

    def setUp(self):
        ##primeiro eu preciso criar os candidatos para ele conseguir usar.
        parse_candidates("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df-c0003-e009579-081-f.json")
        # depois criar os municipios tbm. 
        parse_mun("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/config/mun-e009579-cm.json")

    def test_parse_candidates(self):              
        
        parser = StateParser(9579, "DF")
        parser.process("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df-c0003-e009579-v.json")
        
        # candidates = Candidates.objects.get(state="DF")
        # self.assertEquals(candidates.cands[0]["party"], "P12")
        # self.assertEquals(candidates.cands[0]["sqcand"], 70007787023)
