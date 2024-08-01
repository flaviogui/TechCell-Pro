from django.db import models # type: ignore
from aparelhoApp.models import Aparelho # type: ignore
from django.utils import timezone # type: ignore
from uuid import uuid4

class Reparo(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_progresso', 'Em Progresso'),
        ('concluido', 'Concluído'),
    ]
    aparelho = models.ForeignKey(Aparelho, on_delete=models.CASCADE)
    descricao_problema = models.TextField()
    custo_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateTimeField(default=timezone.now)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    protocolo = models.UUIDField(default=uuid4, editable=False, unique=True)
    cliente_notificado = models.BooleanField(default=False)

    def __str__(self):
        return f'Reparo {self.protocolo} - {self.aparelho.nome}'
    


