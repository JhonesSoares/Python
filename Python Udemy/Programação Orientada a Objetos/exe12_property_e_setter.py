# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor) -> None:
        self.cor_tinta = cor
        self.__cor = self.cor_tinta
        self.__cor_tampa = None

    @property
    def cor(self):          # OBTEM VALOR DO ATRIBUTO (GETTER)
        return self.__cor
    @cor.setter
    def cor(self, valor):        # HABILITA PARA OBTER NOVO VALOR PARA ATRIBUTO (SETTER)
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self.__cor = valor
    
    @property
    def cor_tampa(self):
        return self.__cor_tampa
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self.__cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Laranjado'
caneta.cor_tampa = 'Vermelho'

print(caneta.cor_tampa, caneta.cor)
