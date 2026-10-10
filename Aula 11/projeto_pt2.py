class UsuarioSistema:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def create(self):
        novo_usuario = input("Digite o nome do novo usuário: ")
        self.usuarios.append(novo_usuario)
        print(f"Usuário {novo_usuario} cadastrado com sucesso!")

    def read(self):
        print("Usuários cadastrados:")
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario}")

    def update(self):
        self.read() 
        indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
        if 0 <= indice < len(self.usuarios):
            novo_nome = input(f"Digite o novo nome para {self.usuarios[indice]}: ")
            self.usuarios[indice] = novo_nome
            print(f"Usuário atualizado para {novo_nome} com sucesso!")
        else:
            print("Usuário inválido.")

    def delete(self):
        self.read()
        indice = int(input("Digite o número do usuário que deseja excluir: ")) - 1
        if 0 <= indice < len(self.usuarios):
            removido = self.usuarios.pop(indice)
            print(f"Usuário {removido} excluído com sucesso!")
        else:
            print("Usuário inválido.")


def menu():
    usuarios = ["Pietryk", "Judy"]  
    sistema = UsuarioSistema(usuarios)

    opcao = 0
    while opcao != 5:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Usuário")
        print("2 - Ler Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            sistema.create()
        elif opcao == 2:
            sistema.read()
        elif opcao == 3:
            sistema.update()
        elif opcao == 4:
            sistema.delete()
        elif opcao == 5:
            print("Encerrando o sistema.")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
