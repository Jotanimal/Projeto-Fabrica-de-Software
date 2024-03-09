from rest_framework.routers import DefaultRouter
from .viewsets import DigimonViewSet
from django.urls import path, include

router = DefaultRouter()

router.register('Digimon', DigimonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]