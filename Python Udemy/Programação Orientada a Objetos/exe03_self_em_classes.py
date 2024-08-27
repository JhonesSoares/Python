# ENTENDENDO SELF EM CLASSES
# Classe - Molde (geralmente sem dados)
# Instância da class(objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a própia instância

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} está acelerando.')

fusca = Carro('fusca')
Carro.acelerar(fusca)

celta = Carro('Celta')
Carro.acelerar(celta)