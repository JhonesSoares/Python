#Tuplas em Python
#tuple
#Coleção ordenada e imutável
#São declaradas com colchetes.

tupla_regioes = ("Norte", "Sul", "Sudeste","Nordeste", "Centro Oeste")
print(tupla_regioes)

tupla_regioes = ("Norte", 1, "Sudeste",3, "Centro Oeste")
print(tupla_regioes)

#ACESSAR ITENS NA TUPLA
#Para acessar itens de tupla utilize o número do índice, entre colchetes:
tupla_regioes = ("Norte", "Sul", "Sudeste","Nordeste", "Centro Oeste")
print(tupla_regioes[1])

tupla_regioes = ("Norte", "Sul", "Sudeste","Nordeste", "Centro Oeste", "Noroeste", "Leste" )
print(tupla_regioes[2:5]) #intervalos de índices

tupla_regioes = ("Norte", "Sul", "Sudeste","Nordeste", "Centro Oeste", "Noroeste", "Leste" )
print(tupla_regioes[-4:-1]) #indexação negativa


#ALTERAR VALORES DA TUPLA
#Como as tuplas são imutáveis ou imutáveis, a alternativa é converter a tupla em uma lista, alterar a lista e converter a lista novamente em uma tupla.
x = ("Norte", "Sul", "Sudeste","Nordeste", "Centro Oeste")
y = list(x)
y[1] = "SUL"
x = tuple(y)
print(x)


#LOOP ATRAVÉS DE UMA TUPLA USANDO UM FORLOOP
tupla_regioes = ("Norte", "Sul", "Sudeste","Nordeste", "Centro Oeste")
for x in tupla_regioes:
  print(x)



