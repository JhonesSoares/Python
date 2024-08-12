def main():
        
    def cpf_usuário():    
        import random

        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))
        
        return nove_digitos


    cpf_enviado_pelo_usuario = str(cpf_usuário())


    def primeiro_digito():
        nove_digitos = cpf_enviado_pelo_usuario; #print(nove_digitos)
        contador_regressivo_1 = 10
        resultado_1 = 0

        for digito1 in nove_digitos:
            resultado_1 +=  (int(digito1) * contador_regressivo_1); #print(resultado_1)
            contador_regressivo_1 -= 1
            
        resultado_1 = (resultado_1 * 10) % 11
        digito_1 = 0 if resultado_1 > 9 else resultado_1
        #print(digito_1)
        return str(digito_1)


    def segundo_digito():
        dez_digitos = cpf_enviado_pelo_usuario + primeiro_digito()
        contador_regressivo_2 = 11
        resultado_2 = 0

        for digito2 in dez_digitos:
            resultado_2 += (int(digito2) * contador_regressivo_2); #print(resultado_2)
            contador_regressivo_2 -= 1

        resultado_2 = (resultado_2 * 10) % 11;   #print(resultado_2)
        digito_2 = 0 if resultado_2 > 9 else resultado_2
        #print(digito_2)
        return str(digito_2)

    cpf_gerado_pelo_calculo = f'{cpf_enviado_pelo_usuario}{primeiro_digito()}{segundo_digito()}'
    print(cpf_gerado_pelo_calculo)





    
main()