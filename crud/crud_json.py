import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
diretorio_crud = base_dir
arquivo_json = diretorio_crud / 'nomes.json'


def criar_arquivo_json():
    diretorio_crud.mkdir(parents=True, exist_ok=True)
    if not arquivo_json.exists():
        with arquivo_json.open('w', encoding='utf-8') as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=4)


def ler_nomes():
    try:
        with arquivo_json.open('r', encoding='utf-8') as arquivo:
            nomes = json.load(arquivo)
    except json.JSONDecodeError as erro:
        raise ValueError('O arquivo JSON está vazio ou contém dados inválidos.') from erro
    if not isinstance(nomes, list) or any(not isinstance(nome, str) for nome in nomes):
        raise ValueError('O arquivo JSON deve conter uma lista de nomes.')
    return nomes


def salvar_nomes(nomes):
    with arquivo_json.open('w', encoding='utf-8') as arquivo:
        json.dump(nomes, arquivo, ensure_ascii=False, indent=4)


def exibir_menu():
    print('\nMenu:')
    print('1 - Adicionar nome')
    print('2 - Listar nomes')
    print('3 - Atualizar nome')
    print('4 - Remover nome')
    print('0 - Sair')


def processar_opcao(opcao):
    if opcao == '1':
        nome = input('Digite o nome a ser adicionado: ').strip()
        if not nome:
            print('O nome não pode ficar vazio.')
            return True
        nomes = ler_nomes()
        nomes.append(nome)
        salvar_nomes(nomes)
        print(f"Nome '{nome}' adicionado com sucesso.")
        return True

    if opcao == '2':
        nomes = ler_nomes()
        if not nomes:
            print('A lista de nomes está vazia.')
        else:
            print('Nomes cadastrados:')
            for nome in nomes:
                print(f'- {nome}')
        return True

    if opcao == '3':
        nomes = ler_nomes()
        if not nomes:
            print('A lista de nomes está vazia.')
            return True

        print('Nomes cadastrados:')
        for indice, nome in enumerate(nomes, start=1):
            print(f'{indice} - {nome}')

        try:
            indice = int(input('Digite o número do nome a ser atualizado: ')) - 1
            if 0 <= indice < len(nomes):
                novo_nome = input('Digite o novo nome: ').strip()
                if not novo_nome:
                    print('O nome não pode ficar vazio.')
                    return True
                nomes[indice] = novo_nome
                salvar_nomes(nomes)
                print('Nome atualizado com sucesso.')
            else:
                print('Índice inválido.')
        except ValueError:
            print('Por favor, insira um número válido.')
        return True

    if opcao == '4':
        nomes = ler_nomes()
        if not nomes:
            print('A lista de nomes está vazia.')
            return True

        print('Nomes cadastrados:')
        for indice, nome in enumerate(nomes, start=1):
            print(f'{indice} - {nome}')

        try:
            indice = int(input('Digite o número do nome a ser removido: ')) - 1
            if 0 <= indice < len(nomes):
                nome_removido = nomes.pop(indice)
                salvar_nomes(nomes)
                print(f"Nome '{nome_removido}' removido com sucesso.")
            else:
                print('Índice inválido.')
        except ValueError:
            print('Por favor, insira um número válido.')
        return True

    if opcao == '0':
        print('Saindo do sistema...')
        return False

    print('Opção inválida, tente novamente.')
    return True


def menu():
    criar_arquivo_json()

    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        try:
            if not processar_opcao(opcao):
                break
        except (OSError, ValueError) as erro:
            print(f'Não foi possível processar os dados: {erro}')


if __name__ == '__main__':
    menu()
