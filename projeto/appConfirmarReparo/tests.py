from audioop import reverse
from django.test import TestCase, Client # type: ignore
from django.test import TestCase # type: ignore
from appConfirmarReparo.models import Reparo
from aparelhoApp.models import Aparelho # type: ignore


class ReparoIntegrationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.aparelho = Aparelho.objects.create(
            nome='Notebook',
            descricao='Notebook de alta performance',
            marca='MarcaZ',
            modelo='ModeloX',
            imei='111111111111111',
            numero_serie='SN1111111111',
            descricao_problema='Problema com o teclado'
        )
        self.reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            descricao_problema='Problema com o teclado',
            custo_estimado=200.00,
        )

    def test_confirmar_reparo_view(self):
        # Confirmação do reparo
        response = self.client.post(reverse('confirmar_reparo', args=[self.reparo.pk]), {
            'custo_estimado': 250.00,

        })
        self.reparo.refresh_from_db()
        self.assertEqual(self.reparo.status, 'concluido')
        self.assertEqual(response.status_code, 302)  # Redirecionamento após a confirmação

    def test_view_reparo_status(self):
        response = self.client.get(reverse('reparo_detalhes', args=[self.reparo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Notebook de alta performance')
        self.assertContains(response, 'Problema com o teclado')