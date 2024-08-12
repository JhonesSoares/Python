def main():
        
    def cpf_usuário():    
        import re

        cpf_informado = input('Digite seu CPF para validação: ')\
             .replace('.', '')\
             .replace('-', '')
        
        def validar_input(valor): # Verifica se o valor é uma string
            if not isinstance(valor, str):
                return False
            
            padrao = r'^\d{11}$' # Define o padrão de regex para exatamente 11 dígitos
            
            if re.match(padrao, valor): # Verifica se o valor corresponde ao padrão
                return True
            else:
                return False

        if validar_input(cpf_informado):
            #print("Input válido!")
            return cpf_informado
        else:
            print("CPF incorreto!")
            return cpf_usuário()


    cpf_enviado_pelo_usuario = str(cpf_usuário())


    def primeiro_digito():
        cpf = cpf_enviado_pelo_usuario
        nove_digitos = cpf[:9]; #print(nove_digitos)
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
        cpf = cpf_enviado_pelo_usuario
        dez_digitos = cpf[:9] + primeiro_digito()
        contador_regressivo_2 = 11
        resultado_2 = 0

        for digito2 in dez_digitos:
            resultado_2 += (int(digito2) * contador_regressivo_2); #print(resultado_2)
            contador_regressivo_2 -= 1

        resultado_2 = (resultado_2 * 10) % 11;   #print(resultado_2)
        digito_2 = 0 if resultado_2 > 9 else resultado_2
        #print(digito_2)
        return str(digito_2)

    def validando_cpf_usuario():
        cpf = cpf_enviado_pelo_usuario; #print(cpf)
        nove_digitos = cpf[:9]

        cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito()}{segundo_digito()}'

        if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
            print(f'{cpf_enviado_pelo_usuario} é válido')
        else:
            print(f'CPF inválido!')





    validando_cpf_usuario()
main()