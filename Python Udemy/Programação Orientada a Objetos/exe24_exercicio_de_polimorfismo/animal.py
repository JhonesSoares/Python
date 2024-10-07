# CLASSE ANIMAL (classe abstrata e principal(super))

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self) -> None:
        self._peso = int
        self._idade = int
        self._membros = str

    @property
    def set_peso(self):
        return self._peso
    @set_peso.setter
    def set_peso(self, valor):
        self._peso = valor

    @property
    def set_idade(self):
        return self._idade
    @set_idade.setter
    def set_idade(self, valor):
        self._idade = valor

    @property
    def set_membros(self):
        return self._membros
    @set_membros.setter
    def set_membros(self, valor):
        self._membros = valor

    @abstractmethod
    def locomover(self): pass

    @abstractmethod
    def alimentar(self): pass

    @abstractmethod
    def emitir_som(self): pass


if __name__ == '__main__':
    pass    