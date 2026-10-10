lista_de_carros = []

quantidade = int(input("Quantos carros você deseja adicionar á lista?"))

for i in range(quantidade):
    carro = input(f"Digite o nome do carro {i}: ")
    lista_de_carros.append(carro)


print("Listade carros criada: ", lista_de_carros)

for index,carro in enumerate(lista_de_carros):
    print(f"Na posição {index} está o carro : {carro}")


indice_exclusao = int(input(f"Digite o índice de 0 a {len(lista_de_carros)-1} para excluir um carro"))

if 0 <= indice_exclusao < len(lista_de_carros):
    carro_removido = lista_de_carros.pop(indice_exclusao)
    print(f"Carro '{carro_removido}' foi removido da lista")
else:
    print('ERROR : Índice inválido.')