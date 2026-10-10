import json
from pathlib import Path

arquivo_json = Path(__file__).resolve().parent / 'nomes.JSON'

if not arquivo_json.exists():
    with arquivo_json.open('w', encoding='utf-8') as arquivo:
        json.dump([], arquivo, ensure_ascii=False, indent=4)
    print(f"Arquivo '{arquivo_json.name}' criado com uma lista vazia")

with arquivo_json.open('r', encoding='utf-8') as arquivo:
    nomes = json.load(arquivo)

if not nomes:
    print('Lista de nomes vazia.')
else:
    print('Nomes encontrados:', nomes)