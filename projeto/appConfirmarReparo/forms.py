from django import forms  # type: ignore
from .models import Reparo  # type: ignore


class ConfirmarReparoForm(forms.ModelForm):
    class Meta:
        model = Reparo
        fields = ['status', 'data_inicio', 'data_conclusao',
                  'custo_estimado', 'cliente_notificado']
        widgets = {
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_conclusao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
