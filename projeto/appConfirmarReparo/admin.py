from django.contrib import admin # type: ignore
from .models import Reparo

# Registro dos modelos para o admin

admin.site.register(Reparo)
