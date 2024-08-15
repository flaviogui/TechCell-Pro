from django.db import models  # type: ignore
import uuid

# Create your models here.

class Ferramenta(models.Model):
    CONDICAO_CHOICES = [
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('danificado', 'Danificado'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    codigo = models.CharField(max_length=50, unique=True)
    quantidade_disponivel = models.PositiveIntegerField()
    condicao = models.CharField(max_length=20, choices=CONDICAO_CHOICES)

    class Meta:
        verbose_name = 'Ferramenta'
        verbose_name_plural = 'Ferramentas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

