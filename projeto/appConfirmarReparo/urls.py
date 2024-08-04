from django.urls import path # type: ignore
from . import views

app_name = 'appConfirmarReparo'


urlpatterns = [
    path('lista_reparos', views.lista_reparos, name='lista_reparos'),
    path('reparo/<int:pk>/', views.reparo_detalhes, name='reparo_detalhes'),
    path('confirmar_reparo/<int:pk>/', views.confirmar_reparo, name='confirmar_reparo'),
    
]

