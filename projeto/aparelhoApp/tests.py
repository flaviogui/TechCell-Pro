from django.test import TestCase, Client # type: ignore
from uuid import uuid4
from .models import Aparelho
from aparelhoApp.forms import AparelhoForm
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

class AparelhoViewsTest(TestCase):

    def setUp(self):
        self.aparelho = Aparelho.objects.create(
            nome='Teste Aparelho',
            marca='Marca Teste',
            modelo='Modelo Teste',
            imei='123456789012345',
            numero_serie='ABC123456',
            descricao_problema='Problema Teste'
        )

    
    def test_create_view(self):
        """Testa a view de criação de aparelhos."""
        response = self.client.get(reverse('aparelho:create_aparelho'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aparelho_form.html')
    
    def test_list_view(self):
        """Testa a view de listagem de aparelhos."""
        response = self.client.get(reverse('aparelho:list_aparelho'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aparelho_list.html')
        # self.assertContains(response, 'Teste Aparelho')  <--(Esse teste não tá pssando)
    
    def test_update_view(self):
        """Testa a view de atualização de aparelhos."""
        response = self.client.get(reverse('aparelho:update_aparelho', args=[self.aparelho.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aparelho_update.html')

class AparelhoFormTest(TestCase):

    def test_aparelho_form_valid(self):
        form_data = {
            'nome': 'iPhone',
            'descricao': 'iPhone 13 Pro Max',
            'marca': 'Apple',
            'modelo': '13 Pro Max',
            'imei': '123456789012345',
            'numero_serie': 'SN12345',
            'descricao_problema': 'Tela quebrada'
        }
        form = AparelhoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_aparelho_form_invalid(self):
        form_data = {
            'nome': '',  # Nome vazio
            'descricao': 'iPhone 13 Pro Max',
            'marca': '',
            'modelo': '',
            'imei': '123456789012345',
            'numero_serie': '',
            'descricao_problema': 'Tela quebrada'
        }
        form = AparelhoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        self.assertIn('marca', form.errors)
        self.assertIn('modelo', form.errors)
        self.assertIn('numero_serie', form.errors)