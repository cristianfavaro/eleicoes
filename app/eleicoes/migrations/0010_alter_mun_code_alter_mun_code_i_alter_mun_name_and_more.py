# Generated by Django 4.2.3 on 2023-11-01 03:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes', '0009_alter_mun_code_alter_mun_code_i'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mun',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='mun',
            name='code_i',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Código IBGE'),
        ),
        migrations.AlterField(
            model_name='mun',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Nome Município'),
        ),
        migrations.AlterField(
            model_name='mun',
            name='state',
            field=models.CharField(max_length=5, verbose_name='Estado'),
        ),
    ]
