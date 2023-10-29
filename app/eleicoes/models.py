from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Election(models.Model):
    number = models.IntegerField("Número")
    year = models.IntegerField("Ano")
    name = models.CharField("Nome", max_length=100)

class State(models.Model):
    election = models.ForeignKey('Eleição', on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=200)
    code = models.CharField("Código", max_length=3)

class Municipality(models.Model): 
    code = models.IntegerField("Código", validators=[MaxValueValidator(99999)])
    code_i = models.IntegerField("Código IBGE", validators=[MaxValueValidator(99999)])
    name = models.CharField("Nome Município", max_length=200)
    is_state = models.BooleanField("Capital")
    zones = models.JSONField("Zonas Eleitorais")
