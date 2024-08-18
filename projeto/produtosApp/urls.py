<<<<<<< HEAD
from django.urls import path
from . import views
=======
from django.urls import path  # type: ignore
from .views import produto_create_view, produto_list_view, produto_update_view, produto_delete_view

app_name = 'produto'
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520

app_name = 'produtos'

urlpatterns = [
<<<<<<< HEAD
    path('', views.listar_produtos, name='listar_produtos'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('<int:pk>/', views.visualizar_produto, name='visualizar_produto'),
    path('<int:pk>/editar/', views.editar_produto, name='editar_produto'),
    path('<int:pk>/excluir/', views.excluir_produto, name='excluir_produto'),
=======
    path('create/', produto_create_view, name='create_produto'),
    path('list/', produto_list_view, name='list_produto'),
    path('update/<uuid:pk>', produto_update_view, name='update_produto'),
    path('delete/<uuid:pk>', produto_delete_view, name='delete_produto'),
>>>>>>> ade1cd5856bba61e60f916571a9c5ed28f9ea520
]