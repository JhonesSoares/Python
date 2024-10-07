from animal import Animal
from mamifero import Mamifero, Canguru, Cachorro
from reptil import Reptil
from peixe import Peixe
from ave import Ave

cachorro = Cachorro()
cachorro.set_peso(85)
cachorro.set_idade(2)
cachorro._membros('4 membros')
cachorro.alimentar()
cachorro.emitir_som()
cachorro.locomover()
print()
print(cachorro.reagir('olá'))
print(cachorro.reagir('Vai apanhar'))
print(cachorro.reagir(11, 45))
print(cachorro.reagir(21, 00))
print(cachorro.reagir(True))
print(cachorro.reagir(False))
print(cachorro.reagir(2, 12.5))
print(cachorro.reagir(17, 4.5))