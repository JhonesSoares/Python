# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carinho:
    def __init__(self) -> None:
        self._produtos = []

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self.produto += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def total(self):
        preco = []
        for p in self._produtos:
            preco.append(p.preco)
        return sum(preco)          #sum([p.preco for p in self._produtos]) ----> list compreenshion

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

carinho = Carinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camisa', 20)

carinho.inserir_produtos(p1, p2)

print(carinho.listar_produtos())
print(carinho.total())
