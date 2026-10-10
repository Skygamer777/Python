import os
import json

arquivo_JSON = "nomes.JSON"

if not os.path.exists(arquivo_JSON):
    with open(arquivo_JSON, "w", encoding='utf-8') as arquivo:
        json.dump([], arquivo) 
    print(f"Arquivo '{arquivo_JSON}' criado com uma lista vazia")
with open(arquivo_JSON, "r",encoding='utf-8') as arquivo:
    nomes = json.load(arquivo)
    
if not nomes:
    print("Lista de nomes vazia.")
else:
    print("Nomes encontrados: ",nomes)
    