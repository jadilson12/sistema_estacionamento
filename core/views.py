from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)
from .forms import (
    PessoaForm,
    MovRotativoForm,
    MovMensalistaForm,
    MensalistaForm,
    VeiculoForm
)


def home(request):
    context = {'mensagem': 'ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def criar_pessoas(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def update_pessoa(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    data = {'obj': pessoa}
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', data)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def criar_veiculos(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def update_veiculo(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


def delete_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    data = {'obj': veiculo}
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', data)


def lista_movrotativo(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movrotativo': mov_rot, 'form': form}
    return render(request, 'core/lista_movrotativo.html', data)


def criar_movrotativo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativo')


def update_movrotativo(request, id):
    data = {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/update_movrotativo.html', data)


def delete_movrotativo(request, id):
    movrotativo = MovRotativo.objects.get(id=id)
    data = {'obj': movrotativo}
    if request.method == 'POST':
        movrotativo.delete()
        return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/delete_confirm.html', data)


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalista.html', data)


def criar_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


def update_mensalista(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


def delete_mensalista(request, id):
    mensalista = Mensalista.objects.get(id=id)
    data = {'obj': mensalista}
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', data)
    

def lista_movmensalista(request):
    movmensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'movmensalistas': movmensalistas, 'form': form}
    return render(request, 'core/lista_movmensalista.html', data)


def criar_movmensalista(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')


def update_movmensalista(request, id):
    data = {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/update_movmensalista.html', data)


def delete_movmensalista(request, id):
    movmensalista = MovMensalista.objects.get(id=id)
    data = {'obj': movmensalista}
    if request.method == 'POST':
        movmensalista.delete()
        return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/delete_confirm.html', data)
