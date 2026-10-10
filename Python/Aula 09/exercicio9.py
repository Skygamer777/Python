usuario = ["Bruno","Guilherme"]
def create():
    novo_usuario = input("Digite o nome do novo usuário: ")
    usuario.append(novo_usuario)
    print(f"Usuário {novo_usuario} cadastro com sucesso!")
def read():
    print("Usuários cadastrados: ")
    for i, nome in enumerate(usuario, start=1):
        print(f"{i}. {nome}")
def update():
    read()
    indice = int(input("Digite o número do usuário: ")) -1 
    if  0 <= indice < len(usuario):
        novo_nome = input(f"Digite o novo nome para {usuario[indice]}: ")
        usuario[indice] = novo_nome
        print(f"Usuário atalizado para {novo_nome} com sucesso!")
    else:
        print("Usuário inválido")
def delete():
    read()
    indice = int(input("Digite o número do usuário qe deseja excluir: ")) -1
    if 0 <= indice < len(usuario):
        removido = usuario.pop(indice)
        print(f"Usuário {removido} excluído com sucesso!")
    else:
        print("Usuário inválido")
        
def menu():
    opcao = 0 
    while opcao != 5:
        print("\nEscolha uma opção: ")
        print("1 - Cadastrar Usuários")
        print("2 - Ler Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Sair")
        
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            create()
        elif opcao == 2:
            read()
        elif opcao == 3:
            update()
        elif opcao == 4:
            delete()
        elif opcao == 5:
            print("Encerrando o sistema")
        else:
            print("Opção inválida. Tente novamente")
menu()
