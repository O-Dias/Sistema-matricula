import random
import string

class Aluno:
    def __init__(self, nome, matricula, data_nascimento, sexo, endereco, telefone, email):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
    
    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Matrícula: {self.matricula}')
        print(f'Data de Nascimento: {self.data_nascimento}')
        print(f'Sexo: {self.sexo}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}\n')

alunos = {}

def gerar_matricula():
    while True:
        letra_inicial = random.choice(string.ascii_uppercase)
        numeros = ''.join(random.choices(string.digits, k=7))
        matricula = letra_inicial + numeros
        if matricula not in alunos:
            return matricula

def cadastrar_aluno():
    print('\n{ CADASTRO DE ALUNOS }')
    nome = input('Digite o nome do aluno: ')
    matricula = gerar_matricula()
    print(f'Matrícula gerada: {matricula}')
    data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
    sexo = input('Digite o sexo (M/F): ')
    endereco = input('Digite o endereço: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ')
    
    aluno = Aluno(nome, matricula, data_nascimento, sexo, endereco, telefone, email)
    alunos[matricula] = aluno
    print('\nAluno cadastrado!\n')

def listar_alunos():
    print('\n{ LISTA DE ALUNOS }')
    if alunos:
        for aluno in alunos.values():
            aluno.exibir_informacoes()
    else:
        print('Nenhum aluno cadastrado.\n')

def buscar_aluno_por_matricula():
    print('\n{ BUSCAR ALUNO POR MATRÍCULA }')
    matricula = input('Digite o número da matrícula: ').strip()
    aluno = alunos.get(matricula)
    if aluno:
        aluno.exibir_informacoes()
    else:
        print('Matrícula não encontrada.\n')
