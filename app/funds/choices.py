from django.db import models


class Choices(models.IntegerChoices):
    @classmethod
    def mapping(cls):
        return {name: i for i,name in cls.choices}

class MetricTypeChoices(models.IntegerChoices):
    UNKNOWN=0,	""
    CH_1=1,	"Sharpe 3 anos" #nos dois casos date é o último dia
    CH_2=2,	"Retorno 3 anos"


class FrequencyChoices(models.IntegerChoices):
    UNKNOWN=0,	""
    CH_1=1,	"Daily"
    CH_2=2,	"Monthly"
    CH_3=3,	"Bimonthly"
    CH_4=4,	"Quarterly"
    CH_5=5,	"Yearly"


class SituacaoChoices(Choices):
    UNKNOWN=0,	""
    CAT_1=1,	"EM FUNCIONAMENTO NORMAL"
    CAT_2=2,	"EM SITUAÇÃO ESPECIAL"
    CAT_3=3,	"LIQUIDAÇÃO"
    CAT_4=4,	"FASE PRÉ-OPERACIONAL"
    CAT_5=5,	"EM ANÁLISE"
    CAT_6=6,	"INCORPORAÇÃO"
    CAT_7=7,	"CANCELADA"

class ClasseAnbimaChoices(Choices):
    UNKNOWN=0,	""
    CH_1=1,	    "Renda Fixa Duração Livre Grau de Invest."
    CH_2=2,	    "Renda Fixa Duração Livre Crédito Livre"
    CH_3=3,	    "Ações Invest. no Exterior"
    CH_4=4,	    "Fechados de Ações"
    CH_5=5,	    "Ações Livre"
    CH_6=6,	    "Renda Fixa Duração Baixa Crédito Livre"
    CH_7=7,	    "Renda Fixa Duração Média Grau de Invest."
    CH_8=8,	    "Renda Fixa Duração Baixa Grau de Invest."
    CH_9=9,	    "Multimercados Livre"
    CH_10=10,	"Renda Fixa Dívida Externa"
    CH_11=11,	"Multimercados Macro"
    CH_12=12,	"Ações Índice Ativo"
    CH_13=13,	"Cambial"
    CH_14=14,	"Ações Valor/Crescimento"
    CH_15=15,	"Renda Fixa Duração Livre Soberano"
    CH_16=16,	"Renda Fixa Duração Baixa Soberano"
    CH_17=17,	"Renda Fixa Duração Alta Grau de Invest."
    CH_18=18,	"Multimercados Invest. no Exterior"
    CH_19=19,	"Multimercados Juros e Moedas"
    CH_20=20,	"Multimercados Balanceados"
    CH_21=21,	"Ações Small Caps"
    CH_22=22,	"Previdência RF Duração Livre Grau de Inv"
    CH_23=23,	"Ações Indexados"
    CH_24=24,	"Renda Fixa Duração Média Crédito Livre"
    CH_25=25,	"Previdência Balanceados de 30-49"
    CH_26=26,	"Previdência RF Duração Média Grau de Inv"
    CH_27=27,	"Ações Setoriais"
    CH_28=28,	"Fundos de Participações"
    CH_29=29,	"Ações Dividendos"
    CH_30=30,	"Multimercados Estrat. Específica"
    CH_31=31,	"Previdência RF Duração Livre Crédito Liv"
    CH_32=32,	"Renda Fixa Indexados"
    CH_33=33,	"Previdência Balanceados de 15-30"
    CH_34=34,	"Previdência RF Duração Baixa Grau de Inv"
    CH_35=35,	"Previdência Balanceados até 15"
    CH_36=36,	"Ações FMP - FGTS"
    CH_37=37,	"Previdência Multimercado Livre"
    CH_38=38,	"Previdência RF Duração Alta Grau de Inv."
    CH_39=39,	"Previdência RF Duração Livre Soberano"
    CH_40=40,	"Multimercados Dinâmico"
    CH_41=41,	"Previdência Ações Indexados"
    CH_42=42,	"Multimercados L/S - Direcional"
    CH_43=43,	"Fundos de Mono Ação"
    CH_44=44,	"Previdência RF Indexados"
    CH_45=45,	"Ações Sustentabilidade/Governança"
    CH_46=46,	"FII Hibrido Gestão Ativa"
    CH_47=47,	"Multimercados Trading"
    CH_48=48,	"Renda Fixa Duração Média Soberano"
    CH_49=49,	"Previdência Multimercados Juros e Moedas"
    CH_50=50,	"Previdência Balanceados Data Alvo"
    CH_51=51,	"Previdência Ações Ativo"
    CH_52=52,	"Multimercados L/S - Neutro"
    CH_53=53,	"Previdência RF Duração Baixa Soberano"
    CH_54=54,	"Multimercados Capital Protegido"
    CH_55=55,	"Renda Fixa Duração Alta Soberano"
    CH_56=56,	"Renda Fixa Duração Alta Crédito Livre"
    CH_57=57,	"Previdência RF Duração Alta Soberano"
    CH_58=58,	"FIDC Outros"
    CH_59=59,	"FIDC Fomento Mercantil"
    CH_60=60,	"Previdência RF Duração Baixa Crédito Liv"
    CH_61=61,	"FII Renda Gestão Ativa"
    CH_62=62,	"Previdência RF Data Alvo"
    CH_63=63,	"Previdência RF Duração Média Soberano"
    CH_64=64,	"Renda Fixa Invest. no Exterior"
    CH_65=65,	"Previdência RF Duração Média Crédito Liv"
    CH_66=66,	"Previdência Balanceados acima de 49"
    CH_67=67,	"Previdência RF Duração Alta Crédito Livr"


