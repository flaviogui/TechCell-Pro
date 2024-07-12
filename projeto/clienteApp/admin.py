from django.contrib import admin # type: ignore

# Register your models here.

from .models import Cliente

admin.site.register(Cliente)