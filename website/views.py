from django.shortcuts import render


def home(resquest):
    return render(resquest, 'website/index.html')
