#  INTRODUÇÃO ÀS GENERATOR FUNCTIONS EM PYTHON

def generator(n=0):
    yield 1 # pausar
    print('continuando...')

    yield 2 #pause
    print('mais uma...')

    yield 3 
    print('vou terminar...')

    return 'acabou'

gen = generator(n=0)

#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

#ITERANDO COM FOR
for n in gen:
    print(n)


def generator2(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator2(maximum=1000000)
for n in gen:
    print(n)    


# Yield from
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()    