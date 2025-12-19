from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

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
    
    def test_requisicao_get_para_listar_cursos(self):
        '''Teste de requisição GET'''
        reponse = self.client.get(self.url)#/cursos/
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_curso(self):
        '''Teste de requisição GET para um curso'''
        reponse = self.client.get(f'{self.url}1/') #/curso/1/
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(reponse.data, dados_curso_serializados)

    def test_resquisicao_post_para_criar_um_curso(self):
        '''Teste de requisição POST para um curso'''
        dados = {
            'codigo': 'TEST01',
            'descricao': 'Teste 01',
            'nivel':'A'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_resquisicao_delete_um_curso(self):
        '''Teste de requisição DELETE um curso'''
        response = self.client.delete(f'{self.url}2/') # curso/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_resquisicao_put_para_atualizar_um_curso(self):
        '''Teste de requisição PUT para um curso'''
        dados = {
            'codigo': 'TEST01',
            'descricao': 'TestePut',
            'nivel':'B'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)