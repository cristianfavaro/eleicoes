# Generated by Django 4.2.3 on 2023-11-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes', '0011_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='arq',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Arquivos'),
        ),
    ]