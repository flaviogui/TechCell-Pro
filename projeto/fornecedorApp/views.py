from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Fornecedor
from .forms import FornecedorForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um funcionario


def fornecedor_create_view(request):
    form = FornecedorForm()
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor Criado com Sucesso!')
            return redirect(reverse('fornecedor:list_fornecedor'))
    context = {
        'form': form
    }
    return render(request, 'fornecedor_form.html', context)


def fornecedor_list_view(request):
    fornecedores = fornecedores.objects.all()
    context = {'fornecedores: ffornecedores'}
    return render(request, 'fornecedor_list.html', context)


def fornecedor_update_view(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Fornecedor Alterado com Sucesso!')
        return redirect(reverse('fornecedor:list_fornecedor'))
    context = {
        'form': form
    }
    return render(request, 'fornecedor_update.html', context)


def fornecedor_delete_view(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    return redirect(reverse('fornecedor:list_fornecedor'))
