nome = input('Digite seu nome: ')
tamanho_nome = len(nome)


if tamanho_nome > 1 and nome == str:
    if tamanho_nome <= 4:
        print('Seu nome é pequeno')
    elif tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('digitr mais de uma letra')
       