from django.contrib import admin  # type: ignore
from .models import Peca

# Registro dos modelos para o admin

admin.site.register(Peca)
