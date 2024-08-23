from django.db import models  # type: ignore
import uuid

# Create your models here.


class Servico(models.Model):
    STATUS_CHOICES = [
        ('-', '-'),
        ('limpeza', 'Limpeza'),
        ('formatação_backup', 'Formatação e Backup'),
        ('reparo', 'Reparo'),
        ('troca_tela', 'Troca de Tela'),
        ('substituicao_bateria', 'Substituição de Bateria'),
        ('remocao_virus', 'Remoção de Vírus'),
        ('atualizacao_sistema', 'Atualização de Sistema'),
        ('recuperacao_dados', 'Recuperação de Dados'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    preco = models.IntegerField()
    duracao = models.CharField(max_length=10)
    tipo = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default='-')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['nome']

    def __str__(self):
        return self.nome
