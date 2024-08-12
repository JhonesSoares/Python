#Comprehension em list
#[expression for item in list if filter]

#uma forma elegante de navegar por um lista para gerar outras coleções como resultad

numeros_lista = list(range(1,11))
print(numeros_lista)

numeros_copia = [x for x in  numeros_lista]
print(numeros_copia)
print(numeros_lista)


for x in numeros_lista:
  if x % 2 == 0:
    print(x ** 2)

[ x ** 2 for x in numeros_lista if x % 2 == 0]


numeros_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(numeros_dict)

[x for x in  numeros_dict] #gerar uma lista com as chaves

[x for x in  numeros_dict.values()] #gerar uma lista com os valores