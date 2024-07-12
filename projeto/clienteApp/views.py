from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um cliente


def cliente_create_view(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Criado com Sucesso!')
            return redirect(reverse('cliente:create_cliente'))
    context = {
        'form': form
    }
    return render(request, 'cliente_form.html', context)


def cliente_list_view(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente_list.html', context)


def cliente_update_view(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário Alterado com Sucesso!')
        return redirect(reverse('cliente:list_cliente'))
    context = {
        'form': form
    }
    return render(request, 'cliente_update.html', context)


def cliente_delete_view(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect(reverse('cliente:list_cliente'))
