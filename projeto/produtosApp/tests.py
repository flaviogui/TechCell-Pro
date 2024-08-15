from decimal import Decimal
from django.test import SimpleTestCase # type: ignore
from django.urls import reverse, resolve # type: ignore
from .views import listar_produtos, visualizar_produto, criar_produto, editar_produto, excluir_produto
from django.test import TestCase # type: ignore
from django.db import IntegrityError # type: ignore
from .models import Produto
from .forms import ProdutoForm


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
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            descricao='Descrição do produto teste.',
            codigo_barras='1234567890123',
            preco=99.99,
            categoria='Categoria Teste'
        )

    def test_str_metodo(self):
        """
        Testa o método __str__ do modelo Produto.
        """
        self.assertEqual(str(self.produto), 'Produto Teste')

    def test_codigo_barras_unico(self):
        """
        Testa a unicidade do campo 'codigo_barras'.
        """
        # Tenta criar um novo produto com o mesmo código de barras
        with self.assertRaises(IntegrityError):
            Produto.objects.create(
                nome='Produto Duplicado',
                descricao='Descrição de produto duplicado.',
                codigo_barras='1234567890123',  # Código duplicado
                preco=29.99,
                categoria='Categoria Duplicada'
            )


class TestUrls(SimpleTestCase):

    def test_listar_produtos_url_resolve(self):
        url = reverse('listar_produtos')
        self.assertEqual(resolve(url).func, listar_produtos)

    def test_visualizar_produto_url_resolve(self):
        url = reverse('visualizar_produto', args=[1])
        self.assertEqual(resolve(url).func, visualizar_produto)

    def test_criar_produto_url_resolve(self):
        url = reverse('criar_produto')
        self.assertEqual(resolve(url).func, criar_produto)

    def test_editar_produto_url_resolve(self):
        url = reverse('editar_produto', args=[1])
        self.assertEqual(resolve(url).func, editar_produto)

    def test_excluir_produto_url_resolve(self):
        url = reverse('excluir_produto', args=[1])
        self.assertEqual(resolve(url).func, excluir_produto)



class ProdutoViewsTest(TestCase):

    def setUp(self):
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            descricao='Descrição do produto teste.',
            codigo_barras='1234567890123',
            preco=99.99,
            categoria='Categoria Teste'
        )

    def test_listar_produtos(self):
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_produtos.html')
        self.assertContains(response, 'Produto Teste')

    def test_visualizar_produto(self):
        response = self.client.get(reverse('visualizar_produto', args=[self.produto.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'visualizar_produto.html')
        self.assertContains(response, 'Produto Teste')

    def test_criar_produto(self):
        response = self.client.post(reverse('criar_produto'), {
            'nome': 'Novo Produto',
            'descricao': 'Descrição do novo produto.',
            'codigo_barras': '9876543210987',
            'preco': '59.99',
            'categoria': 'Nova Categoria'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_produtos'))
        novo_produto = Produto.objects.get(codigo_barras='9876543210987')
        self.assertEqual(novo_produto.nome, 'Novo Produto')

    def test_editar_produto(self):
        response = self.client.post(reverse('editar_produto', args=[self.produto.pk]), {
            'nome': 'Produto Editado',
            'descricao': 'Descrição do produto editado.',
            'codigo_barras': '1234567890123',
            'preco': '79.99',
            'categoria': 'Categoria Editada'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_produtos'))
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Produto Editado')

    def test_excluir_produto(self):
        response = self.client.post(reverse('excluir_produto', args=[self.produto.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_produtos'))
        self.assertFalse(Produto.objects.filter(pk=self.produto.pk).exists())
