from django import forms  # type: ignore
from aparelhoApp.models import Aparelho  # type: ignore


class AparelhoForm(forms.ModelForm):
    class Meta:
        model = Aparelho
        fields = '__all__'