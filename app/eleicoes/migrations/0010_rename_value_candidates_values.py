# Generated by Django 4.2.3 on 2023-11-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes', '0009_rename_carg_candidates_carper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidates',
            old_name='value',
            new_name='values',
        ),
    ]
