from django.db import models

# Create your models here.

class DigimonModel(models.Model):

    nome_digimon = models.CharField(verbose_name = "Nome", max_length = 25)
    tipo_digimon = models.CharField(verbose_name = "Tipo", max_length = 10)
    atributo_digimon = models.CharField(verbose_name = "Atributo", max_length = 15)
    level_digimon = models.CharField(verbose_name = "Level", max_length = 15)