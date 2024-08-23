# forms.py
from django import forms
from aparelhoApp.models import Aparelho
from clienteApp.models import Cliente

class AparelhoForm(forms.ModelForm):
    class Meta:
        model = Aparelho
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),  # Adiciona um widget de seleção para o cliente
        }
