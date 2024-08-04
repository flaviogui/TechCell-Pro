from django.urls import path  # type: ignore
from .views import cliente_create_view, cliente_list_view, cliente_update_view, cliente_delete_view


app_name = 'cliente'

urlpatterns = [
    path('create/', cliente_create_view, name='create_cliente'),  # type: ignore
    path('list/', cliente_list_view, name='list_cliente'),
    path('edit/<str:pk>', cliente_update_view, name='update_cliente'),
    path('delete/<str:pk>', cliente_delete_view, name='delete_cliente')
]
