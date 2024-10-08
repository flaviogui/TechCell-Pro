from django import forms # type: ignore

from aparelhoApp.models import Aparelho # type: ignore
from .models import Reparo # type: ignore

class ConfirmarReparoForm(forms.ModelForm):
    aparelho = forms.ModelChoiceField(queryset=Aparelho.objects.all(), label="Aparelho")

    class Meta:
        model = Reparo
        fields = ['aparelho','status', 'data_inicio', 'data_conclusao', 'custo_estimado', 'cliente_notificado']
        widgets = {
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_conclusao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['custo_estimado'].required = True 