class ClasseChoices(Choices):
    UNKNOWN=0,	""
    CHO_1=1,	"Fundo Multimercado"
    CHO_2=2,	"Fundo de Ações"
    CHO_3=3,	"Fundo de Renda Fixa"
    CHO_4=4,	"Fundo Cambial"
    CHO_5=5,	"FIDC"
    CHO_6=6,	"FIDC-NP"
    CHO_7=7,	"FIC FIDC"
    CHO_8=8,	"FICFIDC-NP"
    CHO_9=9,	"FMP-FGTS"
    CHO_10=10,	"FIDCFIAGRO"
    CHO_11=11,	"FIP Multi"
    CHO_12=12,	"FIP"
    CHO_13=13,	"FIP CS"
    CHO_14=14,	"FIC FIP"
    CHO_15=15,	"FIP EE"
    CHO_16=16,	"FIP IE"
    CHO_17=17,	"FII"
    CHO_18=18,	"FII-FIAGRO"
    CHO_19=19,	"FIP-FIAGRO"
    CHO_20=20,	"FUNCINE"
    CHO_21=21,	"FIDC-PIPS"
    CHO_22=22,	"FMIEE"
    CHO_23=23,	"Fundo Referenciado"
    CHO_24=24,	"Fundo de Curto Prazo"
    CHO_25=25,	"Fundo da Dívida Externa"
    CHO_26=26,	"FIP PD&I"


class ClasseValorChoices(Choices):
    UNKNOWN=0,	""
    CAT_1=1,	"Crédito Privado Até 15 Dias"
    CAT_2=2,	"Alocação Ações"
    CAT_3=3,	"Ações no Exterior"
    CAT_4=4,	"Prefixado Renda Fixa Ativo"
    CAT_5=5,	"Juro Real"
    CAT_6=6,	"Renda Fixa DI"
    CAT_7=7,	"Debênture Incentivada"
    CAT_8=8,	"Ações"
    CAT_9=9,	"Crédito Privado Acima de 16 Dias"
    CAT_10=10,	"Crédito Privado até 15 Dias"
    CAT_11=11,	"Ações Índice"
    CAT_12=12,	"Long & Short"
    CAT_13=13,	"Investimento no Exterior"
    CAT_14=14,	"Multimercado Baixa Volatilidade"
    CAT_15=15,	"Long Biased"
    CAT_16=16,	"Multimercado"
    CAT_17=17,	"Alocação Multimercado"

    def get_id_by_label(name):
        labels = {
            'RF DI': 6,
            'RF Ativo Prefixado': 4,
            'JuroReal': 5,
            'CP 15': 1,
            'CP 16': 9,
            'DebInc': 7,
            'Multi Baixa Vol': 13,
            'Multi': 15,
            'LongShort': 11,
            'LongBiased': 14,
            'AçõesIndice': 10,
            'Ações': 8,
            'AçõesExterior': 3,
            'InvExterior': 12,
            'AlocMulti': 16,
            'AlocAções': 2, 
        }        

        return labels.get(name, ClasseValorChoices.UNKNOWN)