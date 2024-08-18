from django.urls import path  # type: ignore
from .views import ferramenta_create_view, ferramenta_list_view, ferramenta_update_view, ferramenta_delete_view


app_name = 'ferramenta'

urlpatterns = [
    path('create/', ferramenta_create_view, name='create_ferramenta'),  # type: ignore
    path('list/', ferramenta_list_view, name='list_ferramenta'),
    path('edit/<str:pk>', ferramenta_update_view, name='update_ferramenta'),
    path('delete/<str:pk>', ferramenta_delete_view, name='delete_ferramenta')
]
