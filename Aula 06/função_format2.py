produtos = ["PC Gamer","Xbox Series","Playstation 5","Nintendo Switch","Notebook Gamer"]
valores = [8000,3000,4500,2500,6000]
for produto,valor in zip(produtos, valores):
    print("O valor de {} é R${} ".format(produto,valor))

for i in range(len(produtos)):
    print("O valor de {} é R${}".format(produtos[i], valores[i]))

for i, produto in enumerate(produtos):
    print("O valor de {} é R${}".format(produtos[i], valores[i]))