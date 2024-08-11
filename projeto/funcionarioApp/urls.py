from django.urls import path  # type: ignore
from .views import funcionario_create_view, funcionario_list_view, funcionario_update_view, funcionario_delete_view


app_name = 'funcionario'

urlpatterns = [
    path('create/', funcionario_create_view,
         name='create_funcionario'),  # type: ignore
    path('list/', funcionario_list_view, name='list_funcionario'),
    path('edit/<str:pk>', funcionario_update_view, name='update_funcionario'),
    path('delete/<str:pk>', funcionario_delete_view, name='delete_funcionario')
]
