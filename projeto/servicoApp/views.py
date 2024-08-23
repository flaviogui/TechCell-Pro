from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Servico
from .forms import ServicoForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um funcionario


def servico_create_view(request):
    form = ServicoForm()
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço Criado com Sucesso!')
            return redirect(reverse('servico:list_servico'))
    context = {
        'form': form
    }
    return render(request, 'servico_form.html', context)


def servico_list_view(request):
    servicos = Servico.objects.all()
    context = {'servicos': servicos}
    return render(request, 'servico_list.html', context)


def servico_update_view(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    form = ServicoForm(request.POST or None, instance=servico)
    if form.is_valid():
        form.save()
        messages.success(request, 'Serviço Alterado com Sucesso!')
        return redirect(reverse('servico:list_servico'))
    context = {
        'form': form
    }
    return render(request, 'servico_update.html', context)


def servico_delete_view(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    servico.delete()
    return redirect(reverse('servico:list_servico'))
