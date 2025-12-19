from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

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
    
    def test_requisicao_get_para_listar_estudantes(self):
        '''Teste de requisição GET'''
        reponse = self.client.get(self.url) #/estudantes/
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        '''Teste de requisição GET para um estudante'''
        reponse = self.client.get(f'{self.url}1/') #/estudantes/1/
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(reponse.data, dados_estudante_serializados)

    def test_resquisicao_post_para_criar_um_estudante(self):
        '''Teste de requisição POST para um estudante'''
        dados = {
            'nome': 'Teste',
            'email': 'teste@teste.com',
            'cpf': '18877832029',
            'data_nascimento': '2020-03-03',
            'celular': '84 88888-3333'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_resquisicao_delete_um_estudante(self):
        '''Teste de requisição DELETE um estudante'''
        response = self.client.delete(f'{self.url}2/') # estudante/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_resquisicao_put_para_atualizar_um_estudante(self):
        '''Teste de requisição PUT para um estudante'''
        dados = {
            'nome': 'Put',
            'email': 'testeput@teste.com',
            'cpf': '93874577023',
            'data_nascimento': '2021-01-02',
            'celular': '11 22222-3333'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)