
# CRIE UMA FUÇÃO QUE DUPLICA, TRIPLICA E QUADRUPLICA UM NUMERO

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))