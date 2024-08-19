from django.test import TestCase, Client  # type: ignore
from django.urls import reverse, resolve  # type: ignore
from .models import Peca
from fornecedorApp.models import Fornecedor
import uuid
from pecaApp.views import peca_create_view, peca_list_view, peca_update_view, peca_delete_view
from pecaApp.forms import PecaForm


class PecaModelTest(TestCase):

    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor Teste')
        self.peca = Peca.objects.create(
            id=uuid.uuid4(),
            nome='Peca Teste',
            descricao='Descricao Teste',
            codigo='123456789',
            quantidade=10,
            preco_compra=100.0,
            fornecedor=self.fornecedor
        )

    def test_peca_creation(self):
        self.assertTrue(isinstance(self.peca, Peca))
        self.assertEqual(self.peca.__str__(), self.peca.nome)

    def test_peca_fields(self):
        self.assertEqual(self.peca.nome, 'Peca Teste')
        self.assertEqual(self.peca.descricao, 'Descricao Teste')
        self.assertEqual(self.peca.codigo, '123456789')
        self.assertEqual(self.peca.quantidade, 10)
        self.assertEqual(self.peca.preco_compra, 100.0)
        self.assertEqual(self.peca.fornecedor, self.fornecedor)


class PecaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor Teste')
        self.peca = Peca.objects.create(
            id=uuid.uuid4(),
            nome='Nova Peca',
            descricao='Descricao Teste',
            codigo='123456789',
            quantidade=10,
            preco_compra=100.0,
            fornecedor=self.fornecedor
        )

    def test_peca_create_view(self):
        response = self.client.post(reverse('peca:create_peca'), {
            'nome': 'Nova Peca',
            'descricao': 'Nova Descricao',
            'codigo': '987654321',
            'quantidade': 5,
            'preco_compra': 50.0,
            'fornecedor': self.fornecedor.id
        })
        # Adiciona esta linha para ver o conteúdo da resposta
        print(response.content)
        self.assertEqual(response.status_code, 302)
        # Verifica se uma nova peça foi criada
        self.assertEqual(Peca.objects.count(), 2)
        self.assertEqual(Peca.objects.last().nome, 'Nova Peca')

    def test_peca_list_view(self):
        response = self.client.get(reverse('peca:list_peca'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.peca.nome)

    def test_peca_update_view(self):
        response = self.client.post(reverse('peca:update_peca', args=[str(self.peca.id)]), {
            'nome': 'Peca Atualizada',
            'descricao': 'Descricao Atualizada',
            'codigo': '123456789',
            'quantidade': 15,
            'preco_compra': 150.0,
            'fornecedor': self.fornecedor.id
        })
        self.assertEqual(response.status_code, 302)
        self.peca.refresh_from_db()
        self.assertEqual(self.peca.nome, 'Peca Atualizada')

    def test_peca_delete_view(self):
        response = self.client.post(
            reverse('peca:delete_peca', args=[str(self.peca.id)]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Peca.objects.filter(id=self.peca.id).exists())


class TestUrls(TestCase):

    def test_create_url_resolves(self):
        url = reverse('peca:create_peca')
        self.assertEqual(resolve(url).func, peca_create_view)

    def test_list_url_resolves(self):
        url = reverse('peca:list_peca')
        self.assertEqual(resolve(url).func, peca_list_view)

    def test_update_url_resolves(self):
        url = reverse('peca:update_peca', args=['some-uuid'])
        self.assertEqual(resolve(url).func, peca_update_view)

    def test_delete_url_resolves(self):
        url = reverse('peca:delete_peca', args=['some-uuid'])
        self.assertEqual(resolve(url).func, peca_delete_view)


class PecaFormTest(TestCase):

    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor Teste')

    def test_peca_form_valid(self):
        form_data = {
            'nome': 'Peca Teste',
            'descricao': 'Descricao Teste',
            'codigo': '123456789',
            'quantidade': 10,
            'preco_compra': 100.0,
            'fornecedor': self.fornecedor.id
        }
        form = PecaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_peca_form_invalid(self):
        form_data = {
            'nome': '',
            'descricao': 'Descricao Teste',
            'codigo': '123456789',
            'quantidade': 10,
            'preco_compra': 100.0,
            'fornecedor': self.fornecedor.id
        }
        form = PecaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
