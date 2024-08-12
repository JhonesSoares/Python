# CALCULADORA COM WHILE

while True:
    numero_1 = input('Digite primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+ - / *): ')
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:    
        numeros_validos = None

    
    if numeros_validos is None:
        print('Um dos números são inválidos!!')
        continue
        
    operadores_permitidos = '(+-/*)'
    if operador not in operadores_permitidos:
        print('O operador é inválido!!')
        continue
    if len(operador) > 1 and operador == '':
        print('Digite apenas um operador!!')
        continue

    if operador != '':
        if operador == '+':
            res = num_1_float + num_2_float
        elif operador == '-':
             res = num_1_float - num_2_float
        elif operador == '/':
            res = num_1_float / num_2_float
        elif operador == '*':
            res = num_1_float * num_2_float
        print(f'O resultado de {numero_1} {operador} {numero_2} é igual a {res}')            
    else:
        print('Digite um operador!!')
        continue    

    if numeros_validos is None:
        print('Um dos números são inválidos!!')
                

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break