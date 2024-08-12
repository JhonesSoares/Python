def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()
    
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0!
    return f'{d} de {mes_extenso} de {a}'

print(converter_mes_para_extenso('10/05/2021'))


def imprimir_mensagem(disciplina, curso):
    return f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}."
    
resultado = imprimir_mensagem("Python", "ADS")
print(f"Resultado = {resultado}")


#parâmetros posicionais indefinidos, ou seja, a passagem de valores é feita de modo posicial, porém a quantidade não é conhecida.
def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    
    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

        
print("\nChamada 1")        
imprimir_parametros("São Paulo", 10, 23.78, "João")

print("\nChamada 2")        
imprimir_parametros(10, "São Paulo")


#O último grupo de funções possui parâmetro nominal e não obrigatório. O mecanismo é parecido com as do grupo 5, porém agora a passagem é feita de modo nominal e não posicional, o que nos permite acessar tanto o valor do parâmetro quanto o nome da variável que o armazena.
def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    
    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")

        
print("\nChamada 1")        
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")

print("\nChamada 2")        
imprimir_parametros(desconto=10, valor=100)