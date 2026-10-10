import os
import json

# Nome do diretório e do arquivo JSON
diretorio_crud = "crud"
arquivo_json = os.path.join(diretorio_crud, "nomes.json")

# Função para criar o diretório e o arquivo JSON se não existirem
def criar_arquivo_json():
    # Cria o diretório 'crud' se não existir
    if not os.path.exists(diretorio_crud):
        os.makedirs(diretorio_crud)
        
    # Cria o arquivo JSON se não existir
    if not os.path.exists(arquivo_json):
        with open(arquivo_json, 'w') as arquivo:
            json.dump([], arquivo)  # Inicializa com uma lista vazia

def ler_nomes():
    try:
        with open(arquivo_json, 'r') as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está vazio ou contém dados inválidos.")
        return []  # Retorna uma lista vazia se houver erro
    except FileNotFoundError:
        print("Erro: O arquivo JSON não foi encontrado.")
        return []  # Retorna uma lista vazia se o arquivo não existir

def salvar_nomes(nomes):
    with open(arquivo_json, 'w') as arquivo:
        json.dump(nomes, arquivo)

def menu():
    criar_arquivo_json()  # Certifique-se de que o arquivo existe ao iniciar o menu

    while True:
        print("\nMenu:")
        print("1 - Adicionar nome")
        print("2 - Listar nomes")
        print("3 - Atualizar nome")
        print("4 - Remover nome")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome a ser adicionado: ")
            nomes = ler_nomes()
            nomes.append(nome)
            salvar_nomes(nomes)
            print(f"Nome '{nome}' adicionado com sucesso.")
        
        elif opcao == '2':
            nomes = ler_nomes()
            if not nomes:
                print("A lista de nomes está vazia.")
            else:
                print("Nomes cadastrados:")
                for n in nomes:
                    print(f"- {n}")
        
        elif opcao == '3':
            nomes = ler_nomes()
            if not nomes:
                print("A lista de nomes está vazia.")
                continue
            
            print("Nomes cadastrados:")
            for idx, n in enumerate(nomes):
                print(f"{idx + 1} - {n}")
            
            try:
                indice = int(input("Digite o número do nome a ser atualizado: ")) - 1
                
                if 0 <= indice < len(nomes):
                    novo_nome = input("Digite o novo nome: ")
                    nomes[indice] = novo_nome
                    salvar_nomes(nomes)
                    print("Nome atualizado com sucesso.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == '4':
            nomes = ler_nomes()
            if not nomes:
                print("A lista de nomes está vazia.")
                continue
            
            print("Nomes cadastrados:")
            for idx, n in enumerate(nomes):
                print(f"{idx + 1} - {n}")
            
            try:
                indice = int(input("Digite o número do nome a ser removido: ")) - 1
                
                if 0 <= indice < len(nomes):
                    nome_removido = nomes.pop(indice)
                    salvar_nomes(nomes)
                    print(f"Nome '{nome_removido}' removido com sucesso.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

menu()
