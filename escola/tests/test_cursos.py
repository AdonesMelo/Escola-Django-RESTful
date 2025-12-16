from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso

class CursosTesCase(APITestCase):
    def setUp(self):
        self.ususario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.ususario)
        self.matricula_01 = Curso.objects.create(
            codigo = 'DEV01',
            descricao = 'Teste 01',
            nivel = 'B'  
        )
        self.matricula_02 = Curso.objects.create(
            codigo = 'DEV02',
            descricao = 'Teste 02',
            nivel = 'I' 
        )
    
    def test_requisicao_get_para_listar_curso(self):
        '''Teste de requisição GET'''
        reponse = self.client.get(self.url)
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)