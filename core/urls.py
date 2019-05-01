from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.home, name='core_home'),
    path('pessoas/', v.lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', v.lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot/', v.lista_movrotativo, name='core_movrotativo'),
    path('mensalista/', v.lista_mensalista, name='core_mensalista'),
    path('mov-mens/', v.lista_movmensalista, name='core_movmensalista')
]
