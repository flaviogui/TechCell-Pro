from django.test import TestCase, Client  # type: ignore
from django.urls import reverse, resolve  # type: ignore
from funcionarioApp.models import Funcionario
from django.test import SimpleTestCase  # type: ignore
from funcionarioApp.forms import FuncionarioForm
import uuid
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

class FuncionarioModelTest(TestCase):

    def setUp(self):
        # Criando um objeto Funcionario para testar
        self.funcionario = Funcionario.objects.create(
            id=uuid.uuid4(),
            nome="João Silva",
            email="joao.silva@example.com",
            telefone="1234567890",
            cpf="12345678909",  # CPF válido como string
            cargo="atendente"
        )

    def test_funcionario_creation(self):
        # Testa se o objeto Funcionario foi criado corretamente
        funcionario = Funcionario.objects.get(id=self.funcionario.id)
        self.assertEqual(funcionario.nome, "João Silva")
        self.assertEqual(funcionario.email, "joao.silva@example.com")
        self.assertEqual(funcionario.telefone, "1234567890")
        self.assertEqual(funcionario.cpf, "12345678909")
        self.assertEqual(funcionario.cargo, "atendente")

    def test_funcionario_str_representation(self):
        # Testa o método __str__ do modelo Funcionario
        self.assertEqual(str(self.funcionario), "João Silva")

    def test_funcionario_default_cargo(self):
        # Testa o valor padrão do campo cargo
        funcionario_sem_cargo = Funcionario.objects.create(
            id=uuid.uuid4(),
            nome="Maria Silva",
            email="maria.silva@example.com",
            telefone="0987654321",
            cpf="98765432100"  # CPF válido como string
        )
        self.assertEqual(funcionario_sem_cargo.cargo, "-")

    def test_funcionario_ordering(self):
        # Testa a ordenação dos objetos Funcionario pelo campo nome
        Funcionario.objects.create(
            id=uuid.uuid4(),
            nome="Ana Souza",
            email="ana.souza@example.com",
            telefone="1122334455",
            cpf="11122233344",  # CPF válido como string
            cargo="técnico"
        )
        funcionarios = Funcionario.objects.all()
        self.assertEqual(funcionarios[0].nome, "Ana Souza")
        self.assertEqual(funcionarios[1].nome, "João Silva")

class FuncionarioFormTest(TestCase):

    def test_form_valid_data(self):
        form_data = {
            'nome': 'João Silva',
            'email': 'joao.silva@example.com',
            'telefone': '1234567890',
            'cpf': '12345678909',
            'cargo': 'atendente',
        }
        form = FuncionarioForm(data=form_data)
        self.assertTrue(form.is_valid())
        funcionario = form.save()
        self.assertEqual(funcionario.nome, 'João Silva')
        self.assertEqual(funcionario.email, 'joao.silva@example.com')
        self.assertEqual(funcionario.telefone, '1234567890')
        self.assertEqual(funcionario.cpf, '12345678909')
        self.assertEqual(funcionario.cargo, 'atendente')

    def test_form_invalid_data(self):
        form_data = {
            'nome': '',  # Nome em branco deve falhar
            'email': 'email_invalido',
            'telefone': '1234567890',
            'cpf': 'cpf_invalido',  # CPF inválido
            'cargo': 'cargo_invalido',  # Cargo não está na lista de escolhas
        }
        form = FuncionarioForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('cpf', form.errors)
        self.assertIn('cargo', form.errors)

    def test_form_missing_data(self):
        form_data = {
            'nome': 'Maria Souza',
            # Falta o campo 'email'
            'telefone': '0987654321',
            'cpf': '98765432100',
            'cargo': 'técnico',
        }
        form = FuncionarioForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_default_values(self):
        form_data = {
            'nome': 'Carlos Oliveira',
            'email': 'carlos.oliveira@example.com',
            'cpf': '12345678909',  # Usando um CPF válido
            'cargo': '-',  # Explicitamente fornecendo o valor padrão
        }
        form = FuncionarioForm(data=form_data)
        
        # Verifique se o formulário é válido
        self.assertTrue(form.is_valid(), msg=form.errors)  # Inclua os erros no msg para depuração

        # Se for válido, salve e verifique o valor padrão
        if form.is_valid():
            funcionario = form.save()
            self.assertEqual(funcionario.cargo, '-')  # Testa o valor padrão para cargo