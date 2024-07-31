from django.contrib import admin # type: ignore
from .models import Aparelho, ConfirmacaoReparo

# Registro dos modelos para o admin
admin.site.register(Aparelho)
admin.site.register(ConfirmacaoReparo)
