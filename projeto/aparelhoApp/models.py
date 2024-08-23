# models.py
from django.db import models
import uuid
from clienteApp.models import Cliente  # Importar o modelo Cliente

class Aparelho(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, default='nome')
    descricao = models.CharField(max_length=255, default='Descrição padrão')
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    imei = models.CharField(max_length=15, unique=True)
    numero_serie = models.CharField(max_length=50, unique=True)
    descricao_problema = models.TextField()
    ordem_servico = models.CharField(max_length=36, unique=True, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = 'Aparelho'
        verbose_name_plural = 'Aparelhos'
        ordering = ['marca', 'modelo']

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.numero_serie}"

    def save(self, *args, **kwargs):
        if not self.ordem_servico:
            self.ordem_servico = str(uuid.uuid4())
        super(Aparelho, self).save(*args, **kwargs)
