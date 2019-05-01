from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.home, name='core_home'),
    path('pessoas/', v.lista_pessoas, name='core_lista_pessoas'),
    path('pessoas/criar', v.criar_pessoas, name='core_criar_pessoas'),

    path('veiculos/', v.lista_veiculos, name='core_lista_veiculos'),
    path('veiculos/criar', v.criar_veiculos, name='core_criar_veiculos'),

    path('mov-rot/', v.lista_movrotativo, name='core_lista_movrotativo'),
    path('mov-rot/criar', v.criar_movrotativo, name='core_criar_movrotativo'),

    path('mensalista/', v.lista_mensalista, name='core_lista_mensalista'),
    path('mensalista/criar', v.criar_mensalista, name='core_criar_mensalista'),

    path('mov-mens/', v.lista_movmensalista, name='core_movmensalista'),
    path('mov-mens/criar', v.criar_movmensalista, name='core_criar_movmensalista')
]
