
def parametros_decorador(nome):
    print(nome, '01') # 01

    def decorador(func):
        print(func, '02') # 02

        def sua_nova_funcao(*args, **kwargs):
            print(f'valor parametros Args: {args} -- {kwargs}') # 03
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='Primeiro')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco) # 04
