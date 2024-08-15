from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('<int:pk>/', views.visualizar_produto, name='visualizar_produto'),
    path('novo/', views.criar_produto, name='criar_produto'),
    path('<int:pk>/editar/', views.editar_produto, name='editar_produto'),
    path('<int:pk>/excluir/', views.excluir_produto, name='excluir_produto'),
]
