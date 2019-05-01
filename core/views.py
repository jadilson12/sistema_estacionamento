from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)


def home(request):
    context = {'mensagem': 'ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativo(request):
    mov_rot = MovRotativo.objects.all()
    return render(
        request, 'core/lista_movrotativo.html', {'movrotativo': mov_rot})


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    return render(
        request, 'core/lista_mensalista.html', {'mensalistas': mensalistas})


def lista_movmensalista(request):
    mov_mens = MovMensalista.objects.all()
    return render(
        request, 'core/lista_movmensalista.html', {'mov_mens': mov_mens})
