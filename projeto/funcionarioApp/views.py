from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Funcionario
from .forms import FuncionarioForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um funcionario


def funcionario_create_view(request):
    form = FuncionarioForm()
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário Criado com Sucesso!')
            return redirect(reverse('cliente:list_cliente'))
    context = {
        'form': form
    }
    return render(request, 'funcionario_form.html', context)


def funcionario_list_view(request):
    funcionarios = Funcionario.objects.all()
    context = {'funcionarios': funcionarios}
    return render(request, 'funcionario_list.html', context)


def funcionario_update_view(request, pk):
    cliente = get_object_or_404(Funcionario, pk=pk)
    form = FuncionarioForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        messages.success(request, 'Funcionário Alterado com Sucesso!')
        return redirect(reverse('funcionario:list_funcionario'))
    context = {
        'form': form
    }
    return render(request, 'funcionario_update.html', context)


def funcionario_delete_view(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.delete()
    return redirect(reverse('funcionario:list_funcionario'))
