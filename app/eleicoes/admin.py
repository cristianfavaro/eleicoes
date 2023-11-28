from django.contrib import admin
from eleicoes.models import BRData, StateData, MunData
# Register your models here.
admin.site.register(BRData)
admin.site.register(StateData)
admin.site.register(MunData)