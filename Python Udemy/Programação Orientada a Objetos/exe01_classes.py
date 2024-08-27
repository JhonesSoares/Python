# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Jhones', 'Soares')
#p1.nome = 'abestadoooooooo'
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa('Maria', 'Joana')
print(p2.nome)
print(p2.sobrenome)