import json
from pathlib import Path


class UsuarioSistema:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.arquivo = base_dir / 'dados' / 'usuarios.json'
        self.criar_arquivo()
        self.usuarios = self.ler_usuarios()

    def criar_arquivo(self):
        self.arquivo.parent.mkdir(parents=True, exist_ok=True)
        if not self.arquivo.exists():
            with self.arquivo.open('w', encoding='utf-8') as arquivo:
                json.dump([], arquivo, ensure_ascii=False)

    def ler_usuarios(self):
        with self.arquivo.open('r', encoding='utf-8') as arquivo:
            usuarios = json.load(arquivo)
        if not isinstance(usuarios, list) or any(
            not isinstance(usuario, str) for usuario in usuarios
        ):
            raise ValueError('O arquivo de usuários deve conter uma lista de nomes.')
        return usuarios

    def create(self):
        novo_usuario = input('Digite o nome do novo usuário: ').strip()
        if not novo_usuario:
            print('O nome não pode ficar vazio.')
            return
        self.usuarios.append(novo_usuario)
        self.salvar_usuarios()
        print(f'Usuário {novo_usuario} cadastrado com sucesso!')

    def read(self):
        print('Usuários cadastrados:')
        if not self.usuarios:
            print('Nenhum usuário cadastrado.')
            return
        for indice, usuario in enumerate(self.usuarios, start=1):
            print(f'{indice}. {usuario}')

    def selecionar_indice(self, acao):
        if not self.usuarios:
            print('Nenhum usuário cadastrado.')
            return None

        self.read()
        try:
            indice = int(input(f'Digite o número do usuário que deseja {acao}: ')) - 1
        except ValueError:
            print('Por favor, insira um número válido.')
            return None

        if not 0 <= indice < len(self.usuarios):
            print('Usuário inválido.')
            return None
        return indice

    def update(self):
        indice = self.selecionar_indice('atualizar')
        if indice is None:
            return

        novo_nome = input(f'Digite o novo nome para {self.usuarios[indice]}: ').strip()
        if not novo_nome:
            print('O nome não pode ficar vazio.')
            return
        self.usuarios[indice] = novo_nome
        self.salvar_usuarios()
        print(f'Usuário atualizado para {novo_nome} com sucesso!')

    def delete(self):
        indice = self.selecionar_indice('excluir')
        if indice is None:
            return
        removido = self.usuarios.pop(indice)
        self.salvar_usuarios()
        print(f'Usuário {removido} excluído com sucesso!')

    def salvar_usuarios(self):
        with self.arquivo.open('w', encoding='utf-8') as arquivo:
            json.dump(self.usuarios, arquivo, ensure_ascii=False, indent=4)