import os
from django.test import TestCase  # type: ignore
from django.core.wsgi import get_wsgi_application  # type: ignore


class WSGITest(TestCase):
    def test_wsgi_application(self):
        # Configura a variável de ambiente
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'techcell_pro.settings')

        # Importa e verifica a aplicação WSGI
        try:
            application = get_wsgi_application()
            self.assertIsNotNone(application)
        except Exception as e:
            self.fail(f"WSGI application failed to load: {e}")
