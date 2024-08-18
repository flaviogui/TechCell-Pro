<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages
from django.urls import reverse

# Função para criar um produto
def criar_produto(request):
=======
from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um aparelho


def produto_create_view(request):
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
<<<<<<< HEAD
            return redirect(reverse('produtos:listar_produtos'))  # Corrigido para incluir o app_name
=======
            return redirect(reverse('produto:list_produto'))
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520
    else:
        form = ProdutoForm()

    context = {
        'form': form
    }
<<<<<<< HEAD
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
=======
    return render(request, 'produto_form.html', context)

# Função para listar aparelhos


def produto_list_view(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produto_list.html', context)

# Função para atualizar um aparelho


def produto_update_view(request, pk):
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto alterado com sucesso!')
<<<<<<< HEAD
            return redirect(reverse('produtos:listar_produtos'))  # Corrigido para incluir o app_name
=======
            return redirect(reverse('produto:list_produto'))
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520
    else:
        form = ProdutoForm(instance=produto)

    context = {
        'form': form
    }
<<<<<<< HEAD
    return render(request, 'editar_produto.html', context)

# Função para excluir um produto
def excluir_produto(request, pk):
=======
    return render(request, 'produto_update.html', context)

# Função para excluir um aparelho


def produto_delete_view(request, pk):
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
<<<<<<< HEAD
        return redirect(reverse('produtos:listar_produtos'))  # Corrigido para incluir o app_name

    context = {'produto': produto}
    return render(request, 'excluir_produto.html', context)
=======
        return redirect(reverse('produto:list_produto'))

    context = {'produto': produto}
    return render(request, 'produto_confirm_delete.html', context)
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520
