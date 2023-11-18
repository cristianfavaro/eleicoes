#ajustes rest framework
from rest_framework import routers
from django.urls import path, include
from .views import StateDataViewSet, MunDataViewSet, BRDataViewSet

router = routers.DefaultRouter()

# router.register('empresa', EmpresaViewSet, basename='empresa')
router.register('<int:id>/mun', MunDataViewSet, basename='mun')
router.register(r'(?P<ele_id>\d+)/state', StateDataViewSet, basename='state')
router.register(r'(?P<ele_id>\d+)/br', BRDataViewSet , basename='br')

urlpatterns = [
    path('eleicoes/', include(router.urls)),     
]
