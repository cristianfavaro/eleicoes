# Generated by Django 4.2.3 on 2023-11-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes', '0002_remove_candidates_local_candidates_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statedata',
            name='muns',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Municípios'),
        ),
    ]