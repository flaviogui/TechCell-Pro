from django.test import TestCase, Client  # type: ignore # type: ignore
from django.urls import reverse  # type: ignore
from clienteApp.models import Cliente
from clienteApp.forms import ClienteForm
from django.test import SimpleTestCase  # type: ignore
from django.urls import reverse, resolve  # type: ignore
from clienteApp.views import cliente_create_view, cliente_list_view, cliente_update_view, cliente_delete_view
from django.test import TestCase  # type: ignore
from clienteApp.models import Cliente
from django.test import TestCase  # type: ignore
from clienteApp.forms import ClienteForm


class ClienteViewsTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Teste Cliente',
            email='teste@cliente.com',
            telefone='123456789',
            cpf='12345678901'
        )

        self.client = Client()
        self.create_url = reverse('cliente:create_cliente')
        self.list_url = reverse('cliente:list_cliente')
        self.update_url = lambda pk: reverse(
            'cliente:update_cliente', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse(
            'cliente:delete_cliente', kwargs={'pk': pk})

    def test_retorno_cliente(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliente_form.html')
        self.assertIsInstance(response.context['form'], ClienteForm)

    def test_listar_cliente(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliente_list.html')
        self.assertContains(response, self.cliente.nome)

    def test_editar_cliente(self):
        response = self.client.get(self.update_url(self.cliente.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliente_update.html')
        self.assertIsInstance(response.context['form'], ClienteForm)
        self.assertEqual(response.context['form'].instance, self.cliente)

    def test_deletar_cliente(self):
        response = self.client.post(self.delete_url(self.cliente.pk))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Cliente.objects.filter(pk=self.cliente.pk).exists())


class TestUrls(SimpleTestCase):

    def test_create_url_resolves(self):
        url = reverse('cliente:create_cliente')
        self.assertEqual(resolve(url).func, cliente_create_view)

    def test_list_url_resolves(self):
        url = reverse('cliente:list_cliente')
        self.assertEqual(resolve(url).func, cliente_list_view)

    def test_update_url_resolves(self):
        # Substitua '1' pelo ID válido de um cliente existente se necessário
        url = reverse('cliente:update_cliente', args=['1'])
        self.assertEqual(resolve(url).func, cliente_update_view)

    def test_delete_url_resolves(self):
        # Substitua '1' pelo ID válido de um cliente existente se necessário
        url = reverse('cliente:delete_cliente', args=['1'])
        self.assertEqual(resolve(url).func, cliente_delete_view)


class ClienteModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Teste Cliente',
            email='teste@cliente.com',
            telefone='123456789',
            cpf='12345678901'
        )

    def test_cliente_str_method(self):
        self.assertEqual(str(self.cliente), 'Teste Cliente')

    def test_cliente_instance(self):
        self.assertIsInstance(self.cliente, Cliente)

    def test_cliente_creation(self):
        cliente_count = Cliente.objects.count()
        self.assertEqual(cliente_count, 1)


class ClienteFormTest(TestCase):

    def test_cliente_form_valid(self):
        form_data = {
            'nome': 'Novo Cliente',
            'email': 'novo@cliente.com',
            'telefone': '987654321',
            'cpf': '12345678909',  # CPF válido de exemplo
        }
        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_cliente_form_invalid(self):
        form_data = {
            'nome': 'Novo Cliente',
            'email': 'email_invalido',  # Email inválido para testar validação
            'telefone': '987654321',
            'cpf': '12345678901',  # CPF inválido para testar validação
        }
        form = ClienteForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Verifica se há exatamente 1 erro de validação
        self.assertEqual(len(form.errors), 2)
        # Verifica se o campo 'cpf' está presente nos erros
        self.assertIn('cpf', form.errors.keys())
        # Verifica a mensagem de erro esperada
        self.assertEqual(form.errors['cpf'][0], 'Número de CPF inválido')
