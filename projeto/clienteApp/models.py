from django.db import models  # type: ignore
import uuid
from cpf_field.models import CPFField  # type: ignore # Use CPFField
# Create your models here.


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=16, null=True, blank=True)
    cpf = CPFField('cpf')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome
