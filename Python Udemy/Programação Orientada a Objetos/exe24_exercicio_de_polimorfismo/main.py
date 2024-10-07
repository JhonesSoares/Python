from animal import Animal
from mamifero import Mamifero, Canguru, Cachorro
from reptil import Reptil
from peixe import Peixe
from ave import Ave

cachorro = Canguru()
cachorro.set_peso(85)
cachorro.set_idade(2)
cachorro._membros('4 membros')
cachorro.alimentar()
cachorro.emitir_som()
cachorro.locomover()

print(cachorro.__dict__)