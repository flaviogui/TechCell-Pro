from uuid import uuid4
from django.test import TestCase
from django.urls import reverse
from .models import Reparo, Aparelho
from django.utils import timezone

class ReparoIntegrationTest(TestCase):
    def setUp(self):
        self.aparelho = Aparelho.objects.create(nome="Aparelho Teste", descricao="Descrição Teste")
        self.reparo = Reparo.objects.create(
            aparelho=self.aparelho,
            custo_estimado=100.00,
            data_inicio=timezone.now(),
            data_conclusao=None,
            status='pendente',
            protocolo=uuid4(),
        )

    def test_confirmar_reparo_view(self):
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
