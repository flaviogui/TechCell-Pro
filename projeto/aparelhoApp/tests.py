from django.test import TestCase, Client # type: ignore
from uuid import uuid4
from .models import Aparelho
from django.urls import reverse, resolve  # type: ignore
from .views import (
    aparelho_create_view,
    aparelho_list_view,
    aparelho_update_view,
    aparelho_delete_view,
)

class AparelhoModelTest(TestCase):
    
    def setUp(self):
        """Cria uma instância de Aparelho para os testes."""
        self.aparelho = Aparelho.objects.create(
            nome='Smartphone',
            descricao='Smartphone topo de linha',
            marca='MarcaX',
            modelo='ModeloY',
            imei='123456789012345',
            numero_serie='SN1234567890',
            descricao_problema='Tela quebrada'
        )

    def test_aparelho_creation(self):
        """Testa a criação de um Aparelho."""
        aparelho = Aparelho.objects.get(imei='123456789012345')
        self.assertEqual(aparelho.nome, 'Smartphone')
        self.assertEqual(aparelho.marca, 'MarcaX')
        self.assertEqual(aparelho.numero_serie, 'SN1234567890')

    def test_ordem_servico_default(self):
        """Testa se o campo ordem_servico é gerado automaticamente se não for fornecido."""
        aparelho = Aparelho(
            nome='Tablet',
            descricao='Tablet com tela grande',
            marca='MarcaY',
            modelo='ModeloZ',
            imei='987654321098765',
            numero_serie='SN0987654321',
            descricao_problema='Problema com a bateria'
        )
        aparelho.save()
        self.assertIsNotNone(aparelho.ordem_servico)
        self.assertTrue(len(aparelho.ordem_servico), 36)  # Verifica o comprimento do UUID

    def test_unique_fields(self):
        """Testa se os campos únicos são realmente únicos."""
        with self.assertRaises(Exception):
            Aparelho.objects.create(
                nome='Smartwatch',
                descricao='Smartwatch com GPS',
                marca='MarcaZ',
                modelo='ModeloA',
                imei='123456789012345',  # IMEI duplicado
                numero_serie='SN1234567891',
                descricao_problema='Problema com o GPS'
            )

        with self.assertRaises(Exception):
            Aparelho.objects.create(
                nome='Smartwatch',
                descricao='Smartwatch com GPS',
                marca='MarcaZ',
                modelo='ModeloA',
                imei='987654321098765',
                numero_serie='SN1234567890',  # Número de série duplicado
                descricao_problema='Problema com o GPS'
            )

    def test_string_representation(self):
        """Testa a representação em string do modelo Aparelho."""
        self.assertEqual(str(self.aparelho), 'MarcaX ModeloY - SN1234567890')

    def test_meta_options(self):
        """Testa se as opções de Meta estão funcionando corretamente."""
        meta = Aparelho._meta
        self.assertEqual(meta.verbose_name, 'Aparelho')
        self.assertEqual(meta.verbose_name_plural, 'Aparelhos')
        self.assertEqual(meta.ordering, ['marca', 'modelo'])


class AparelhoURLTest(TestCase):
    
    def test_create_url(self):
        path = reverse('aparelho:create_aparelho')
        self.assertEqual(resolve(path).view_name, 'aparelho:create_aparelho')
        self.assertEqual(resolve(path).func, aparelho_create_view)
    
    def test_list_url(self):
        path = reverse('aparelho:list_aparelho')
        self.assertEqual(resolve(path).view_name, 'aparelho:list_aparelho')
        self.assertEqual(resolve(path).func, aparelho_list_view)

    def test_update_url(self):
        aparelho = Aparelho.objects.create(
            nome='Tablet',
            descricao='Tablet com tela grande',
            marca='MarcaY',
            modelo='ModeloZ',
            imei='987654321098765',
            numero_serie='SN0987654321',
            descricao_problema='Problema com a bateria'
        )
        path = reverse('aparelho:update_aparelho', args=[aparelho.pk])
        self.assertEqual(resolve(path).view_name, 'aparelho:update_aparelho')
        self.assertEqual(resolve(path).func, aparelho_update_view)
    
    def test_delete_url(self):
        aparelho = Aparelho.objects.create(
            nome='Tablet',
            descricao='Tablet com tela grande',
            marca='MarcaY',
            modelo='ModeloZ',
            imei='987654321098765',
            numero_serie='SN0987654321',
            descricao_problema='Problema com a bateria'
        )
        path = reverse('aparelho:delete_aparelho', args=[aparelho.pk])
        self.assertEqual(resolve(path).view_name, 'aparelho:delete_aparelho')
        self.assertEqual(resolve(path).func, aparelho_delete_view)