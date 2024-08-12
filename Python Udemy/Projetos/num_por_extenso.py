from num2words import num2words

numero_usuario = int(input('Digite um numero: '))

num_ingles = num2words(numero_usuario, lang='en')
print(f'Em inglês: {num_ingles}')
numero_ingles_ordinario = num2words(numero_usuario, lang='en', to='ordinal')
print(f'Em ordinário: {numero_ingles_ordinario}')

num_protugues = num2words(numero_usuario, lang='pt-br')
print(f'Em Português: {num_protugues}')
numero_portugues_ordinario = num2words(numero_usuario, lang='pt-br', to='ordinal')
print(f'Em Português: {numero_portugues_ordinario}')