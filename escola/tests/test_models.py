from django.test import TestCase
from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    def teste_falha(self):
        self.fail('Teste falhou :(')