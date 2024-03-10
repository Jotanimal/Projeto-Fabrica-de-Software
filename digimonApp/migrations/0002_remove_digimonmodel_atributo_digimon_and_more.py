# Generated by Django 5.0.3 on 2024-03-10 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digimonApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digimonmodel',
            name='atributo_digimon',
        ),
        migrations.RemoveField(
            model_name='digimonmodel',
            name='tipo_digimon',
        ),
        migrations.AddField(
            model_name='digimonmodel',
            name='imagem_digimon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='digimonmodel',
            name='level_digimon',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Level'),
        ),
    ]
