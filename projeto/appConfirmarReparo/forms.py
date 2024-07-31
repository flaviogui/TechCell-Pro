from django import forms # type: ignore
from .models import Reparo # type: ignore

class ConfirmarReparoForm(forms.ModelForm):
    class Meta:
        model = Reparo
        fields = ['custo_estimado', 'descricao_problema']
