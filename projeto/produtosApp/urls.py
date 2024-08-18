from django.urls import path  # type: ignore
from .views import produto_create_view, produto_list_view, produto_update_view, produto_delete_view

app_name = 'produto'

urlpatterns = [
    path('create/', produto_create_view, name='create_produto'),
    path('list/', produto_list_view, name='list_produto'),
    path('update/<uuid:pk>', produto_update_view, name='update_produto'),
    path('delete/<uuid:pk>', produto_delete_view, name='delete_produto'),
]