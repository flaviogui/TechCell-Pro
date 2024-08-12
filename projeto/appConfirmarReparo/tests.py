from django.test import TestCase, SimpleTestCase # type: ignore
from django.urls import reverse, resolve # type: ignore
from django.utils import timezone # type: ignore
from uuid import uuid4
from appConfirmarReparo.models import Reparo, Aparelho
from appConfirmarReparo.forms import ConfirmarReparoForm
from appConfirmarReparo.views import reparo_detalhes, confirmar_reparo

class ReparoIntegrationTest(TestCase):
    def setUp(self):
        self.aparelho = Aparelho.objects.create(
            nome="Aparelho Teste", descricao="Descrição Teste"
        )
        self.reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=100.00,
            data_inicio=timezone.now(),
            data_conclusao=None,
            status='pendente',
            protocolo=uuid4(),
        )

    def test_confirmar_reparo_view(self):
        response = self.client.get(reverse('appConfirmarReparo:confirmar_reparo', args=[self.reparo.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_reparo_status(self):
        response = self.client.get(reverse('appConfirmarReparo:reparo_detalhes', args=[self.reparo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pendente')

class ConfirmarReparoFormTest(TestCase):
    def setUp(self):
        self.aparelho = Aparelho.objects.create(
            nome="Aparelho Teste", descricao="Descrição Teste"
        )
        self.reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=100.0,
            status='pendente',
            data_inicio=timezone.now()
        )

    def test_form_valid_data(self):
        form_data = {
            'custo_estimado': 150.0,
            'aparelho': self.aparelho.id,
            'status': 'pendente',
            'data_inicio': timezone.now().strftime('%Y-%m-%dT%H:%M'),  # Formato compatível com o formulário
            'data_conclusao': '',  # Pode ser opcional
            'cliente_notificado': False  # Valor padrão
        }
        form = ConfirmarReparoForm(data=form_data, instance=self.reparo)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        form_data = {
            'custo_estimado': 'invalid_value',
            'aparelho': self.aparelho.id,
            'status': 'pendente',
            'data_inicio': timezone.now().strftime('%Y-%m-%dT%H:%M'),  # Formato compatível com o formulário
            'data_conclusao': '',  # Pode ser opcional
            'cliente_notificado': False  # Valor padrão
        }
        form = ConfirmarReparoForm(data=form_data, instance=self.reparo)
        self.assertFalse(form.is_valid())
        self.assertIn('custo_estimado', form.errors)

    def test_form_empty_data(self):
        form = ConfirmarReparoForm(data={}, instance=self.reparo)
        self.assertFalse(form.is_valid())
        self.assertIn('custo_estimado', form.errors)
        self.assertIn('status', form.errors)
        self.assertIn('data_inicio', form.errors)
        self.assertIn('aparelho', form.errors)

    def test_form_save(self):
        form_data = {
            'custo_estimado': 200.0,
            'aparelho': self.aparelho.id,
            'status': 'pendente',
            'data_inicio': timezone.now().strftime('%Y-%m-%dT%H:%M'),  # Formato compatível com o formulário
            'data_conclusao': '',  # Pode ser opcional
            'cliente_notificado': False  # Valor padrão
        }
        form = ConfirmarReparoForm(data=form_data, instance=self.reparo)
        self.assertTrue(form.is_valid(), form.errors)
        saved_reparo = form.save()
        self.assertEqual(saved_reparo.custo_estimado, 200.0)


class UrlsTestCase(SimpleTestCase): # type: ignore
    def test_reparo_detalhes_url(self):
        url = reverse('appConfirmarReparo:reparo_detalhes', args=[1])
        self.assertEqual(url, '/appConfirmarReparo/reparo/1/')
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func, reparo_detalhes)

    def test_confirmar_reparo_url(self):
        url = reverse('appConfirmarReparo:confirmar_reparo', args=[1])
        self.assertEqual(url, '/appConfirmarReparo/confirmar_reparo/1/')
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func, confirmar_reparo)

class ReparoModelTest(TestCase):
    def setUp(self):
        self.aparelho = Aparelho.objects.create(
            nome="Ar Condicionado", descricao="Modelo XYZ"
        )

    def test_criacao_reparo(self):
        reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=150.00,
            data_inicio=timezone.now(),
            status='pendente'
        )
        self.assertIsInstance(reparo, Reparo)
        self.assertEqual(reparo.custo_estimado, 150.00)
        self.assertEqual(reparo.status, 'pendente')
        self.assertTrue(isinstance(reparo.protocolo, uuid4().__class__))

    def test_metodo_str(self):
        reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=200.00,
            data_inicio=timezone.now(),
            status='em_progresso'
        )
        self.assertEqual(str(reparo), f'Reparo {reparo.protocolo} - {self.aparelho.nome}')

    def test_cliente_notificado_default(self):
        reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=300.00,
            data_inicio=timezone.now(),
            status='pendente'
        )
        self.assertFalse(reparo.cliente_notificado)

    def test_data_conclusao_pode_ser_nula(self):
        reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=350.00,
            data_inicio=timezone.now(),
            status='pendente',
            data_conclusao=None
        )
        self.assertIsNone(reparo.data_conclusao)