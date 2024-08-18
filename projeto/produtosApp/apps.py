from django.apps import AppConfig # type: ignore


class ProdutoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtosApp'
