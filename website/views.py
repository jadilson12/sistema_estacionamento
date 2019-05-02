from django.shortcuts import render


def home(resquest):
    return render(resquest, 'website/index.html')


def contato(resquest):
    return render(resquest, 'website/contato.html')
