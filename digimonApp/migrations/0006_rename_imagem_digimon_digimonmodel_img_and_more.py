# Generated by Django 5.0.3 on 2024-03-10 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digimonApp', '0005_digimonmodel_imagem_digimon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='digimonmodel',
            old_name='imagem_digimon',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='digimonmodel',
            old_name='level_digimon',
            new_name='level',
        ),
    ]
