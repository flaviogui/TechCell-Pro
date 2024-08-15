from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Produto
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def visualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'visualizar_produto.html', {'produto': produto})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Corrigido para o nome da URL
    else:
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Corrigido para o nome da URL
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')  # Corrigido para o nome da URL
    return render(request, 'excluir_produto.html', {'produto': produto})
