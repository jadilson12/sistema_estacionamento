from django.contrib import admin
from .models import (
    Pessoa,
    Marca,
    Veiculo,
    Parametro,
    MovRotativo
)


class MovRotativoAmdin(admin.ModelAdmin):
    list_display = (
         'veiculo','checkin', 'checkout', 'valor_hora', 'pago', 'total', 'horas_total')

    def veiculo(self, obj):
        return obj.veiculo


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametro)
admin.site.register(MovRotativo, MovRotativoAmdin)
