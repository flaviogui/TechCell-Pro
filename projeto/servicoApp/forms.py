from django import forms  # type: ignore
from servicoApp.models import Servico  # type: ignore


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
