from django.db import models  # type: ignore
import uuid
from fornecedorApp.models import Fornecedor  # type: ignore
# Create your models here.


class Peca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=75)
    descricao = models.CharField(max_length=250)
    codigo = models.CharField(max_length=9)
    quantidade = models.IntegerField()
    preco_compra = models.FloatField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Peça'
        verbose_name_plural = 'Peça'
        ordering = ['nome']

    def __str__(self):
        return self.nome
