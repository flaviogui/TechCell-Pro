# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Ferramenta
from .forms import FerramentaForm

def list_ferramentas(request):
    ferramentas = Ferramenta.objects.all()
    return render(request, 'ferramentaApp/list.html', {'ferramentas': ferramentas})

def detail_ferramenta(request, pk):
    ferramenta = get_object_or_404(Ferramenta, pk=pk)
    return render(request, 'ferramentaApp/detail.html', {'ferramenta': ferramenta})

def create_ferramenta(request):
    if request.method == "POST":
        form = FerramentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ferramentaApp:list_ferramentas')
    else:
        form = FerramentaForm()
    return render(request, 'ferramentaApp/form.html', {'form': form})

def update_ferramenta(request, pk):
    ferramenta = get_object_or_404(Ferramenta, pk=pk)
    if request.method == "POST":
        form = FerramentaForm(request.POST, instance=ferramenta)
        if form.is_valid():
            form.save()
            return redirect('ferramentaApp:detail_ferramenta', pk=ferramenta.pk)
    else:
        form = FerramentaForm(instance=ferramenta)
    return render(request, 'ferramentaApp/form.html', {'form': form})

def delete_ferramenta(request, pk):
    ferramenta = get_object_or_404(Ferramenta, pk=pk)
    if request.method == "POST":
        ferramenta.delete()
        return redirect('ferramentaApp:list_ferramentas')
    return render(request, 'ferramentaApp/confirm_delete.html', {'ferramenta': ferramenta})

