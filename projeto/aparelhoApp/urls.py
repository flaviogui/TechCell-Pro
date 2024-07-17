from django.urls import path
from .views import aparelho_create_view, aparelho_list_view, aparelho_update_view, aparelho_delete_view

app_name = 'aparelho'

urlpatterns = [
    path('create/', aparelho_create_view, name='create_aparelho'),
    path('list/', aparelho_list_view, name='list_aparelho'),
    path('update/<int:pk>/', aparelho_update_view, name='update_aparelho'),
    path('delete/<int:pk>/', aparelho_delete_view, name='delete_aparelho'),
]