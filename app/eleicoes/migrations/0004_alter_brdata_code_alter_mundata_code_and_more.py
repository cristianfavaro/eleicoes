# Generated by Django 4.2.3 on 2023-11-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes', '0003_alter_statedata_muns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brdata',
            name='code',
            field=models.CharField(max_length=6, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='mundata',
            name='code',
            field=models.CharField(max_length=6, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='statedata',
            name='code',
            field=models.CharField(max_length=6, verbose_name='Código'),
        ),
    ]