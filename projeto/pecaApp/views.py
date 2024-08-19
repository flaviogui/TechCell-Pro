from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Peca
from .forms import PecaForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um funcionario


def peca_create_view(request):
    form = PecaForm()
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peça Criada com Sucesso!')
            return redirect(reverse('peca:list_peca'))
    context = {
        'form': form
    }
    return render(request, 'peca_form.html', context)


def peca_list_view(request):
    pecas = Peca.objects.all()
    context = {'pecas': pecas}
    return render(request, 'peca_list.html', context)


def peca_update_view(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    form = PecaForm(request.POST or None, instance=peca)
    if form.is_valid():
        form.save()
        messages.success(request, 'Peça Alterada com Sucesso!')
        return redirect(reverse('peca:list_peca'))
    context = {
        'form': form
    }
    return render(request, 'peca_update.html', context)


def peca_delete_view(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    peca.delete()
    return redirect(reverse('peca:list_peca'))
