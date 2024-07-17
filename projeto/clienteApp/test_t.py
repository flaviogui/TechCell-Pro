from django.test import TestCase, Client  # type: ignore # type: ignore
from django.urls import reverse  # type: ignore
from clienteApp.models import Cliente
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
