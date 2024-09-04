
#RECUPERANDO DADOS DAS CLASSES

import json
from exe08_salvando_class_Json1 import caminho_veiculo, Veiculo, fazer_dump 

fazer_dump()

with open(caminho_veiculo, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

dados_veiculos = dados
#print(dados_veiculos)

#ANALISANDO OS DADOS
carro = dados_veiculos[0]
moto = dados_veiculos[1]
#print(moto)
#print(carro)


# RECRIANDO CLASSES(OBJ) EM BANCO DE DADOS importando classe de outro arquivo
carro_0 = Veiculo(**dados_veiculos[0])
moto_0 = Veiculo(**dados_veiculos[1])

# CRIANDO CLASSES(OBJ), IMPORTANDO DADOS EM UM BANCO DE DADOS
class Veiculo_1:
    def __init__(self, veiculo, marca, nome, cor, ano):
        self.veiculo = veiculo
        self.marca = marca
        self.nome = nome
        self.cor = cor
        self.ano = ano
carro_1 = Veiculo_1(**dados_veiculos[0])
moto_1 = Veiculo_1(**dados_veiculos[1])
#print(carro_1.__dict__)
print(moto_1.nome)
