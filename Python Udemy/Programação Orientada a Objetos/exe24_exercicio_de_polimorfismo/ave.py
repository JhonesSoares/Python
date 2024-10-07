from animal import Animal

class Ave(Animal):
    def __init__(self) -> None:
        super().__init__()
        
        self._cor_pena = None

    @property
    def set_cor_pena(self):
        return self._cor_pena
    @set_cor_pena.setter
    def set_cor_pena(self, valor):
        self._cor_pena = valor

    def locomover(self):
        print(f'Voando')

    def alimentar():
        print(f'Comendo ração')

    def emitir_som(self):
        print('Som de ave.')    

    def fazer_ninho(self):
        print(f'Fez um ninho')


class Arara(Ave):
    ...




if __name__ == '__main__':
    pass