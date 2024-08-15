from django.db import models

# Create your models here.

class Ferramenta(models.Model):
    CONDICAO_CHOICES = [
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('danificado', 'Danificado'),
    ]
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    codigo = models.CharField(max_length=50, unique=True)
    quantidade_disponivel = models.PositiveIntegerField()
    condicao = models.CharField(max_length=20, choices=CONDICAO_CHOICES)
    fornecedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

