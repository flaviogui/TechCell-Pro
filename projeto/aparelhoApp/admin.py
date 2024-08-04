from django.contrib import admin # type: ignore

# Register your models here.

from .models import Aparelho

admin.site.register(Aparelho)