from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Ferramenta
from .forms import FerramentaForm
from django.contrib import messages  # type: ignore
from django.urls import reverse  # type: ignore

# Função para criar um cliente


def ferramenta_create_view(request):
    form = FerramentaForm()
    if request.method == 'POST':
        form = FerramentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ferramenta Criada com Sucesso!')
            return redirect(reverse('ferramenta:list_ferramenta'))
    context = {
        'form': form
    }
    return render(request, 'ferramenta_form.html', context)


def ferramenta_list_view(request):
    ferramenta = Ferramenta.objects.all()
    context = {'ferramenta': ferramenta}
    return render(request, 'ferramenta_list.html', context)


def ferramenta_update_view(request, pk):
    ferramenta = get_object_or_404(Ferramenta, pk=pk)
    form = FerramentaForm(request.POST or None, instance=ferramenta)
    if form.is_valid():
        form.save()
        messages.success(request, 'Ferramenta Alterado com Sucesso!')
        return redirect(reverse('ferramenta:list_ferramenta'))
    context = {
        'form': form
    }
    return render(request, 'ferramenta_update.html', context)


def ferramenta_delete_view(request, pk):
    ferramenta = get_object_or_404(Ferramenta, pk=pk)
    ferramenta.delete()
    return redirect(reverse('ferramenta:list_ferramenta'))
