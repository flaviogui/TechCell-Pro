from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore
from django.views.decorators.http import require_http_methods  # type: ignore
# Função para criar um cliente


@require_http_methods(["POST"])  # type: ignore
def cliente_create_view(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Criado com Sucesso!')
            return redirect(reverse('cliente:list_cliente'))
    context = {
        'form': form
    }
    return render(request, 'cliente_form.html', context)


@require_http_methods(["GET"])
def cliente_list_view(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente_list.html', context)


@require_http_methods(["PATCH"])
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


@require_http_methods(["DELETE"])
def cliente_delete_view(pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect(reverse('cliente:list_cliente'))
