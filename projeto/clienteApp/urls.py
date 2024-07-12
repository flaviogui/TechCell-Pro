from django.urls import path  # type: ignore
from .views import *


app_name = 'cliente'

urlpatterns = [
    path('create/', cliente_create_view, name='create_cliente'),  # type: ignore
    path('list/', cliente_list_view, name='list_cliente'),
    path('edit/<str:pk>', cliente_update_view, name='update_cliente'),
    path('delete/<str:pk>', cliente_delete_view, name='delete_cliente')
]
