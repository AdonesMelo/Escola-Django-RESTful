from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula

class MatriculasTesCase(APITestCase):
    def setUp(self):
        self.ususario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.ususario)
        self.estudante_01 = Estudante.objects.create(
            nome='Aluno Teste Um',
            email='aluno01@teste.com',
            cpf='92919454048',
            data_nascimento='2000-01-01',
            celular='11 99999-9999'
        )
        self.curso_01 = Curso.objects.create(
            codigo='DEV01',
            descricao='Testes Curso 01',
            nivel='B'
        )
        # Cria a matrícula alvo do teste
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_01,
            curso=self.curso_01,
            periodo='V'
        )

        self.estudante_02 = Estudante.objects.create(
            nome='Aluno Teste Dois',
            email='aluno02@teste.com',
            cpf='76521504002',
            data_nascimento='2000-01-01',
            celular='11 99999-9999'
        )
        self.curso_01 = Curso.objects.create(
            codigo='DEV02',
            descricao='Testes Curso 02',
            nivel='A'
        )
        # Cria a matrícula alvo do teste
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_02,
            curso=self.curso_01,
            periodo='N'
        )

    def test_requisicao_get_para_listar_matricula(self):
        '''Teste de requisição GET'''
        reponse = self.client.get(self.url)
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)