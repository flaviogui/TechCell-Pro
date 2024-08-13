from django.http import HttpResponse  # Correção do import
from django.contrib import messages  # Correção do import
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Reparo
from .forms import ConfirmarReparoForm


def index(request):
    return HttpResponse("Hello, world. You're at the index.")  # Correção do HttpResponse


def confirmar_reparo(request, pk):
    reparo = get_object_or_404(Reparo, pk=pk)
    if request.method == 'POST':
        form = ConfirmarReparoForm(request.POST, instance=reparo)
        if form.is_valid():
            reparo = form.save(commit=False)
            reparo.save()
            return redirect('appConfirmarReparo:reparo_detalhes', pk=reparo.pk)  # Certifique-se de que o namespace e nome da view estejam corretos
    else:
        form = ConfirmarReparoForm(instance=reparo)
    return render(request, 'confirmar_reparo.html', {
        'form': form,
        'reparo': reparo,
    })


def reparo_detalhes(request, pk):
    reparo = get_object_or_404(Reparo, pk=pk)
    return render(request, 'reparo_detalhes.html', {'reparo': reparo})


def lista_reparos(request):
    reparos = Reparo.objects.all()
    return render(request, 'lista_reparos.html', {'reparos': reparos})


def reparo_create_view(request):
    if request.method == 'POST':
        form = ConfirmarReparoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reparo cadastrado com sucesso!')
            return redirect('appConfirmarReparo:lista_reparos')  # Redireciona para a view nomeada 'lista_reparos'
    else:
        form = ConfirmarReparoForm()

    return render(request, 'reparo_create.html', {'form': form})
