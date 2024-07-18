from django.db import models # type: ignore
import uuid

# Modelo para Aparelho
class Aparelho(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    imei = models.CharField(max_length=15, unique=True)
    numero_serie = models.CharField(max_length=50, unique=True)
    descricao_problema = models.TextField()
    ordem_servico = models.CharField(max_length=36, unique=True, null=True, blank=True)

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

# Implementação de funções adicionais para interagir com o modelo

from django.core.exceptions import ObjectDoesNotExist # type: ignore

def cadastrar_aparelho(marca, modelo, imei, numero_serie, descricao_problema):
    aparelho = Aparelho(marca=marca, modelo=modelo, imei=imei, numero_serie=numero_serie, descricao_problema=descricao_problema)
    aparelho.save()
    return aparelho.ordem_servico

def alterar_aparelho(id_aparelho, marca=None, modelo=None, imei=None, numero_serie=None, descricao_problema=None):
    try:
        aparelho = Aparelho.objects.get(id=id_aparelho)
        if marca:
            aparelho.marca = marca
        if modelo:
            aparelho.modelo = modelo
        if imei:
            aparelho.imei = imei
        if numero_serie:
            aparelho.numero_serie = numero_serie
        if descricao_problema:
            aparelho.descricao_problema = descricao_problema
        aparelho.save()
        return True
    except ObjectDoesNotExist:
        return False

def consultar_aparelho(numero_serie):
    try:
        aparelho = Aparelho.objects.get(numero_serie=numero_serie)
        return aparelho
    except ObjectDoesNotExist:
        return None

def visualizar_detalhes_aparelho(id_aparelho):
    try:
        aparelho = Aparelho.objects.get(id=id_aparelho)
        return aparelho
    except ObjectDoesNotExist:
        return None

def excluir_aparelho(id_aparelho):
    try:
        aparelho = Aparelho.objects.get(id=id_aparelho)
        aparelho.delete()
        return True
    except ObjectDoesNotExist:
        return False