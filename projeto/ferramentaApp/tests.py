# Create your tests here.
from django.test import TestCase, Client # type: ignore
from django.urls import reverse # type: ignore
from ferramentaApp.models import Ferramenta
from ferramentaApp.forms import FerramentaForm
from django.urls import reverse, resolve  # type: ignore
from django.test import SimpleTestCase  # type: ignore
from ferramentaApp.views import (
    ferramenta_create_view, 
    ferramenta_list_view, 
    ferramenta_update_view, 
    ferramenta_delete_view
)
from django.test import TestCase  # type: ignore
import uuid
from django.test import TestCase  # type: ignore



class FerramentaViewsTest(TestCase):

    def setUp(self):
        self.ferramenta = Ferramenta.objects.create(
            nome='Chave de Fenda',
            descricao='Chave de fenda de alta qualidade.',
            codigo='CF001',
            quantidade_disponivel=10,
            condicao='novo'
        )

        self.client = Client()
        self.create_url = reverse('ferramenta:create_ferramenta')
        self.list_url = reverse('ferramenta:list_ferramenta')
        self.update_url = lambda pk: reverse(
            'ferramenta:update_ferramenta', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse(
            'ferramenta:delete_ferramenta', kwargs={'pk': pk})

    def test_retorno_ferramenta(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ferramenta_form.html')
        self.assertIsInstance(response.context['form'], FerramentaForm)

    def test_listar_ferramenta(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ferramenta_list.html')
        self.assertContains(response, self.ferramenta.nome)

    def test_editar_ferramenta(self):
        response = self.client.get(self.update_url(self.ferramenta.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ferramenta_update.html')
        self.assertIsInstance(response.context['form'], FerramentaForm)
        self.assertEqual(response.context['form'].instance, self.ferramenta)

    def test_deletar_ferramenta(self):
        response = self.client.post(self.delete_url(self.ferramenta.pk))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Ferramenta.objects.filter(pk=self.ferramenta.pk).exists())

class FerramentaUrlsTest(SimpleTestCase):

    def test_create_url_resolves(self):
        url = reverse('ferramenta:create_ferramenta')
        self.assertEqual(resolve(url).func, ferramenta_create_view)

    def test_list_url_resolves(self):
        url = reverse('ferramenta:list_ferramenta')
        self.assertEqual(resolve(url).func, ferramenta_list_view)

    def test_update_url_resolves(self):
        url = reverse('ferramenta:update_ferramenta', args=['1'])
        self.assertEqual(resolve(url).func, ferramenta_update_view)

    def test_delete_url_resolves(self):
        url = reverse('ferramenta:delete_ferramenta', args=['1'])
        self.assertEqual(resolve(url).func, ferramenta_delete_view)

class FerramentaModelTest(TestCase):

    def setUp(self):
        self.ferramenta = Ferramenta.objects.create(
            nome='Chave de Fenda',
            descricao='Chave de fenda phillips de tamanho médio.',
            codigo='CF001',
            quantidade_disponivel=10,
            condicao='novo'
        )

    def test_ferramenta_str_method(self):
        self.assertEqual(str(self.ferramenta), 'Chave de Fenda')

    def test_ferramenta_instance(self):
        self.assertIsInstance(self.ferramenta, Ferramenta)

    def test_ferramenta_creation(self):
        ferramenta_count = Ferramenta.objects.count()
        self.assertEqual(ferramenta_count, 1)

    def test_ferramenta_uuid(self):
        self.assertIsInstance(self.ferramenta.id, uuid.UUID)

    def test_ferramenta_unique_codigo(self):
        with self.assertRaises(Exception):
            Ferramenta.objects.create(
                nome='Chave de Fenda 2',
                descricao='Chave de fenda phillips de tamanho grande.',
                codigo='CF001',  # Código duplicado
                quantidade_disponivel=5,
                condicao='usado'
            )

class FerramentaFormTest(TestCase):

    def test_ferramenta_form_invalid(self):
        form_data = {
            'nome': 'Martelo',
            'descricao': 'Martelo de ferro com cabo de madeira.',
            'codigo': '',  # Campo código vazio para testar validação
            'quantidade_disponivel': -1,  # Valor negativo para testar validação
            'condicao': 'novo',
        }
        form = FerramentaForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Verifica se há exatamente 2 erros de validação
        self.assertEqual(len(form.errors), 2)
        # Verifica se os campos 'codigo' e 'quantidade_disponivel' estão presentes nos erros
        self.assertIn('codigo', form.errors.keys())
        self.assertIn('quantidade_disponivel', form.errors.keys())
        # Verifica a mensagem de erro esperada para o campo 'codigo'
        self.assertEqual(form.errors['codigo'][0], 'This field is required.')
        # Verifica a mensagem de erro esperada para o campo 'quantidade_disponivel'
        self.assertEqual(form.errors['quantidade_disponivel'][0], 'Ensure this value is greater than or equal to 0.')
