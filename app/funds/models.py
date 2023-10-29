from django.db import models
from django.db.models import JSONField
from .choices import ClasseAnbimaChoices, SituacaoChoices, ClasseChoices, ClasseValorChoices, MetricTypeChoices, FrequencyChoices
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.

class Fund(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    classe_valor = models.IntegerField("Classe Valor", choices=ClasseValorChoices.choices, default=0)
    denom_social = models.CharField("Denominação Social", max_length=100, blank=True, null=True)
    cnpj_fundo = models.CharField("CNPJ do fundo", max_length=20, unique=True)
    #defaults
    admin = models.CharField("Nome do Administrador", max_length=100, blank=True, null=True)
    auditor = models.CharField("Nome do Auditor", max_length=100, blank=True, null=True)
    cd_cvm = models.IntegerField("Código CVM", blank=True, null=True)
    classe = models.IntegerField("Classe", choices=ClasseChoices.choices, null=True)
    classe_anbima = models.IntegerField("Classe Anbima", choices=ClasseAnbimaChoices.choices, null=True)
    cnpj_admin = models.CharField("CNPJ do Administrador", max_length=20, blank=True, null=True)
    cnpj_auditor = models.CharField("CNPJ do Auditor", max_length=20, blank=True, null=True)
    cnpj_controlador = models.CharField("CNPJ do Controlador", max_length=20, blank=True, null=True)
    cnpj_custodiante = models.CharField("CNPJ do Custodiante", max_length=20, blank=True, null=True)
    condom = models.CharField("Forma de condomínio", max_length=100, blank=True, null=True)
    controlador = models.CharField("Nome do Controlador", max_length=100, blank=True, null=True)
    cpf_cnpj_gestor = models.CharField("Informa o código de identificação do gestor pessoa física ou jurídica", max_length=20, blank=True, null=True)
    custodiante = models.CharField("Nome do Custodiante", max_length=100, blank=True, null=True)
    diretor = models.CharField("Nome do Diretor Responsável", max_length=100, blank=True, null=True)
    dt_cancel = models.CharField("Data de cancelamento", max_length=10, blank=True, null=True)
    dt_const = models.CharField("Data de constituição", max_length=10, blank=True, null=True)
    dt_fim_exerc = models.CharField("Data fim do exercício social", max_length=10, blank=True, null=True)
    dt_ini_ativ = models.CharField("Data de início de atividade", max_length=10, blank=True, null=True)
    dt_ini_classe = models.CharField("Data de início na classe", max_length=10, blank=True, null=True)
    dt_ini_exerc = models.CharField("Data início do exercício social", max_length=10, blank=True, null=True)
    dt_ini_sit = models.CharField("Data início da situação", max_length=10, blank=True, null=True)
    dt_patrim_liq = models.CharField("Data do patrimônio líquido", max_length=10, blank=True, null=True)
    dt_reg = models.CharField("Data de registro", max_length=10, blank=True, null=True)
    entid_invest = models.BooleanField("Indica se o fundo é entidade de investimento", null=True, default=None)
    fundo_cotas = models.BooleanField("Indica se é fundo de cotas", null=True, default=None)
    fundo_exclusivo = models.BooleanField("Indica se é fundo exclusivo", null=True, default=None)
    gestor = models.CharField("Nome do Gestor", max_length=100, blank=True, null=True)
    inf_taxa_adm = models.TextField("Informações Adicionais (Taxa de administração)", blank=True, null=True)
    inf_taxa_perfm = models.TextField("formações Adicionais (Taxa de performance)", blank=True, null=True)
    invest_cempr_exter = models.BooleanField("Indica se o fundo pode aplicar 100% dos recursos no exterior", null=True)
    pf_pj_gestor = models.CharField("Indica se o gestor é pessoa física ou jurídica", max_length=2, blank=True, null=True)
    publico_alvo = models.CharField("Público-alvo", max_length=20, blank=True, null=True)
    rentab_fundo = models.CharField("Forma de rentabilidade do fundo (indicador de desempenho)", max_length=100, blank=True, null=True)
    sit = models.IntegerField("Situação", choices=SituacaoChoices.choices, null=True)
    taxa_adm = models.FloatField("Taxa de administração", blank=True, null=True)
    taxa_perfm = models.FloatField("Taxa de performance", blank=True, null=True)
    tp_fundo = models.CharField("Tipo de fundo", max_length=30, blank=True, null=True)
    trib_lprazo = models.BooleanField("Indica se possui tributação de longo prazo", null=True, default=None)
    vl_patrim_liq = models.FloatField("Valor do patrimônio líquido", blank=True, null=True)

    def __str__(self):
        return str(self.denom_social)

class DailyReport(models.Model):
    captc_dia = models.FloatField("Captação do dia", blank=True, null=True)
    fund = models.ForeignKey('Fund', related_name="daily_data", on_delete=models.CASCADE)
    dt_comptc = models.DateField("Data de competência do documento")
    nr_cotst = models.IntegerField("Número de cotistas", blank=True, null=True)
    resg_dia = models.FloatField("Resgate no dia", blank=True, null=True)
    tp_fundo = models.CharField("Tipo de fundo", max_length=15, blank=True, null=True)
    vl_patrim_liq = models.FloatField("Valor do patrimônio líquido", blank=True, null=True)
    vl_quota = models.DecimalField("Valor da cota", blank=True, null=True, decimal_places=12, max_digits=27)
    vl_total = models.FloatField("Valor total da carteira", blank=True, null=True)

    def __str__(self):
        return f"{str(self.fund)} in {self.dt_comptc}"

    class Meta:
        unique_together = ('dt_comptc', 'fund')

class Guia(models.Model):
    fund = models.ForeignKey(Fund, related_name="guia", on_delete=models.CASCADE)
    content = JSONField()
    date = models.DateField()

    def __str__(self):
        return str(self.fund)
    
    class Meta:
        unique_together = ('date', 'fund') 

class Document(models.Model):
    fund = models.ForeignKey(Fund, related_name="documents", on_delete=models.CASCADE)
    doc_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    dataEntrega = models.DateTimeField("Data Entrega", blank=True, null=True)

    categoriaDocumento = models.CharField(max_length=100, blank=True, null=True)
    tipoDocumento = models.CharField(max_length=100, blank=True, null=True)
    especieDocumento = models.CharField(max_length=100, blank=True, null=True)
    dataReferencia = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    descricaoStatus = models.CharField(max_length=100, blank=True, null=True)
    analisado = models.CharField(max_length=100, blank=True, null=True)
    situacaoDocumento = models.CharField(max_length=100, blank=True, null=True)
    assuntos = models.CharField(max_length=100, blank=True, null=True)
    altaPrioridade = models.CharField(max_length=100, blank=True, null=True)
    formatoDataReferencia = models.CharField(max_length=100, blank=True, null=True)
    versao = models.CharField(max_length=100, blank=True, null=True)
    modalidade = models.CharField(max_length=100, blank=True, null=True)
    descricaoModalidade = models.CharField(max_length=100, blank=True, null=True)
    nomePregao = models.CharField(max_length=100, blank=True, null=True)
    informacoesAdicionais = models.CharField(max_length=100, blank=True, null=True)
    arquivoEstruturado = models.CharField(max_length=100, blank=True, null=True)
    formatoEstruturaDocumento = models.CharField(max_length=100, blank=True, null=True)
    nomeAdministrador = models.CharField(max_length=100, blank=True, null=True)
    cnpjAdministrador = models.CharField(max_length=100, blank=True, null=True)
    cnpjFundo = models.CharField(max_length=100, blank=True, null=True)
    idTemplate = models.CharField(max_length=100, blank=True, null=True)
    idSelectNotificacaoConvenio = models.CharField(max_length=100, blank=True, null=True)
    idSelectItemConvenio = models.CharField(max_length=100, blank=True, null=True)
    indicadorFundoAtivoB3 = models.CharField(max_length=100, blank=True, null=True)
    idEntidadeGerenciadora = models.CharField(max_length=100, blank=True, null=True)
    ofertaPublica = models.CharField(max_length=100, blank=True, null=True)
    numeroEmissao = models.CharField(max_length=100, blank=True, null=True)
    tipoPedido = models.CharField(max_length=100, blank=True, null=True)
    dda = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return str(self.fund)

class Score(models.Model):
    fund = models.ForeignKey(Fund, related_name="scores", on_delete=models.CASCADE)
    frequency = models.IntegerField(choices=FrequencyChoices.choices, default=2)
    value = models.FloatField(null=True)
    date = models.DateField("End Date") #should always be the end

    def __str__(self):
        return str(self.fund)

    class Meta:
        unique_together = ('date', 'fund', 'frequency')

    @staticmethod
    def create_scores(periods):
        import pandas as pd
        from funds.parsers.metrics import parse_df
        ## Criar o score com os dados de sharp e retorno mensal.
        available_dates = Metric.objects.order_by("-date").values("date").distinct()
        start_period = available_dates[periods - 1]["date"]
            
        values = Metric.objects.filter(date__gte=start_period).values("fund_id", 'fund__cnpj_fundo', "date", 'frequency', 'metric_type', 'value')
        df = pd.DataFrame(values) #as duas métricas estão aqui.
        
        #fazer as continhas com os dois. 
        retorno = parse_df(df, 2, 0.70)
        sharpe = parse_df(df, 1, 0.30)
        retorno[retorno.columns[2:]] = retorno[retorno.columns[2:]].add(sharpe[sharpe.columns[2:]], fill_value=0).fillna(0)

        # Criando o score
        data = pd.melt(retorno.reset_index(), id_vars=["fund_id", "fund__cnpj_fundo"], var_name="date", value_name="value")
        data["frequency"] = 2
        
        return Score.objects.bulk_create(
            [
                Score(**row) for i, row in  data.drop(["fund__cnpj_fundo"], axis=1).iterrows()
            ],
            update_conflicts=True,
            unique_fields=["fund_id", "frequency", "date"],
            update_fields=[
                "value",
            ],
            batch_size=500,
        )   

class Star(models.Model):
    fund = models.ForeignKey(Fund, related_name="stars", on_delete=models.CASCADE)
    frequency = models.IntegerField(choices=FrequencyChoices.choices, default=2)
    value = models.SmallIntegerField(null=True,  validators=[MaxValueValidator(5)])
    date = models.DateField("End Date") #should always be the end of reference

    def __str__(self):
        return str(self.fund)
    
    class Meta:
        unique_together = ('date', 'fund', 'frequency')

    @staticmethod
    def create_stars(periods):
        """
            Cria as estrelas com base nos últimos períodos determinados pelo usuário.
            No futuro vamos tratar para ela criar também outros tipos de frequencias.
        """
        import pandas as pd
        import numpy as np
        
        available_dates = Score.objects.order_by("-date").values("date").distinct()
        start_period = available_dates[periods - 1]["date"]
            
        values = Score.objects.filter(date__gte=start_period).values("fund_id", 'fund__cnpj_fundo', "date", 'frequency', 'value')
        df = pd.DataFrame(values) #as duas métricas estão aqui.
        
        pivot = df.pivot(columns=["date"], index=["fund_id", "fund__cnpj_fundo"], values="value")

        pivot["soma_periodos"] = pivot[pivot.columns].sum(axis=1)
        pivot["total_periodos"] = pivot[pivot.columns[:-1]].select_dtypes(np.number).gt(0).sum(axis=1) 
        pivot["score"] = pivot.apply(lambda x: x["soma_periodos"] / (x["total_periodos"] * 100), axis=1)
        pivot["value"] = pd.qcut(pivot['score'], 4, labels=[2, 3, 4, 5])
        pivot = pivot[["value"]].reset_index()

        #trazendo data - sempre a mais recente vai ser a referência
        pivot["date"] = available_dates[0]["date"]
        pivot["frequency"] = 2

        stars = [
            Star(**row) for i, row in  pivot.drop(["fund__cnpj_fundo"], axis=1).iterrows()
        ]

        return Star.objects.bulk_create(
            stars,
            update_conflicts=True,
            unique_fields=["fund_id", "frequency", "date"],
            update_fields=[
                "value",
            ],
            batch_size=500,
        )   
        
class Metric(models.Model):
    fund = models.ForeignKey(Fund, related_name="metrics", on_delete=models.CASCADE)
    date = models.DateField("End Date") 
    frequency = models.IntegerField(choices=FrequencyChoices.choices)
    metric_type = models.IntegerField(choices=MetricTypeChoices.choices)
    value = models.FloatField(null=True)

    class Meta:
        unique_together = ('date', 'fund', 'frequency', 'metric_type')

    def __str__(self):
        return str(self.fund)

    @staticmethod
    def create_metrics(file, table, metric_type, frequency=2):
        """
            Função que recebe os parametros para escolher qual tabela vai pegar do documento.
        """
        from funds.parsers.metrics import get_metrics

        df = get_metrics(file, table)
        df["frequency"] = frequency
        df["metric_type"] = metric_type
        
        return Metric.objects.bulk_create(
            [
                Metric(**row) for i, row in  df.drop(["cnpj_fundo", "Name"], axis=1).iterrows()
            ],
            update_conflicts=True,
            unique_fields=["fund_id", "frequency", "date", "metric_type"],
            update_fields=[
                "value",
            ],
            batch_size=500,
        )
