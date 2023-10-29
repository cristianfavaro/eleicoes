import requests
import time
from funds.models import Document, Fund
from django.utils import timezone
from datetime import datetime
import json
from django.core.exceptions import MultipleObjectsReturned
from funds.api.serializers import DocumentSerializer
from django.db.models import Q


url = "https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosDados"


def get_documents(
        date=False, 
        paginate=False,
        d = 1,
        start_point = 0,
        step = 100,
        documents = [],
    ):
    #parametro inicial

    documents = documents
    
    d = d
    start_point = start_point
    step = step

    
    params = {
        "d": d,
        "s": start_point, #item inicial
        "l": step, #itens por página
        "o[0][dataEntrega]": "desc",    
    }
    if date:
        params["dataInicial"] = date
        params["dataFinal"] = date
    
    response = requests.get(url, params=params)
    response = response.json()
    documents = documents + response["data"]
    
    ## faz as coisas aqui.
    if paginate:
        recordsFiltered = response["recordsFiltered"]
        number_pages = (recordsFiltered // step) if paginate == "__all__" else paginate - 1 ##ele já começa com 1

        if d <= number_pages:
            start_point = d * step 
            d += 1
            time.sleep(1)
            return get_documents(date=date, 
                paginate=paginate, d=d, start_point=start_point, 
                step=step, documents=documents
            )

    return documents



def parse_data(
    date=False, 
    paginate=False,
    step = 10,
    file=False,
    notify=True, 
):

    created_items = []
    errors = []

    if file:
        with open(file, encoding='utf-8') as f:
            documents = json.loads(f.read())
    else:
        documents = get_documents(date=date, paginate=paginate, step=step)

    codes = set(
        Document.objects.all()
            .filter(created_at__gte=timezone.now() - timezone.timedelta(days=2))
            .values_list('doc_id', flat=True)
    )   

    for item in documents:
        doc_id = item.pop('id')
        if doc_id not in codes:

            descricaoFundo = item.pop("descricaoFundo", "")

            try:
                fund = Fund.objects.get(denom_social=descricaoFundo)
            
            except MultipleObjectsReturned:
                fund = Fund.objects.filter(Q(denom_social=descricaoFundo) & ~Q(sit=7)).get()
                
            #VC PODE TER DE TRATAR OUTROS ERROS TBM
            except Fund.DoesNotExist: #fundo nao existe
                errors.append(descricaoFundo)
                fund = False 

            finally: 
                if fund:                
                    item["fund"] = fund            
                    dataEntrega = item.pop("dataEntrega", "")

                    try: item["dataEntrega"] = datetime.strptime(dataEntrega, '%d/%m/%Y %H:%M')
                    except ValueError: pass

                    doc, created = Document.objects.get_or_create(
                        doc_id=doc_id,
                        defaults=item
                    )
                    
                    if created:
                        created_items.append(doc)


    return created_items, errors