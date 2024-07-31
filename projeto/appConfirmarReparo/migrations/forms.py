from django import forms
from .models import Reparo

class ConfirmarReparoForm(forms.ModelForm):
    class Meta:
        model = Reparo
        fields = ['custo_estimado', 'descricao_problema']
