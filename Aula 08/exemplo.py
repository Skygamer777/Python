frutas_disponiveis = ["Banana","Maçã","Laranja"]
info_fruta = ("Banana",3.50, 20)
frutas_fora_de_estoque = {"Maçã","Kiwi"}
estoque = {
    "Banana":{"preco":3.50,"Quantidade":20},
    "Laranja": {"preco":2.75,"Quantidade":15}
}
print("Frutas disponiveis: ",frutas_disponiveis)
print("Informações sobre a fruta: ",info_fruta)
print("Frutas fora de estoque: ",frutas_fora_de_estoque)
print("Estoque atualizado: ",estoque)

print("Preço da banana: ",estoque["Banana"]["Quantidade"])
print("Quantidade da banana: ",estoque["Banana"]["Quantidade"])