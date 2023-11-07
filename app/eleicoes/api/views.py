from rest_framework import viewsets, status
from .serializers import StateDataSerializer, MunDataSerializer, BRDataSerializer
from eleicoes.models import StateData, MunData, BRData
from django.http import Http404

class StateDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StateDataSerializer
    queryset = StateData.objects.all()

    def get_object(self):
        #Pego o State tanto pelo número na base quanto sigla. 
        pk = self.kwargs['pk']
        if pk.isdigit():
            return super(StateDataViewSet, self).get_object()
        return self.get_queryset().get(code=pk.upper())
               
        
class MunDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MunDataSerializer
    queryset = MunData.objects.all()


class BRDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BRDataSerializer
    queryset = BRData.objects.all()
