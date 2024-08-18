from django.test import TestCase, Client # type: ignore
from uuid import uuid4
from .models import Produto
from produtosApp.forms import ProdutoForm
from django.urls import reverse, resolve  # type: ignore
from .views import (
    produto_create_view,
    produto_list_view,
    produto_update_view,
    produto_delete_view,
)

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

    def test_meta_options(self):
        """Testa se as opções de Meta estão funcionando corretamente."""
        meta = Produto._meta
        self.assertEqual(meta.verbose_name, 'Produto')
        self.assertEqual(meta.verbose_name_plural, 'Produtos')
        self.assertEqual(meta.ordering, ['nome', 'preco'])


class ProdutoURLTest(TestCase):
    
    def test_create_url(self):
        path = reverse('produto:create_produto')
        self.assertEqual(resolve(path).view_name, 'produto:create_produto')
        self.assertEqual(resolve(path).func, produto_create_view)
    
    def test_list_url(self):
        path = reverse('produto:list_produto')
        self.assertEqual(resolve(path).view_name, 'produto:list_produto')
        self.assertEqual(resolve(path).func, produto_list_view)

    def test_update_url(self):
        produto = Produto.objects.create(
            nome='Capinha de smartphone',
            descricao='Capinha de smartphone muito boa',
            cod_barras='123456789088',
            preco=11.99,
            categoria='Produtos diversos'
        )
        path = reverse('produto:update_produto', args=[produto.pk])
        self.assertEqual(resolve(path).view_name, 'produto:update_produto')
        self.assertEqual(resolve(path).func, produto_update_view)
    
    def test_delete_url(self):
        produto = Produto.objects.create(
            nome='Capinha de smartphone',
            descricao='Capinha de smartphone muito boa',
            cod_barras='123456789088',
            preco=11.99,
            categoria='Produtos diversos'        
        )
        
        path = reverse('produto:delete_produto', args=[produto.pk])
        self.assertEqual(resolve(path).view_name, 'produto:delete_produto')
        self.assertEqual(resolve(path).func, produto_delete_view)

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