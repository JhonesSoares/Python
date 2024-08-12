
entrada = input('Digite a hora em números intéiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço ess hora!')            
except:
    print('Digite apenas números')    