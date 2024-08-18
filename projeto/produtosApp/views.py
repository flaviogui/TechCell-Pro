from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um aparelho


def produto_create_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect(reverse('produto:list_produto'))
    else:
        form = ProdutoForm()

    context = {
        'form': form
    }
    return render(request, 'produto_form.html', context)

# Função para listar aparelhos


def produto_list_view(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produto_list.html', context)

# Função para atualizar um aparelho


def produto_update_view(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto alterado com sucesso!')
            return redirect(reverse('produto:list_produto'))
    else:
        form = ProdutoForm(instance=produto)

    context = {
        'form': form
    }
    return render(request, 'produto_update.html', context)

# Função para excluir um aparelho


def produto_delete_view(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect(reverse('produto:list_produto'))

    context = {'produto': produto}
    return render(request, 'produto_confirm_delete.html', context)
