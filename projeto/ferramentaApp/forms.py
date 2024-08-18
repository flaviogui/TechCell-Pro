from django import forms  # type: ignore
from ferramentaApp.models import Ferramenta  # type: ignore

class FerramentaForm(forms.ModelForm):
    class Meta:
        model = Ferramenta
        fields = '__all__'
