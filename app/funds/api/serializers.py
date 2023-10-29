from rest_framework import serializers
from funds.models import Fund, Guia, Document, DailyReport


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = "__all__"


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = "__all__"


class FundSerializer(serializers.ModelSerializer):
    subsets = serializers.SerializerMethodField()
    class Meta:
        model = Fund
        fields = '__all__'
        
    def get_subsets(self, obj):
        return {
            "daily_data": obj.daily_data.exists(),
            "metrics": obj.metrics.exists(),
            "documents": obj.documents.exists(),
            "stars": obj.stars.exists(),
            "scores": obj.scores.exists(),
        }


class FundMiniSerializer(serializers.ModelSerializer):  
    classe_valor = serializers.SerializerMethodField()
    class Meta:
        model = Fund
        fields = ('id', 'cnpj_fundo', 'nome', 'classe_valor', 'classe', 'denom_social', 'vl_patrim_liq')

    def get_classe_valor(self, obj):
        return obj.get_classe_valor_display()


class DocumentSerializer(serializers.ModelSerializer):
    fund = FundMiniSerializer()
    class Meta:
        model = Document
        fields = "__all__"

