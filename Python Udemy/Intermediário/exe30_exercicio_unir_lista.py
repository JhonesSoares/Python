# CRIE UMA FUNÇÃO ZIPPER (COMO O ZIPPER DE ROUPAS)
# ELA TEM QUE UNIR DUAS LISTAS NA ORDEM 
# USE TODOS OS VALORES DA MENOR LISTA 
# EXEMPLO:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))


# OUTRO METODO
from itertools import zip_longest

print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue= 'Sem cidade')))