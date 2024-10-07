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

    def reagir(self, frase):
        if int(frase) == 'comida' or int(frase) == 'olá':
            return f'Abanar e latir'
        return f'Rosnar'
    
    def reagir(self, hora, min):
        if int(hora) < 12:
            return 'Abanar'
        if int(hora) > 18:
            return 'Ignorar'
        else:
            return 'Abanar e latir'
        
    def reagir(self, dono):
        if dono:
            return 'Abanar'
        return 'Rosnar e latir'
    
    def reagir(self, idade, peso):
        if int(idade) < 5:
            if int(peso) < 10:
                return 'Abanar'
            return 'Latir'
        else:
            if int(peso) > 10:
                return 'Rosnar'
            return 'Ignorar'    
                    


if __name__ == '__main__':
    pass        