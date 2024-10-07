from animal import Animal

class Mamifero(Animal):
    def __init__(self) -> None:
        super().__init__()

        self._cor_pelo = None

    @property
    def set_cor_pelo(self):
        return self._cor_pelo
    @set_cor_pelo.setter
    def set_cor_pelo(self, valor):
        self._cor_pelo = valor

    def locomover(self):
        print(f'Correndo')

    def alimentar(self):
        print(f'Mamando')

    def emitir_som(self):
        print('Som de mamifero')    

class Canguru(Mamifero):
    def uasr_bolsa(self):
        print('Usando bolsa')

    def locomover(self):
        print('O Canguru está saltando.')        

class Cachorro(Mamifero):
    def enterrar_osso(self):
        print(f'Enterrando o osso.')

    def abanar_rabo(self):
        print('Ábanando o rabo.')

    def emitir_som(self):
        print(f'Cachorro está latindo')            


if __name__ == '__main__':
    pass        