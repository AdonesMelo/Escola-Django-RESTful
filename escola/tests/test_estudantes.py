from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante

class EstudantesTesCase(APITestCase):
    def setUp(self):
        self.ususario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.ususario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste Estudante Um',
            email = 'testeestudantes01@teste.com',
            cpf = '30130395072',
            data_nascimento = '2020-01-01',
            celular = '79 99999-1111'
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste Estudante Dois',
            email = 'testeestudantes02@teste.com',
            cpf = '65377837045',
            data_nascimento = '2020-02-02',
            celular = '79 99999-2222'
        )
    
    def test_requisicao_get_para_listar_estudante(self):
        '''Teste de requisição GET'''
        reponse = self.client.get(self.url)
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)