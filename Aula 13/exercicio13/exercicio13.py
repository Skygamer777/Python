import json
from pathlib import Path

frutas = ['Banana', 'Maçã', 'Melancia', 'Abacate']
caminho_pasta = Path(__file__).resolve().parent / 'dados'
caminho_arquivo = caminho_pasta / 'frutas.json'

caminho_pasta.mkdir(parents=True, exist_ok=True)

with caminho_arquivo.open('w', encoding='utf-8') as arquivo_json:
    json.dump(frutas, arquivo_json, ensure_ascii=False, indent=4)

print(f'Arquivo {caminho_arquivo} criado com sucesso!')
