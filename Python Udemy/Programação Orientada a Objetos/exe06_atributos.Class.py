#ATRIBUSTOS DE CLASSE

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasscimento(self):
        return Pessoa.ano_atual - self.idade    
    
p1 = Pessoa('Jhones', 30)

print(p1.get_ano_nasscimento())
print(Pessoa.ano_atual)
