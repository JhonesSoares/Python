from animal import Animal

class Reptil(Animal):
    def __init__(self) -> None:
        super().__init__()

        self._cor_escama = None

    @property
    def set_cor_escama(self):
        return self._cor_escama
    @set_cor_escama.setter
    def set_cor_escama(self, valor):
        self._cor_escama = valor

    def locomover(self):
        print(f'Rastejando')

    def alimentar():
        print(f'Comendo uma perna')

    def emitir_som(self):
        print('Som de reptíl')    

class Tartaruga(Reptil):
    def locomover(self):
        print(f'Tartaruga se locomovendo bem devagar...')

class Cobra(Reptil):
    ...        


if __name__ == '__main__':
    pass
