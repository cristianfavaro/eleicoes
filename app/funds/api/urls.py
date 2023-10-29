#ajustes rest framework
# from .views import PublicationViewSet, PanelView, NotificationViewSet, ProfileActivationView, ProfileViewSet, RegisterProfileView
from rest_framework import routers
from django.urls import path, include
from .views import FundViewSet, DocumentViewSet, GuiaViewSet

router = routers.DefaultRouter()
router.register('document', DocumentViewSet, basename='document')
router.register('guia', GuiaViewSet, basename='guia')
router.register('', FundViewSet, basename='fund')

urlpatterns = [
    path('', include(router.urls)),     
]
