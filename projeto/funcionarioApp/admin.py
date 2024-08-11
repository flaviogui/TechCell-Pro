from django.contrib import admin  # type: ignore

# Register your models here.

from .models import Funcionario

admin.site.register(Funcionario)
