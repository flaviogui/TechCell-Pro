from datetime import datetime, timezone
from django.db import models  # type: ignore
import uuid

# Create your models here.


class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=16, null=True, blank=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=25)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    data_cadastro = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome']

    def __str__(self):
        return self.nome
