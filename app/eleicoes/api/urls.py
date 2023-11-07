#ajustes rest framework
from rest_framework import routers
from django.urls import path, include
from .views import StateDataViewSet, MunDataViewSet, BRDataViewSet

router = routers.DefaultRouter()

# router.register('empresa', EmpresaViewSet, basename='empresa')
router.register('mun', MunDataViewSet, basename='mun')
router.register('state', StateDataViewSet, basename='state')
router.register('', BRDataViewSet , basename='br')

urlpatterns = [
    path('eleicoes/', include(router.urls)),     
]
