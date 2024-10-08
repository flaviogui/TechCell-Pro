"""
URL configuration for techcell_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # type: ignore
from django.urls import path, include   # type: ignore
from django.views.generic import TemplateView  # type: ignore


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('clienteApp.urls')),
    path('aparelho/', include('aparelhoApp.urls')),
    path('appConfirmarReparo/', include('appConfirmarReparo.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    # path('', TemplateView.as_view(template_name="index.html"))
    path('funcionario/', include('funcionarioApp.urls')),
    path('fornecedor/', include('fornecedorApp.urls')),
    path('produtos/', include('produtosApp.urls')),
    path('ferramenta/', include('ferramentaApp.urls')),
    path('servico/', include('servicoApp.urls')),
    path('peca/', include('pecaApp.urls'))
]
