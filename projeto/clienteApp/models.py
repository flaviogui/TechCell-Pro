from django.db import models  # type: ignore
import uuid
from cpf_field.models import cpffield  # type: ignore
from .my_package import cpf_field  # type: ignore
# Create your models here.


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=16, null=True, blank=True)
    cpf = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome
