from django import forms # type: ignore
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'codigo_barras', 'preco', 'categoria']
