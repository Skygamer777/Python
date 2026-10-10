class carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def detalhes(self):
        return f"Carro: {self.marca}, {self.modelo}, Ano: {self.ano}"
meu_carro = carro("Toyota","Corolla", 2020)
print(meu_carro.detalhes())