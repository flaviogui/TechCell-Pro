from django import forms  # type: ignore
from pecaApp.models import Peca  # type: ignore


class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = '__all__'
