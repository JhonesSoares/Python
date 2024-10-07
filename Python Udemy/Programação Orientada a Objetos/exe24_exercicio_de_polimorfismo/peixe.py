from animal import Animal

class Peixe(Animal):
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
        print(f'Nadando')

    def alimentar():
        print(f'Comendo ração')

    def emitir_som(self):
        print('Peixe não faz som.')    

    def solta_bolha(self):
        print(f'soltou bolha')


class Baleia(Peixe):
    ...




if __name__ == '__main__':
    pass        
