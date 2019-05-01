from django.contrib import admin
from .models import (
    Pessoa,
    Marca,
    Veiculo,
    Parametro,
    MovRotativo,
    Mensalista,
    MovMensalista
)


class MovRotativoAmdin(admin.ModelAdmin):
    list_display = (
        'veiculo', 'checkin', 'checkout', 'valor_hora', 'pago', 'total', 'horas_total')

    def veiculo(self, obj):
        return obj.veiculo


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'data_pgto', 'total')


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametro)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAmdin)
