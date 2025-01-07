from alunos import cadastrar_aluno, listar_alunos, buscar_aluno_por_matricula

def menu():
    print("\n{ MENU DE AÇÕES }")
    print("[1] Cadastrar novo aluno")
    print("[2] Listar alunos")
    print("[3] Buscar aluno por matrícula")
    print("[4] Sair")
    
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 4:
                return opcao
            else:
                print("Por favor, escolha um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 4.")

def executar_menu():
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            listar_alunos()
        elif opcao == 3:
            buscar_aluno_por_matricula()
        elif opcao == 4:
            print("Saindo do sistema.")
            break


executar_menu()