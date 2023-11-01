from django.test import TestCase
from eleicoes.parsers.candidates import parse_candidates
from eleicoes.models import Candidates

class Test(TestCase):
    """test the authorized user tags api"""

    def setUp(self):
        parse_candidates("/app/eleicoes/tests/files/arquivos-de-exemplo/ele2022/9579/dados/df/df-c0003-e009579-081-f.json")

    def test_parse_candidates(self):              
        candidates = Candidates.objects.get(local="DF")
        self.assertEquals(candidates.value[0]["party"], "P12")
        self.assertEquals(candidates.value[0]["sqcand"], 70007787023)
