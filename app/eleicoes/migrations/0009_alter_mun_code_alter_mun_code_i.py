# Generated by Django 4.2.3 on 2023-11-01 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes', '0008_remove_candidates_mun_remove_candidates_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mun',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='mun',
            name='code_i',
            field=models.IntegerField(verbose_name='Código IBGE'),
        ),
    ]
