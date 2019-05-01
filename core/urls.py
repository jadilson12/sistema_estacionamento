from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.home, name='core_home'),
    path('pessoas/', v.lista_pessoas, name='core_lista_pessoas'),
    path('pessoas/criar', v.criar_pessoas, name='core_criar_pessoas'),
    path('pessoas/update/<int:id>', v.update_pessoa, name='core_update_pessoa'),

    path('veiculos/', v.lista_veiculos, name='core_lista_veiculos'),
    path('veiculos/criar', v.criar_veiculos, name='core_criar_veiculos'),
    path('veiculos/update/<int:id>', v.update_veiculo, name='core_update_veiculo'),

    path('mov-rot/', v.lista_movrotativo, name='core_lista_movrotativo'),
    path('mov-rot/criar', v.criar_movrotativo, name='core_criar_movrotativo'),
    path('mov-rot/update/<int:id>', v.update_movrotativo, name='core_update_movrotativo'),

    path('mensalistas/', v.lista_mensalista, name='core_lista_mensalista'),
    path('mensalistas/criar', v.criar_mensalista, name='core_criar_mensalista'),
    path('mensalistas/update/<int:id>', v.update_mensalista, name='core_update_mensalista'),

    path('mov-mens/', v.lista_movmensalista, name='core_lista_movmensalista'),
    path('mov-mens/criar', v.criar_movmensalista, name='core_criar_movmensalista'),
    path('mov-mens/update/<int:id>', v.update_movmensalista, name='core_update_movmensalista')
]
