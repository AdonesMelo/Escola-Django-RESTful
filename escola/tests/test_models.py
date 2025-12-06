from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('Teste falhou :(')
    def setUp(self):
       self.estudante = Estudante.objects.create(
           nome = 'Teste Model',
           email = 'testemodelo@teste.com',
           cpf = '74299631021',
           data_nascimento = '2023-01-01',
           celular = '99 99999-9999'
       )

    def test_verifica_atributos_de_estudante(self):
        '''Teste que verifica os atributos do modelo de estudate'''
        self.assertEqual(self.estudante.nome, 'Teste Model')
        self.assertEqual(self.estudante.email, 'testemodelo@teste.com')
        self.assertEqual(self.estudante.cpf, '74299631021')
        self.assertEqual(self.estudante.data_nascimento, '2023-01-01')
        self.assertEqual(self.estudante.celular, '99 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'PY2026',
            descricao = 'Python',
            nivel = 'A'
        )

    def test_verifica_atributos_do_curso(self):
        '''Teste que verifica os atributos do modelo do curso'''
        self.assertEqual(self.curso.codigo, 'PY2026')
        self.assertEqual(self.curso.descricao, 'Python')
        self.assertEqual(self.curso.nivel, 'A')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        # Cria as dependências necessárias (Foreign Keys)
        self.estudante = Estudante.objects.create(
            nome='Aluno Teste',
            email='aluno@teste.com',
            cpf='85191988051',
            data_nascimento='2000-01-01',
            celular='11 99999-9999'
        )
        self.curso = Curso.objects.create(
            codigo='TDD01',
            descricao='Curso de Testes com Django',
            nivel='A'
        )
        # Cria a matrícula alvo do teste
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='M'
        )

    def test_verifica_atributos_matricula(self):
        '''Verifica se a matrícula linkou corretamente aluno e curso'''
        self.assertEqual(self.matricula.estudante.cpf, '85191988051')
        self.assertEqual(self.matricula.curso.codigo, 'TDD01')
        self.assertEqual(self.matricula.periodo, 'M')