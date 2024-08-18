from django.contrib import admin # type: ignore

# Register your models here.

from .models import Produto

admin.site.register(Produto)