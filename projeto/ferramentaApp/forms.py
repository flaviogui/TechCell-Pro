from django import forms
from .models import Ferramenta

class FerramentaForm(forms.ModelForm):
    class Meta:
        model = Ferramenta
        fields = ['nome', 'descricao', 'codigo', 'quantidade_disponivel', 'condicao', 'fornecedor']
