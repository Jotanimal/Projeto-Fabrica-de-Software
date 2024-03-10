from rest_framework.routers import DefaultRouter
from .viewsets import DigimonList
from django.urls import path, include

router = DefaultRouter()

# Registrando os caminhos da API

router.register('Digimon', DigimonList)

urlpatterns = [
    path('digimon/', DigimonList.as_view()),
]