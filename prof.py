import random
import string

class Professor:
    def __init__(self, nome, matricula, data_nascimento, sexo, endereco, telefone, email, disciplina=None):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.disciplina = disciplina

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Matrícula: {self.matricula}')
        print(f'Data de Nascimento: {self.data_nascimento}')
        print(f'Sexo: {self.sexo}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        if self.disciplina:
            print(f'Disciplina: {self.disciplina}')
        print()

professores = {}

def gerar_matricula_professor():
    while True:
        letra_inicial = random.choice(string.ascii_uppercase)
        numeros = ''.join(random.choices(string.digits, k=7))
        matricula = letra_inicial + numeros
        if matricula not in professores:
            return matricula

def cadastrar_professor():
    print('\n{ CADASTRO DE PROFESSORES }')
    nome = input('Digite o nome do professor: ')
    matricula = gerar_matricula_professor()
    print(f'Matrícula gerada: {matricula}')
    data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
    sexo = input('Digite o sexo (M/F): ')
    endereco = input('Digite o endereço: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ')

    professor = Professor(nome, matricula, data_nascimento, sexo, endereco, telefone, email)
    professores[matricula] = professor
    print('\nProfessor cadastrado com sucesso!\n')

def listar_professores():
    print('\n{ LISTA DE PROFESSORES }')
    if professores:
        for professor in professores.values():
            professor.exibir_informacoes()
    else:
        print('Nenhum professor cadastrado.\n')

def buscar_professor_por_matricula():
    print('\n{ BUSCAR PROFESSOR POR MATRÍCULA }')
    matricula = input('Digite o número da matrícula: ').strip()
    professor = professores.get(matricula)
    if professor:
        professor.exibir_informacoes()
    else:
        print('Matrícula não encontrada.\n')