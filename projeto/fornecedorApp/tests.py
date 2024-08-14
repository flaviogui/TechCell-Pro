from django.test import TestCase, Client  # type: ignore
from .forms import FornecedorForm
from django.urls import reverse  # type: ignore
from django.test import TestCase  # type: ignore
from .models import Fornecedor
import uuid


class FornecedorModelTest(TestCase):

    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste",
            email="fornecedor@teste.com",
            telefone="123456789",
            cnpj="12.345.678/0001-99",
            rua="Rua Teste",
            numero="123",
            bairro="Bairro Teste",
            cidade="Cidade Teste",
            estado="TE",
            cep="12345-678"
        )

    def test_fornecedor_creation(self):
        self.assertTrue(isinstance(self.fornecedor, Fornecedor))
        self.assertEqual(self.fornecedor.__str__(), self.fornecedor.nome)

    def test_fornecedor_fields(self):
        self.assertEqual(self.fornecedor.nome, "Fornecedor Teste")
        self.assertEqual(self.fornecedor.email, "fornecedor@teste.com")
        self.assertEqual(self.fornecedor.telefone, "123456789")
        self.assertEqual(self.fornecedor.cnpj, "12.345.678/0001-99")
        self.assertEqual(self.fornecedor.rua, "Rua Teste")
        self.assertEqual(self.fornecedor.numero, "123")
        self.assertEqual(self.fornecedor.bairro, "Bairro Teste")
        self.assertEqual(self.fornecedor.cidade, "Cidade Teste")
        self.assertEqual(self.fornecedor.estado, "TE")
        self.assertEqual(self.fornecedor.cep, "12345-678")

    def test_fornecedor_uuid(self):
        self.assertTrue(isinstance(self.fornecedor.id, uuid.UUID))


class FornecedorViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste",
            email="fornecedor@teste.com",
            telefone="123456789",
            cnpj="12.345.678/0001-99",
            rua="Rua Teste",
            numero="123",
            bairro="Bairro Teste",
            cidade="Cidade Teste",
            estado="TE",
            cep="12345-678"
        )

    def test_fornecedor_create_view_get(self):
        response = self.client.get(reverse('fornecedor:create_fornecedor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fornecedor_form.html')
        self.assertIsInstance(response.context['form'], FornecedorForm)

    def test_fornecedor_create_view_post(self):
        data = {
            'nome': "Novo Fornecedor",
            'email': "novo@fornecedor.com",
            'telefone': "987654321",
            'cnpj': "98.765.432/0001-99",
            'rua': "Nova Rua",
            'numero': "456",
            'bairro': "Novo Bairro",
            'cidade': "Nova Cidade",
            'estado': "NC",
            'cep': "98765-432"
        }
        response = self.client.post(
            reverse('fornecedor:create_fornecedor'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('fornecedor:list_fornecedor'))
        self.assertTrue(Fornecedor.objects.filter(
            nome="Novo Fornecedor").exists())

    def test_fornecedor_list_view(self):
        response = self.client.get(reverse('fornecedor:list_fornecedor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fornecedor_list.html')
        self.assertIn(self.fornecedor, response.context['fornecedores'])

    def test_fornecedor_update_view_get(self):
        response = self.client.get(
            reverse('fornecedor:update_fornecedor', args=[self.fornecedor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fornecedor_update.html')
        self.assertIsInstance(response.context['form'], FornecedorForm)

    def test_fornecedor_update_view_post(self):
        data = {
            'nome': "Fornecedor Atualizado",
            'email': "atualizado@fornecedor.com",
            'telefone': "123456789",
            'cnpj': "12.345.678/0001-99",
            'rua': "Rua Atualizada",
            'numero': "123",
            'bairro': "Bairro Atualizado",
            'cidade': "Cidade Atualizada",
            'estado': "TE",
            'cep': "12345-678"
        }
        response = self.client.post(
            reverse('fornecedor:update_fornecedor', args=[self.fornecedor.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('fornecedor:list_fornecedor'))
        self.fornecedor.refresh_from_db()
        self.assertEqual(self.fornecedor.nome, "Fornecedor Atualizado")

    def test_fornecedor_delete_view(self):
        response = self.client.post(
            reverse('fornecedor:delete_fornecedor', args=[self.fornecedor.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('fornecedor:list_fornecedor'))
        self.assertFalse(Fornecedor.objects.filter(
            pk=self.fornecedor.pk).exists())
