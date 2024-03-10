from django.db import models

# Create your models here.

class DigimonModel(models.Model):

    name = models.CharField(verbose_name = "Nome", max_length = 25)
    img = models.CharField(verbose_name = "", max_length = 100, blank = True, null = True)
    level = models.CharField(verbose_name = "Level", max_length = 15, blank = True, null = True)

    def __str__(self) -> str:
        return f'{self.name} {self.img} {self.level}'