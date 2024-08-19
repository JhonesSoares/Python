import json

arquivo_1 = 'C:\\Users\\jhone\\OneDrive\\Documentos\\GitHub\\Python\\Python Udemy\\Intermediário\\exe38.json'


pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open(arquivo_1, 'w', encoding='utf8') as arquivo: # CRIANDO O JSON
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('exe38.json', 'r', encoding='utf8') as arquivo: # LENDO ARQUIVO JSON
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    #print(pessoa['nome'])