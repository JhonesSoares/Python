import json

class Veiculo:
    def __init__(self, veiculo, marca, nome, cor, ano):
        self.veiculo = veiculo
        self.marca = marca
        self.nome = nome
        self.cor = cor
        self.ano = ano


carro = Veiculo('Carro','Ford', 'Raptore', 'Preto', 2023)
moto = Veiculo('Moto','Royal Enfield', 'Meteor', 'Preto fosco', 2024)
caminhao = Veiculo('Caminhão', 'Iveco', 'Baú', 'Branco', 2018)
onibus = Veiculo('Ônibus', 'Mercedes', 'Convencional', 'Vermelho', 2019)

dados_veiculos = [carro.__dict__, vars(moto), caminhao.__dict__, vars(onibus)]
#print(dados_veiculos)

caminho_veiculo = 'C:\\Users\\jhone\\OneDrive\\Documentos\\GitHub\\Python\\Python Udemy\\Programação Orientada a Objetos\\exe08_salvandoClass_em_BD\\exe08_veiculos.json'

def fazer_dump():
    with open(caminho_veiculo, 'w', encoding='utf8') as arquivo_veiculo:
        json.dump(dados_veiculos,  arquivo_veiculo, ensure_ascii=False, indent=2)

