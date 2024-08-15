from django import forms  # type: ignore
from fornecedorApp.models import Fornecedor  # type: ignore


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
