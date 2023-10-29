from rest_framework import viewsets
from funds.models import Fund, Guia, Document
from rest_framework.response import Response
from .serializers import FundSerializer, DocumentSerializer, FundMiniSerializer, GuiaSerializer
from .pagination import CustomPagination, CustomCursorPagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.db.models import Q
from app.tools.decorators import paginate


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_class = CustomCursorPagination
    ordering="-doc_id"
    permission_classes = [AllowAny]
    

class FundViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FundMiniSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        params = self.request.query_params.copy()
        q_objects = Q()
        
        classe_valor = params.get("classe_valor", False)
        if classe_valor == "__all__":
            params.pop("classe_valor")
            q_objects.add(~Q(**{"classe_valor": 0}), Q.AND)        

        for param in params.keys():              
            if param in ["cnpj_fundo", "classe", "classe_anbima", "classe_valor"]:
                q_objects.add(Q(**{param: params[param]}), Q.AND)        

        return Fund.objects.filter(q_objects)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FundSerializer(instance)
        return Response(serializer.data)

    @action(detail=True)
    def data(self, request, pk=None):
        fund = self.get_object()
        params = request.query_params.copy()
        field = params.get("field", False)
        if field in ["vl_patrim_liq", "nr_cotst"]: 
            return Response(fund.daily_data.order_by("dt_comptc").values("dt_comptc", field))
        return Response({})
    
    @action(detail=True)
    def metrics(self, request, pk=None):
        fund = self.get_object()

        try: metric = GuiaSerializer(fund.guia.get()).data
        except Guia.DoesNotExist: metric = {}

        return Response(metric)

    @paginate(serializer_class=DocumentSerializer, pagination_class=CustomCursorPagination)
    @action(detail=True)
    def documents(self, request, pk=None):
        fund = self.get_object()
        return fund.documents.all()
    
    @action(detail=True)
    def stars(self, request, pk=None):
        fund = self.get_object()
        return Response(fund.stars.order_by("-date").values("value"))

    @action(detail=True)
    def scores(self, request, pk=None):
        import decimal
        fund = self.get_object()
        return Response(fund.scores.exclude(value=decimal.Decimal('NaN')).order_by("date").values("value", "date"))


class GuiaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GuiaSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Guia.objects.all()
        classe_valor = self.request.query_params.get('classe_valor', False)
        if classe_valor:
            queryset = queryset.filter(fund__classe_valor=classe_valor)
        
        return queryset
