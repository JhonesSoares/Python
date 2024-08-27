# Métodos em intâncias de classes Python
# Hard Coded - É algo que foi escrito diretamente do código

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} está acelerando.')

fusca = Carro('fusca')
fusca.acelerar()

celta = Carro('Celta')
celta.acelerar()