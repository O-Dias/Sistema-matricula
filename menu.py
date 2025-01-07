from alunos import *
from prof import *
from disciplinas_turmas import *

def menu():
    print("\n{ MENU DE AÇÕES }")
    print("[1] Cadastrar novo aluno")
    print("[2] Cadastrar novo professor")
    print("[3] Cadastrar nova disciplina")
    print("[4] Listar alunos")
    print("[5] Listar professores")
    print("[6] Listar disciplinas")
    print("[7] Sair")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Por favor, escolha um número entre 1 e 7.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 7.")

def executar_menu():
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            cadastrar_professor()
        elif opcao == 3:
            cadastrar_disciplina()
        elif opcao == 4:
            listar_alunos()
        elif opcao == 5:
            listar_professores()
        elif opcao == 6:
            listar_disciplinas()
        elif opcao == 7:
            print("Saindo do sistema.")
            break

executar_menu()
