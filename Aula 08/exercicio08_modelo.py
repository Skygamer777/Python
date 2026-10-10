usuarios = ["Luiz", "Felipe", "Tiago", "Ricardo"]
opcoes = [
          "C - Cadastrar Usuário", 
          "R - Leitura de usuários", 
          "U - Atualizar Usuários", 
          "D - Deletar Usuário",
          "Sair"
]

def solicitar_opcao():
    try:
        return int(input("Digite o número da opção desejada: "))
    except ValueError:
        return None

def exibir_opcoes():
    print("Escolha uma opção:")
    for indice, descricao in enumerate(opcoes, start=1):
        print(f"{indice}. {descricao}")

exibir_opcoes()
opcao = solicitar_opcao()

while opcao is not None and 1 <= opcao <= 4:
    if opcao == 1:
        print("Você escolheu a opção Cadastro.")
        novo_usuario = input("Digite o nome do novo usuário: ").strip()
        if novo_usuario:
            usuarios.append(novo_usuario)
            print(f"Usuário {novo_usuario} cadastrado com sucesso!")
        else:
            print("O nome não pode ficar vazio.")

    elif opcao == 2:
        print("Você escolheu a opção Leitura.")  
        for usuario in usuarios:
            print(usuario) 

    elif opcao == 3:
        print("Você escolheu a opção Atualização.")
        for i, usuario in enumerate(usuarios,start=1):
            print(f"{i}.{usuario}")
        try:
            indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
        except ValueError:
            print("Por favor, insira um número válido.")
            indice = -1
        if 0 <= indice < len(usuarios):
            novo_nome = input("Digite o novo nome de usuário: ").strip()
            if novo_nome:
                usuarios[indice] = novo_nome
                print(f"Usuário atualizado para {novo_nome} com sucesso!")
            else:
                print("O nome não pode ficar vazio.")
        else:
            print("Usuário inválido")

    elif opcao == 4:
        print("Você escolheu a opção Exclusão.")
        for i, usuario in enumerate(usuarios, start=1):
            print(f'{i}.{usuario}')
        try:
            indice = int(input("Digite o número do usuário que deseja excluir: ")) - 1
        except ValueError:
            print("Por favor, insira um número válido.")
            indice = -1
        if 0 <= indice < len(usuarios):
            removido = usuarios.pop(indice)
            print(f"Usuário {removido} excluido com sucesso!")
        else:
            print("Usuário inválido")

    exibir_opcoes()
    opcao = solicitar_opcao()

if opcao == 5:
    print("Encerrando o sistema.")
else:
    print("Opção inválida. Encerrando o sistema.")

