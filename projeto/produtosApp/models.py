from django.db import models # type: ignore

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    codigo_barras = models.CharField(max_length=13, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
