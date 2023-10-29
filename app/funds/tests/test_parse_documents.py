from django.test import TestCase
from funds.parsers.documents import parse_data
from funds.models import Fund, Document

class TestParseDocuments(TestCase):
    """test the authorized user tags api"""

    def setUp(self):
        #Create Funds
        #Apaguei dois. 
        names = [
            # 'CPV DUPLICATA FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS',
            'PLETORA FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS',
            'METAL BANK ABM I - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS',
            'LEVO FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS',
            'AGHI FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS NÃO-PADRONIZADOS',
            'CREDIT BRASIL FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS MULTISSETORIAL MASTER',
            'HIKARI FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS',
            'JAFFA FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS NÃO PADRONIZADOS',
            'TERRAMAR FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS',
            # 'QUATRO.BI 12 - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS MULTISSETORIAL - NÃO PADRONIZADO'
        ]
        
        for i, name in enumerate(names):
            Fund.objects.create(denom_social=name, cnpj_fundo=f"000/{i}")


        self.assertEquals(Fund.objects.count(), 8) 

        created, error = parse_data(file="/app/funds/tests/data/document/documents_start.json")
        self.assertEqual(len(created), 1)
        self.assertEqual(len(error), 1)

    def test_run_again(self):
        created, error = parse_data(file="/app/funds/tests/data/document/documents_start.json")
        self.assertEqual(len(created), 0)
        self.assertEqual(len(error), 1)

    def test_add_new_documents(self):
        created, error = parse_data(file="/app/funds/tests/data/document/documents.json") 
        
        # self.assertTrue(Document.objects.filter(doc_id=500949).exists())
        self.assertEqual(len(created), 7)
        self.assertEqual(len(error), 2)

    def test_funds_same_denom_social(self):
        #vamos criar um fundo com o mesmo nome que ele. 
        Fund.objects.create(sit=7, denom_social='METAL BANK ABM I - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS', cnpj_fundo=f"100/0")     
        created, error = parse_data(file="/app/funds/tests/data/document/documents.json")

        self.assertEqual(len(created), 7)
        self.assertEqual(len(error), 2)


    def test_add_missing_funds(self):
        #vamos criar um fundo com o mesmo nome que ele. 

        names = [
            'CPV DUPLICATA FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS',
            'QUATRO.BI 12 - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS MULTISSETORIAL - NÃO PADRONIZADO'
        ]
        
        for i, name in enumerate(names):
            Fund.objects.create(denom_social=name, cnpj_fundo=f"2000/{i}")

        created, error = parse_data(file="/app/funds/tests/data/document/documents.json")

        self.assertEqual(len(created), 9)
        self.assertEqual(len(error), 0)
