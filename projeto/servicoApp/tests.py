from django.test import TestCase  # type: ignore # type: ignore
from django.urls import reverse, resolve  # type: ignore
from django.contrib.messages import get_messages  # type: ignore
from servicoApp.models import Servico
from servicoApp.forms import ServicoForm
import uuid
from servicoApp.views import (
    servico_create_view,
    servico_list_view,
    servico_update_view,
    servico_delete_view
)


class ServicoModelTest(TestCase):

    def setUp(self):
        self.servico = Servico.objects.create(
            nome="Troca de Tela",
            descricao="Substituição completa da tela do aparelho.",
            preco=250,
            duracao="2h",
            tipo="troca_tela"
        )

    def test_servico_creation(self):
        self.assertIsInstance(self.servico, Servico)
        self.assertEqual(self.servico.nome, "Troca de Tela")
        self.assertEqual(self.servico.descricao,
                         "Substituição completa da tela do aparelho.")
        self.assertEqual(self.servico.preco, 250)
        self.assertEqual(self.servico.duracao, "2h")
        self.assertEqual(self.servico.tipo, "troca_tela")

    def test_str_representation(self):
        self.assertEqual(str(self.servico), "Troca de Tela")

    def test_default_id(self):
        self.assertIsInstance(self.servico.id, uuid.UUID)

    def test_tipo_default_value(self):
        servico_sem_tipo = Servico.objects.create(
            nome="Formatação",
            descricao="Formatação completa do sistema.",
            preco=150,
            duracao="1h"
        )
        self.assertEqual(servico_sem_tipo.tipo, "-")

    def test_ordering(self):
        servico2 = Servico.objects.create(
            nome="Atualização de Sistema",
            descricao="Atualização para a versão mais recente do sistema.",
            preco=100,
            duracao="1h",
            tipo="atualizacao_sistema"
        )
        servico3 = Servico.objects.create(
            nome="Limpeza",
            descricao="Limpeza completa do aparelho.",
            preco=50,
            duracao="30min",
            tipo="limpeza"
        )
        servicos = Servico.objects.all()
        self.assertEqual(servicos[0].nome, "Atualização de Sistema")
        self.assertEqual(servicos[1].nome, "Limpeza")
        self.assertEqual(servicos[2].nome, "Troca de Tela")


class ServicoViewsTest(TestCase):

    def setUp(self):
        self.servico = Servico.objects.create(
            nome="Troca de Tela",
            descricao="Substituição completa da tela do aparelho.",
            preco=250,
            duracao="2h",
            tipo="troca_tela"
        )

    def test_servico_create_view_get(self):
        response = self.client.get(reverse('servico:create_servico'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'servico_form.html')
        self.assertIsInstance(response.context['form'], ServicoForm)

    def test_servico_create_view_post(self):
        data = {
            'nome': 'Formatação',
            'descricao': 'Formatação completa do sistema.',
            'preco': 150,
            'duracao': '1h',
            'tipo': 'formatação_backup'
        }
        response = self.client.post(reverse('servico:create_servico'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('servico:list_servico'))
        self.assertEqual(Servico.objects.count(), 2)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Serviço Criado com Sucesso!')

    def test_servico_list_view(self):
        response = self.client.get(reverse('servico:list_servico'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'servico_list.html')
        self.assertIn(self.servico, response.context['servicos'])

    def test_servico_update_view_get(self):
        response = self.client.get(
            reverse('servico:update_servico', args=[self.servico.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'servico_update.html')
        self.assertIsInstance(response.context['form'], ServicoForm)

    def test_servico_update_view_post(self):
        data = {
            'nome': 'Troca de Tela (Atualizado)',
            'descricao': 'Substituição completa da tela do aparelho (Atualizado).',
            'preco': 300,
            'duracao': '3h',
            'tipo': 'troca_tela'
        }
        response = self.client.post(
            reverse('servico:update_servico', args=[self.servico.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('servico:list_servico'))
        self.servico.refresh_from_db()
        self.assertEqual(self.servico.nome, 'Troca de Tela (Atualizado)')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Serviço Alterado com Sucesso!')

    def test_servico_delete_view(self):
        response = self.client.post(
            reverse('servico:delete_servico', args=[self.servico.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('servico:list_servico'))
        self.assertEqual(Servico.objects.count(), 0)


class ServicoFormTest(TestCase):

    def test_servico_form_valid(self):
        data = {
            'nome': 'Reparo de Hardware',
            'descricao': 'Reparo de componentes internos do aparelho.',
            'preco': 350,
            'duracao': '3h',
            'tipo': 'reparo'
        }
        form = ServicoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_servico_form_invalid(self):
        data = {
            'nome': '',
            'descricao': 'Reparo de componentes internos do aparelho.',
            'preco': 350,
            'duracao': '3h',
            'tipo': 'reparo'
        }
        form = ServicoForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_servico_form_fields(self):
        form = ServicoForm()
        expected_fields = ['nome', 'descricao', 'preco', 'duracao', 'tipo']
        self.assertEqual(list(form.fields), expected_fields)

    def test_servico_form_field_max_length(self):
        data = {
            'nome': 'A' * 101,
            'descricao': 'Reparo de componentes internos do aparelho.',
            'preco': 350,
            'duracao': '3h',
            'tipo': 'reparo'
        }
        form = ServicoForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)


class ServicoUrlsTest(TestCase):

    def test_create_servico_url(self):
        url = reverse('servico:create_servico')
        self.assertEqual(resolve(url).func, servico_create_view)

    def test_list_servico_url(self):
        url = reverse('servico:list_servico')
        self.assertEqual(resolve(url).func, servico_list_view)

    def test_update_servico_url(self):
        url = reverse('servico:update_servico', args=['some-uuid'])
        self.assertEqual(resolve(url).func, servico_update_view)

    def test_delete_servico_url(self):
        url = reverse('servico:delete_servico', args=['some-uuid'])
        self.assertEqual(resolve(url).func, servico_delete_view)
