class Veiculo:
    def __init__(self, modelo, placa, diaria):
        self.modelo = modelo
        self.placa = placa
        self.diaria = diaria

    def calcular_locacao(self, dias):
        return self.diaria * dias 
    
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def locar_veiculo(self, veiculo, dias):
        return Locacao(self, veiculo, dias)
    
class Locacao:
    def __init__(self, cliente, veiculo, dias):
        self.cliente = cliente
        self.veiculo = veiculo
        self.dias = dias
        self.valor_total = self.valor_locacao()

    def valor_locacao(self):
        return self.veiculo.calcular_locacao(self.dias)
    
    def detalhes_locacao(self):
        print(f'Cliente: {self.cliente.nome}')
        print(f'Veículo: {self.veiculo.modelo}')
        print(f'Dias: {self.dias}')
        print(f'Valor total: R${self.valor_total:.2f}')


v1 = Veiculo('Ford Range', 'ABC-123', 150)
c1 = Cliente('Jhones', '00000')

l1 = c1.locar_veiculo(v1, 5)

l1.detalhes_locacao()
