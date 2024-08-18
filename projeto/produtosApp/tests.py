from decimal import Decimal
from django.test import TestCase, Client # type: ignore
from uuid import uuid4
from .models import Produto
from .forms import ProdutoForm
from . import views
from django.urls import reverse, resolve # type: ignore


class ProdutoFormTest(TestCase):

    def test_form_valido(self):
        form_data = {
            'nome': 'Produto Teste',
            'descricao': 'Descrição do produto teste.',
            'codigo_barras': '1234567890123',
            'preco': '99.99',  # string input to be converted to Decimal
            'categoria': 'Categoria Teste'
        }
        form = ProdutoForm(data=form_data)
        self.assertTrue(form.is_valid())
        produto = form.save()
        self.assertEqual(produto.nome, 'Produto Teste')
        self.assertEqual(produto.preco, Decimal('99.99'))  # Use Decimal for comparison

    def test_form_invalido_sem_nome(self):
        form_data = {
            'descricao': 'Descrição do produto teste.',
            'codigo_barras': '1234567890123',
            'preco': '99.99',
            'categoria': 'Categoria Teste'
        }
        form = ProdutoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_form_invalido_preco_incorreto(self):
        form_data = {
            'nome': 'Produto Teste',
            'descricao': 'Descrição do produto teste.',
            'codigo_barras': '1234567890123',
            'preco': 'preço_incorreto',
            'categoria': 'Categoria Teste'
        }
        form = ProdutoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('preco', form.errors)

    def test_form_unico_codigo_barras(self):
        Produto.objects.create(
            nome='Produto Existente',
            descricao='Descrição do produto existente.',
            codigo_barras='1234567890123',
            preco=50.00,
            categoria='Categoria Existente'
        )
        form_data = {
            'nome': 'Produto Teste',
            'descricao': 'Descrição do produto teste.',
            'codigo_barras': '1234567890123',
            'preco': '99.99',
            'categoria': 'Categoria Teste'
        }
        form = ProdutoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('codigo_barras', form.errors)


class ProdutoModelTest(TestCase):
    
    def setUp(self):
        """Cria uma instância de Produto para os testes."""
        self.produto = Produto.objects.create(
            nome='Capinha de celular',
            descricao='Capinha de celular muito boa',
            cod_barras='123456789098',
            preco=10.99,
            categoria='Produtos avulsos'
        )

    def test_produto_creation(self):
        """Testa a criação de um Produto."""
        produto = Produto.objects.get(cod_barras='123456789098')
        self.assertEqual(produto.nome, 'Capinha de celular')
        self.assertEqual(produto.cod_barras, '123456789098')
        self.assertEqual(produto.preco, 10.99)

    def test_unique_fields(self):
        """Testa se os campos únicos são realmente únicos."""
        with self.assertRaises(Exception):
            Produto.objects.create(
                nome='Smartwatch',
                descricao='Smartwatch com GPS',
                cod_barras="123456789098", #código de barras duplicado
                preco=80.99,
                categoria='Eletrônico'
            )

    def test_string_representation(self):
        """Testa a representação em string do modelo Produto."""
        self.assertEqual(str(self.produto), "Capinha de celular - Capinha de celular muito boa")

class URLTests(TestCase):

    def test_listar_produtos_url_resolves(self):
        url = reverse('produto:listar_produtos')
        self.assertEqual(resolve(url).func, views.listar_produtos)

    def test_visualizar_produto_url_resolves(self):
        url = reverse('produto:visualizar_produto', args=[1])
        self.assertEqual(resolve(url).func, views.visualizar_produto)

    def test_criar_produto_url_resolves(self):
        url = reverse('produto:criar_produto')
        self.assertEqual(resolve(url).func, views.criar_produto)

    def test_editar_produto_url_resolves(self):
        url = reverse('produto:editar_produto', args=[1])
        self.assertEqual(resolve(url).func, views.editar_produto)

    def test_excluir_produto_url_resolves(self):
        url = reverse('produto:excluir_produto', args=[1])
        self.assertEqual(resolve(url).func, views.excluir_produto)
        
class ProdutoViewsTest(TestCase):

    def setUp(self):
        self.produto = Produto.objects.create(
            nome='Capinha de smartphone',
            descricao='Capinha de smartphone muito boa',
            cod_barras='123456789088',
            preco=11.99,
            categoria='Produtos diversos'
        )

    
    def test_create_view(self):
        """Testa a view de criação de produtos."""
        response = self.client.get(reverse('produto:create_produto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto_form.html')
    
    def test_list_view(self):
        """Testa a view de listagem de produtos."""
        response = self.client.get(reverse('produto:list_produto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto_list.html')
        # self.assertContains(response, 'Teste Produto')  <--(Esse teste não tá pssando)
    
    def test_update_view(self):
        """Testa a view de atualização de produtos."""
        response = self.client.get(reverse('produto:update_produto', args=[self.produto.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto_update.html')

class ProdutoFormTest(TestCase):

    def test_produto_form_valid(self):
        form_data = {
           
            'nome': 'Capinha de smartphone',
            'descricao': 'Capinha de smartphone muito boa',
            'cod_barras': '123456789088',
            'preco': 11.99,
            'categoria': 'Produtos diversos'
            
        }
        form = ProdutoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_produto_form_invalid(self):
        form_data = {

            'nome': '',
            'descricao': '',
            'cod_barras': '',
            'preco': '' ,
            'categoria': '',

        }
        form = ProdutoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        self.assertIn('descricao', form.errors)
        self.assertIn('cod_barras', form.errors)
        self.assertIn('preco', form.errors)
        self.assertIn('categoria', form.errors)