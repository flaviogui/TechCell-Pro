from django.contrib import admin  # type: ignore

# Register your models here.

from .models import Servico

admin.site.register(Servico)
