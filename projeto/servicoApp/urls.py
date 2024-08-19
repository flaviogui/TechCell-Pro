from django.urls import path  # type: ignore
from .views import servico_create_view, servico_list_view, servico_update_view, servico_delete_view


app_name = 'servico'

urlpatterns = [
    path('create/', servico_create_view,
         name='create_servico'),  # type: ignore
    path('list/', servico_list_view, name='list_servico'),
    path('edit/<str:pk>', servico_update_view, name='update_servico'),
    path('delete/<str:pk>', servico_delete_view, name='delete_servico')
]
