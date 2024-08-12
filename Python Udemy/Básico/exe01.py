#PRIMEIRA MANEIRA
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impa_texto = 'Ímpar'

    if par_impar:
        par_impa_texto ='Par'

    print(f'O número {entrada_int} é {par_impa_texto}')
else:
    print('Você não digitou um número interiro')   


#SEGUNDA MANEIRA
entrada = input('Digite um número: ')

try  :
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impa_texto = 'Ímpar'

    if par_impar:
        par_impa_texto ='Par'

    print(f'O número {entrada_int} é {par_impa_texto}')
except:
    print('Você não digitou um número interiro')
     