# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


caminho_arquivo = 'C:\\Users\\jhone\\OneDrive\\Documentos\\GitHub\\Python\\Python Udemy\\Intermediário\\exe37.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(    # varias linhas
        ('linha 3\n', 'linha 4\n')
    )
    arquivo.seek(0, 0) # aponta o cursor para o topo
    print(arquivo.read()) # está lendo apos as linhas sem o metodo SEEK

    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # END quebra de linha
    print(arquivo.readline().strip()) # STRIP quebra de linha

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
    #lista = arquivo.read()
    #print('--------')
    #print(list(lista))
    
print("jhones")    
    