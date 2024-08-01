from http.client import HTTPResponse
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
            reparo.status = 'concluido'
            reparo.data_conclusao = timezone.now()
            reparo.save()
            # Notificar o cliente
            notificar_cliente(reparo) # type: ignore
            return redirect('reparo_detalhes', pk=reparo.pk)
    else:
        form = ConfirmarReparoForm(instance=reparo)
    return render(request, 'confirmar_reparo.html', {
        'form': form,
        'reparo': reparo,
    })
