from django.test import TestCase  # type: ignore
from clienteApp.models import Cliente


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
