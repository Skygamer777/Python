import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.usuarioSistema import UsuarioSistema


def exibir_menu():
    print('\nEscolha uma opção:')
    print('1 - Cadastrar Usuário')
    print('2 - Ler Usuários')
    print('3 - Atualizar Usuário')
    print('4 - Deletar Usuário')
    print('5 - Sair')


def processar_opcao(sistema, opcao):
    if opcao == 1:
        sistema.create()
        return True
    if opcao == 2:
        sistema.read()
        return True
    if opcao == 3:
        sistema.update()
        return True
    if opcao == 4:
        sistema.delete()
        return True
    if opcao == 5:
        print('Encerrando o sistema.')
        return False

    print('Opção inválida. Tente novamente.')
    return True


def menu():
    try:
        sistema = UsuarioSistema()
    except (OSError, ValueError) as erro:
        print(f'Não foi possível carregar os usuários: {erro}')
        return
    opcao = 0

    while opcao != 5:
        exibir_menu()
        try:
            opcao = int(input('Digite o número da opção desejada: '))
        except ValueError:
            print('Por favor, insira um número válido.')
            continue

        if not processar_opcao(sistema, opcao):
            break


if __name__ == '__main__':
    menu()
