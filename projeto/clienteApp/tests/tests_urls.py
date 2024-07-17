from django.test import SimpleTestCase  # type: ignore
from django.urls import reverse, resolve  # type: ignore
from clienteApp.views import cliente_create_view, cliente_list_view, cliente_update_view, cliente_delete_view


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
