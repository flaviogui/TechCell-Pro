from http.client import HTTPResponse
from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.utils import timezone # type: ignore
from .models import Reparo
from .forms import ConfirmarReparoForm


def index(request):
    return HTTPResponse("Hello, world. You're at the index.")

def confirmar_reparo(request, pk):
    reparo = get_object_or_404(Reparo, pk=pk)
    if request.method == 'POST':
        form = ConfirmarReparoForm(request.POST, instance=reparo)
        if form.is_valid():
            reparo = form.save(commit=False)
            reparo.save()
            return redirect('appConfirmarReparo:reparo_detalhes', pk=reparo.pk)
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
            return redirect('lista_reparos.html')  
    else:
        form = ConfirmarReparoForm()
    
    return render(request, 'reparo_create.html', {'form': form})