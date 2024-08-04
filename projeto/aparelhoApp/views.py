from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .models import Aparelho
from .forms import AparelhoForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um aparelho
def aparelho_create_view(request):
    if request.method == 'POST':
        form = AparelhoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aparelho criado com sucesso!')
            return redirect(reverse('aparelho:list_aparelho'))
    else:
        form = AparelhoForm()
    
    context = {
        'form': form
    }
    return render(request, 'aparelho_form.html', context)

# Função para listar aparelhos
def aparelho_list_view(request):
    aparelhos = Aparelho.objects.all()
    context = {'aparelhos': aparelhos}
    return render(request, 'aparelho_list.html', context)

# Função para atualizar um aparelho
def aparelho_update_view(request, pk):
    aparelho = get_object_or_404(Aparelho, pk=pk)
    if request.method == 'POST':
        form = AparelhoForm(request.POST, instance=aparelho)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aparelho alterado com sucesso!')
            return redirect(reverse('aparelho:list_aparelho'))
    else:
        form = AparelhoForm(instance=aparelho)
    
    context = {
        'form': form
    }
    return render(request, 'aparelho_update.html', context)

# Função para excluir um aparelho
def aparelho_delete_view(request, pk):
    aparelho = get_object_or_404(Aparelho, pk=pk)
    if request.method == 'POST':
        aparelho.delete()
        messages.success(request, 'Aparelho excluído com sucesso!')
        return redirect(reverse('aparelho:list_aparelho'))
    
    context = {'aparelho': aparelho}
    return render(request, 'aparelho_confirm_delete.html', context)
