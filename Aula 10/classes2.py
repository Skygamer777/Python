class Pessoa:
    lista_pessoas = []
    def __init__(self, nome, idade, naturalidade):
        self.nome = nome
        self.idade = idade
        self.naturalidade = naturalidade
    def detalhes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Estado em que nasceu: {self.naturalidade}"
    @classmethod
    def adicionar(cls, pessoa):
        cls.lista_pessoas.append(pessoa)
    
    @classmethod
    def exibir_pessoas(cls):
        for pessoa in cls.lista_pessoas:
            print(pessoa.detalhes())
pessoa1 = Pessoa("Marcos Vinicius",30,"SP")
pessoa2 = Pessoa("Emmanue",25,"PR")            
            
Pessoa.adicionar(pessoa1)       
Pessoa.adicionar(pessoa2)

Pessoa.exibir_pessoas()
       
       