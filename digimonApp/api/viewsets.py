from rest_framework.viewsets import ModelViewSet
from .serializers import DigimonSerializer
from ..models import DigimonModel

class DigimonViewSet(ModelViewSet):
    serializer_class = DigimonSerializer
    queryset = DigimonModel.objects.all()