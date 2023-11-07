from rest_framework import serializers

from eleicoes.models import StateData, BRData, MunData

class StateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateData
        fields = "__all__"

class BRDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BRData
        fields = "__all__"

class MunDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunData
        fields = "__all__"
