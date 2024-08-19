from django.urls import path  # type: ignore
from .views import servico_create_view, servico_list_view, servico_update_view, servico_delete_view


app_name = 'servico'

urlpatterns = [
    path('create/', servico_create_view,
         name='create_fornecedor'),  # type: ignore
    path('list/', servico_list_view, name='list_fornecedor'),
    path('edit/<str:pk>', servico_update_view, name='update_fornecedor'),
    path('delete/<str:pk>', servico_delete_view, name='delete_fornecedor')
]
