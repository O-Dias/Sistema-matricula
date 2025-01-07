import random
import string
from prof import professores

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria, professor=None):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.professor = professor

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Código: {self.codigo}')
        print(f'Carga Horária: {self.carga_horaria} horas')
        if self.professor:
            print(f'Professor: {self.professor.nome}')
        print()

disciplinas = {}

def gerar_codigo():
    while True:
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if codigo not in disciplinas:
            return codigo

def cadastrar_disciplina():
    print('\n{ CADASTRO DE DISCIPLINAS }')
    nome = input('Digite o nome da disciplina: ')
    codigo = gerar_codigo()
    carga_horaria = input('Digite a carga horária (em horas): ')

    disciplina = Disciplina(nome, codigo, carga_horaria)
    disciplinas[codigo] = disciplina
    print('\nDisciplina cadastrada com sucesso!\n')

def listar_disciplinas():
    print('\n{ LISTA DE DISCIPLINAS }')
    if disciplinas:
        for disciplina in disciplinas.values():
            disciplina.exibir_informacoes()
    else:
        print('Nenhuma disciplina cadastrada.\n')
