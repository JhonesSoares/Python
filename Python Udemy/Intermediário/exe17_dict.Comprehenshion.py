# dictionary comprehenshion e Set Comprehenshion

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
dc_1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}
print(dc_1)




lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
dc_2 = {
    chave: valor
    for chave, valor in lista
}
print(dc_2)



s1 = {i for i in range(10)}
print(s1)