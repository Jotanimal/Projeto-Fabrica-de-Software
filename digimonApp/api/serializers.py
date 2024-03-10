from rest_framework.serializers import ModelSerializer
from ..models import DigimonModel

class DigimonSerializer(ModelSerializer):
    class Meta:
        model = DigimonModel
        fields = ['id', 'name', 'img', 'level']