from django.urls import path  # type: ignore
from .views import peca_create_view, peca_list_view, peca_update_view, peca_delete_view


app_name = 'peca'

urlpatterns = [
    path('create/', peca_create_view,
         name='create_peca'),  # type: ignore
    path('list/', peca_list_view, name='list_peca'),
    path('edit/<str:pk>', peca_update_view, name='update_peca'),
    path('delete/<str:pk>', peca_delete_view, name='delete_peca')
]
