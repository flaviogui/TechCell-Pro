from django.test import TestCase  # type: ignore
from clienteApp.forms import ClienteForm


class ClienteFormTest(TestCase):

    def test_cliente_form_valid(self):
        form_data = {
            'nome': 'Novo Cliente',
            'email': 'novo@cliente.com',
            'telefone': '987654321',
            'cpf': '12345678909'  # CPF válido de exemplo
        }
        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_cliente_form_invalid(self):
        form_data = {
            'nome': 'Novo Cliente',
            'email': 'email_invalido',  # Email inválido para testar validação
            'telefone': '987654321',
            'cpf': '12345678901'  # CPF inválido para testar validação
        }
        form = ClienteForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Verifica se há exatamente 1 erro de validação
        self.assertEqual(len(form.errors), 2)
        # Verifica se o campo 'cpf' está presente nos erros
        self.assertIn('cpf', form.errors.keys())
        # Verifica a mensagem de erro esperada
        self.assertEqual(form.errors['cpf'][0], 'Número de CPF inválido')
