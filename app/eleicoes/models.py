from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class Election(models.IntegerChoices):    
    ELE_544=544, "Eleição Federal - 2022 (1 turno)"
    DOC_546=546, "Eleição Estadual - 2022 (1 turno)"
    DOC_545=545, "Eleição Federal - 2022 (2 turno)"
    DOC_547=547, "Eleição Estadual - 2022 (2 turno)"

    #Testes
    ELE_9579=9579, "Teste 1"


class Carg(models.IntegerChoices):    
    CARG_1=1, "Presidente"
    CARG_3=3, "Governador"
    


class Mun(models.Model): 
    state = models.CharField("Estado", max_length=5)
    code = models.IntegerField("Código", primary_key=True, validators=[MaxValueValidator(99999)])
    code_i = models.IntegerField("Código IBGE", validators=[MaxValueValidator(99999)])
    name = models.CharField("Nome Município", max_length=300)
    is_capital = models.BooleanField("Capital")
    zones = models.JSONField("Zonas Eleitorais")    


class Candidates(models.Model): 
    #posso pensar em salvar eles separados e por aquivo.
    ele = models.IntegerField("Eleição", choices=Election.choices)
    ## coloco aqui os identificadores do arquivo do TSE. 
    cdabr = models.CharField("Codigo Local", max_length=200)
    carg = models.CharField("Cargo", max_length=100)

    value = models.JSONField("Candidatos")


class CommonInfo(models.Model):
    ele = models.IntegerField(choices=Election.choices)
    cdabr = models.CharField("Código", max_length=6)
 
    value = models.JSONField("Resultados", blank=True, null=True, default=dict)
    brief = models.JSONField("Resumo", blank=True, null=True, default=dict)
    updated_at = models.DateTimeField("Atualizado", auto_now=True)

    class Meta:
        abstract = True
        unique_together = ('ele', 'cdabr')


class BRData(CommonInfo): 
    states = models.JSONField("Estados", blank=True, null=True, default=dict)
    muns = models.JSONField("Municípios", blank=True, null=True, default=dict)


class StateData(CommonInfo):
    muns = models.JSONField("Municípios", blank=True, null=True, default=dict)


class MunData(CommonInfo):  
    pass