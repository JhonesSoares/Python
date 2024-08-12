"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf = '01884095216'
nove_digitos = cpf[:9]; #print(nove_digitos)
contador_regressivo_1 = 10
resultado_1 = 0

for digito1 in nove_digitos:
    resultado_1 +=  (int(digito1) * contador_regressivo_1); #print(resultado_1)
    contador_regressivo_1 -= 1
    
resultado_1 = (resultado_1 * 10) % 11
digito_1 = 0 if resultado_1 > 9 else resultado_1
print(digito_1)


## SEGUNDO DIGITO
contador_regressivo_2 = 11
resultado_2 = 0
dez_digitos = nove_digitos + str(digito_1)

for digito2 in dez_digitos:
    resultado_2 += (int(digito2) * contador_regressivo_2); #print(resultado_2)
    contador_regressivo_2 -= 1

resultado_2 = (resultado_2 * 10) % 11
digito_2 = 0 if resultado_2 > 9 else resultado_2
print(digito_2)
