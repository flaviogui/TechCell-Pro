from django.contrib import admin # type: ignore
from .models import Produto

admin.site.register(Produto)
