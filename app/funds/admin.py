from django.contrib import admin
from funds.models import Fund, Guia, DailyReport, Document, Star, Score
# Register your models here.

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    search_fields = ("fund__cnpj_fundo",)
    raw_id_fields = ('fund',)

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    search_fields = ("fund__cnpj_fundo",)
    raw_id_fields = ('fund',)

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    search_fields = ("denom_social", "cnpj_fundo", "id")

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ("fund__cnpj_fundo", "tipoDocumento", "fund__denom_social")
    raw_id_fields = ('fund',)

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    raw_id_fields = ('fund',)

@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("fund", "dt_comptc")
    raw_id_fields = ('fund',)
