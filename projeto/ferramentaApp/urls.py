from django.urls import path
from . import views

app_name = 'ferramenta'

urlpatterns = [
    path('', views.list_ferramentas, name='list_ferramentas'),
    path('<int:pk>/', views.detail_ferramenta, name='detail_ferramenta'),
    path('create/', views.create_ferramenta, name='create_ferramenta'),
    path('<int:pk>/update/', views.update_ferramenta, name='update_ferramenta'),
    path('<int:pk>/delete/', views.delete_ferramenta, name='delete_ferramenta'),
]
