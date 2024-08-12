# GENRATOR EXPRESSION, ITERABLES E ITARATORS EM PYTHON

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e next

lista = [n for n in range(10)]
generator = (n for n in range(10)) #OBJETO GENERATOR É COM -->  () , DIMINIU ESPAÇO NA MEMORIA (NÃO É TUPLA), NÃO PODE ACESSAR POR INDICE

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    ...
    #print(n)