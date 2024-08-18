from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages
from django.urls import reverse

# Função para criar um produto
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect(reverse('produtos:listar_produtos'))  # Corrigido para incluir o app_name
    else:
        form = ProdutoForm()

    context = {
        'form': form
    }
    return render(request, 'criar_produto.html', context)

# Função para listar produtos
def listar_produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'listar_produtos.html', context)

# Função para visualizar um produto
def visualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    context = {'produto': produto}
    return render(request, 'visualizar_produto.html', context)

# Função para editar um produto
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto alterado com sucesso!')
            return redirect(reverse('produtos:listar_produtos'))  # Corrigido para incluir o app_name
    else:
        form = ProdutoForm(instance=produto)

    context = {
        'form': form
    }
    return render(request, 'editar_produto.html', context)

# Função para excluir um produto
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect(reverse('produtos:listar_produtos'))  # Corrigido para incluir o app_name

    context = {'produto': produto}
    return render(request, 'excluir_produto.html', context)
