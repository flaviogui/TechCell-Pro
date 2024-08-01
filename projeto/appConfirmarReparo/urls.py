# confirmarreparo/urls.py

from django.urls import path # type: ignore
from . import views

app_name = 'appConfirmarReparo'


urlpatterns = [
    path('confirmar_reparo/<int:pk>/', views.confirmar_reparo, name='confirmar_reparo'),
    
]

