from django.test import TestCase, Client  # type: ignore
from django.urls import reverse, resolve  # type: ignore
from funcionarioApp.models import Funcionario
from django.test import SimpleTestCase  # type: ignore
from funcionarioApp.forms import FuncionarioForm
from funcionarioApp.views import (
    funcionario_create_view,
    funcionario_list_view,
    funcionario_update_view,
    funcionario_delete_view
)


class FuncionarioViewsTest(TestCase):

    def setUp(self):
        self.funcionario = Funcionario.objects.create(
            nome='Teste Funcionario',
            email='teste@funcionario.com',
            telefone='123456789',
            cpf='12345678901',
            cargo='Gerente'

        )

        self.client = Client()
        self.create_url = reverse('funcionario:create_funcionario')
        self.list_url = reverse('funcionario:list_funcionario')
        self.update_url = lambda pk: reverse(
            'funcionario:update_funcionario', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse(
            'funcionario:delete_funcionario', kwargs={'pk': pk})

    def test_retorno_funcionario(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'funcionario_form.html')
        self.assertIsInstance(response.context['form'], FuncionarioForm)

    def test_listar_funcionario(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'funcionario_list.html')
        self.assertContains(response, self.funcionario.nome)

    def test_editar_funcionario(self):
        response = self.client.get(self.update_url(self.funcionario.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'funcionario_update.html')
        self.assertIsInstance(response.context['form'], FuncionarioForm)
        self.assertEqual(response.context['form'].instance, self.funcionario)

    def test_deletar_funcionario(self):
        response = self.client.post(self.delete_url(self.funcionario.pk))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Funcionario.objects.filter(pk=self.funcionario.pk).exists())


class TestUrls(SimpleTestCase):

    def test_create_url_resolves(self):
        url = reverse('funcionario:create_funcionario')
        self.assertEqual(resolve(url).func, funcionario_create_view)

    def test_list_url_resolves(self):
        url = reverse('funcionario:list_funcionario')
        self.assertEqual(resolve(url).func, funcionario_list_view)

    def test_update_url_resolves(self):
        url = reverse('funcionario:update_funcionario', args=['1'])
        self.assertEqual(resolve(url).func, funcionario_update_view)

    def test_delete_url_resolves(self):
        url = reverse('funcionario:delete_funcionario', args=['1'])
        self.assertEqual(resolve(url).func, funcionario_delete_view)