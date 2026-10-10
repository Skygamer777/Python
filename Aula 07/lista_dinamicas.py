lista_de_carros = []

try:
    quantidade = int(input("Quantos carros você deseja adicionar à lista? "))
except ValueError:
    print("Por favor, insira uma quantidade inteira válida.")
    raise SystemExit(1)

if quantidade < 0:
    print("A quantidade não pode ser negativa.")
    raise SystemExit(1)

for i in range(quantidade):
    carro = input(f"Digite o nome do carro {i + 1}: ").strip()
    lista_de_carros.append(carro)

print("Lista de carros criada:", lista_de_carros)

for indice, carro in enumerate(lista_de_carros):
    print(f"Na posição {indice} está o carro: {carro}")

if not lista_de_carros:
    print("Não há carros para remover.")
    raise SystemExit

try:
    indice_exclusao = int(
        input(f"Digite o índice de 0 a {len(lista_de_carros) - 1} para excluir um carro: ")
    )
except ValueError:
    print("Por favor, insira um índice inteiro válido.")
    raise SystemExit(1)

if 0 <= indice_exclusao < len(lista_de_carros):
    carro_removido = lista_de_carros.pop(indice_exclusao)
    print(f"Carro '{carro_removido}' foi removido da lista")
else:
    print("Erro: índice inválido.")