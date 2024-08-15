from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produto/<int:pk>/', views.visualizar_produto, name='visualizar_produto'),
    path('produto/novo/', views.criar_produto, name='criar_produto'),
    path('produto/<int:pk>/editar/', views.editar_produto, name='editar_produto'),
    path('produto/<int:pk>/excluir/', views.excluir_produto, name='excluir_produto'),
]
