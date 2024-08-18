from django import forms  # type: ignore
from produtosApp.models import Produto  # type: ignore


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'