from django import forms  # type: ignore
from funcionarioApp.models import Funcionario  # type: ignore


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
