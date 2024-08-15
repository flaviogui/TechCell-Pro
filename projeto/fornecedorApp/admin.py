from django.contrib import admin  # type: ignore

# Register your models here.

from .models import Fornecedor

admin.site.register(Fornecedor)
