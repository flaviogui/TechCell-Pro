from pydoc import resolve
from uuid import uuid4
from uuid import UUID
from django.test import TestCase # type: ignore
from django.urls import reverse # type: ignore
from .models import Reparo, Aparelho
from django.utils import timezone # type: ignore
from .forms import ConfirmarReparoForm
from appConfirmarReparo.views import reparo_detalhes, confirmar_reparo
from django.test import SimpleTestCase # type: ignore
from django.urls import reverse, resolve # type: ignore


class ReparoIntegrationTest(TestCase):
    def setUp(self):
        self.aparelho = Aparelho.objects.create(nome="Aparelho Teste", descricao="Descrição Teste")
        self.reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=100.00,
            data_inicio=timezone.now(),
            data_conclusao=timezone.now(),
            status='pendente',
            protocolo=uuid4(),
        )

    def test_confirmar_reparo_view(self):
        # Envia um POST request para confirmar o reparo
        response = self.client.post(reverse('appConfirmarReparo:confirmar_reparo', args=[self.reparo.pk]), {
            'status': 'concluido',
            'data_conclusao': timezone.now(),
        })
        self.assertEqual(response.status_code, 302)  # 302 é o código de redirecionamento
        self.assertRedirects(response, reverse('appConfirmarReparo:reparo_detalhes', args=[self.reparo.pk]))

    def test_view_reparo_status(self):
        # Supondo que 'reparo_detalhes' é uma página que exibe detalhes do reparo
        response = self.client.get(reverse('appConfirmarReparo:reparo_detalhes', args=[self.reparo.pk]))
        self.assertEqual(response.status_code, 200)
        # Verifica se os detalhes do reparo são exibidos corretamente
        self.assertContains(response, self.reparo.status)
        self.assertContains(response, self.reparo.data_inicio.strftime('%Y-%m-%d %H:%M:%S'))



class ConfirmarReparoFormTest(TestCase):

    def setUp(self):
        # Cria uma instância de Reparo para usar nos testes
        self.reparo = Reparo.objects.create(custo_estimado=100.0)

    def test_form_valid_data(self):
        # Testa o formulário com dados válidos
        form_data = {'custo_estimado': 150.0}
        form = ConfirmarReparoForm(data=form_data, instance=self.reparo)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        # Testa o formulário com dados inválidos (por exemplo, uma string em vez de um número)
        form_data = {'custo_estimado': 'invalid_value'}
        form = ConfirmarReparoForm(data=form_data, instance=self.reparo)
        self.assertFalse(form.is_valid())

    def test_form_empty_data(self):
        # Testa o formulário com dados vazios
        form = ConfirmarReparoForm(data={}, instance=self.reparo)
        self.assertFalse(form.is_valid())

    def test_form_save(self):
        # Testa se o formulário salva corretamente os dados
        form_data = {'custo_estimado': 200.0}
        form = ConfirmarReparoForm(data=form_data, instance=self.reparo)
        self.assertTrue(form.is_valid())
        saved_reparo = form.save()
        self.assertEqual(saved_reparo.custo_estimado, 200.0)


class UrlsTestCase(SimpleTestCase):
    def test_reparo_detalhes_url(self):
        # Testa a resolução da URL 'reparo_detalhes'
        url = reverse('appConfirmarReparo:reparo_detalhes', args=[1])
        self.assertEqual(url, '/reparo/1/')
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func, reparo_detalhes)

    def test_confirmar_reparo_url(self):
        # Testa a resolução da URL 'confirmar_reparo'
        url = reverse('appConfirmarReparo:confirmar_reparo', args=[1])
        self.assertEqual(url, '/confirmar_reparo/1/')
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func, confirmar_reparo)



class ReparoModelTest(TestCase):

    def setUp(self):
        # Criação de um objeto Aparelho para ser usado nos testes
        self.aparelho = Aparelho.objects.create(nome="Ar Condicionado", modelo="XYZ", serial="12345")

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
        self.assertTrue(isinstance(reparo.protocolo, UUID))

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
            status='concluido'
        )
        self.assertIsNone(reparo.data_conclusao)

