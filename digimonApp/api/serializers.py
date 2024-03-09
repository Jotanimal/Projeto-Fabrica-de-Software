from rest_framework.serializers import ModelSerializer
from ..models import DigimonModel

class DigimonSerializer(ModelSerializer):
    class Meta:
        model = DigimonModel
        fields = ['id', 'nome_digimon', 'tipo_digimon', 'atributo_digimon', 'level_digimon']