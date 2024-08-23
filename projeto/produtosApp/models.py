from django.db import models  # type: ignore
import uuid

# Modelo para Produto


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, default='nome')
    descricao = models.CharField(max_length=255, default='Descrição padrão')
    cod_barras = models.CharField(max_length=130, unique=True)
    preco = models.FloatField()
    categoria = models.CharField(
        max_length=255, default='Categoria do produto')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome', 'preco']

    def __str__(self):
        return f"{self.nome} - {self.descricao}"

    def save(self, *args, **kwargs):
        super(Produto, self).save(*args, **kwargs)
