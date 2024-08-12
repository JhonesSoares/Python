# insistance -  para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [1, 2, 3], (1, 2), {0, 1}, {'nome': 'Jhones'}
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item)
    
    elif isinstance(item, str):
        item.upper()
        print(item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)):
        print(item, item * 2)    

    else:
        print('OUTRO')
        print(item)