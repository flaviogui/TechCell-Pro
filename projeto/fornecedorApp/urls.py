from django.urls import path  # type: ignore
from .views import fornecedor_create_view, fornecedor_list_view, fornecedor_update_view, fornecedor_delete_view


app_name = 'fornecedor'

urlpatterns = [
    path('create/', fornecedor_create_view,
         name='create_fornecedor'),  # type: ignore
    path('list/', fornecedor_list_view, name='list_fornecedor'),
    path('edit/<str:pk>', fornecedor_update_view, name='update_fornecedor'),
    path('delete/<str:pk>', fornecedor_delete_view, name='delete_fornecedor')
]
