# Generated by Django 5.0.3 on 2024-03-10 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digimonApp', '0002_remove_digimonmodel_atributo_digimon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digimonmodel',
            name='imagem_digimon',
        ),
        migrations.RemoveField(
            model_name='digimonmodel',
            name='level_digimon',
        ),
    ]
