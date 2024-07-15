from django import forms  # type: ignore
from clienteApp.models import Cliente  # type: ignore


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
