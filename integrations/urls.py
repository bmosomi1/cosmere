from django.urls import path, include
from rest_framework.routers import DefaultRouter

from integrations import views

app_name = 'Integrations'

router = DefaultRouter()
router.register(r'miwama', views.MiwamaMpesaViewSet, basename='MiwamaMpesaViewSet')
router.register(r'greennote', views.GreenNoteMpesaViewSet, basename='GreenNoteMpesaViewSet')
router.register(r'greennote2', views.GreenNote2MpesaViewSet, basename='GreenNote2MpesaViewSet')
router.register(r'olemax', views.OlemaxMpesaViewSet, basename='OlemaxMpesaViewSet')
router.register(r'aquanova', views.AquaNovaViewSet, basename='AquaNovaViewSet')
router.register(r'parklands', views.ParkLandsMpesaViewSet, basename='ParkLandsMpesaViewSet')
router.register(r'parklands2', views.ParkLands2MpesaViewSet, basename='ParkLands2MpesaViewSet')
router.register(r'boresha', views.BoreshaMpesaViewSet, basename='BoreshaMpesaViewSet')
router.register(r'real/boutique', views.RealBoutiqueMpesaViewSet, basename='RealBoutiqueMpesaViewSet')
router.register(r'roberms', views.RobermsMpesaViewSet, basename='RobermsMpesaViewSet')
router.register(r'perezu', views.PerezuMpesaViewSet, basename='PerezuMpesaViewSet')
router.register(r'perezu2', views.PerezuMpesaViewSet2, basename='PerezuMpesaViewSet2')
router.register(r'nope', views.NopeMpesaViewSet, basename='NopeMpesaViewSet')
router.register(r'cleanshift', views.CleanShiftMpesaViewSet, basename='CleanShiftMpesaViewSet')

urlpatterns = [
    path('miwama/confirmation', views.miwama_confirmation),
    path('greennote/confirmation/', views.greennote_confirmation),
    path('', include(router.urls)),
]