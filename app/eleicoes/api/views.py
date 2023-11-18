from rest_framework import viewsets, status
from .serializers import StateDataSerializer, MunDataSerializer, BRDataSerializer
from eleicoes.models import StateData, MunData, BRData
from django.http import Http404

class BaseViewSet(viewsets.ReadOnlyModelViewSet):
    
    def get_queryset(self):
        return self.queryset.filter(ele=self.kwargs['ele_id'])


class StateDataViewSet(BaseViewSet):
    serializer_class = StateDataSerializer
    queryset = StateData.objects.all()

    def get_object(self):
        #Pego o State tanto pelo número na base quanto sigla. 
        pk = self.kwargs['pk']
        if pk.isdigit():
            return super(StateDataViewSet, self).get_object()
        return self.get_queryset().get(cdabr=pk.upper())
               
        
class MunDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MunDataSerializer
    queryset = MunData.objects.all()


class BRDataViewSet(BaseViewSet):
    serializer_class = BRDataSerializer
    queryset = BRData.objects.all()
