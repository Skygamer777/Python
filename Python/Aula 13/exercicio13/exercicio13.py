import os
import json

if not os.path.exists('exercicio13/dados'):
    os.makedirs('exercicio13/dados')
    frutas = ["Banana","Maçã","Melancia","Abacate"]
    
caminho_arquivo = os.path.join('exercicio13/dados','frutas.json')

with open(caminho_arquivo, 'w', encoding="utf-8") as arquivo_json:
    json.dump(frutas,arquivo_json, ensure_ascii=False, indent=4)

print(f"Arquivo {caminho_arquivo} criado com sucesso!")
