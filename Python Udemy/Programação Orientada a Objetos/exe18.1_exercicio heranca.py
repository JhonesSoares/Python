import datetime
ano_atual = datetime.datetime.today().date().year
#print(ano_atual)

class Pessoa:
    def __init__(self, nome, idade, sexo ):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo

    def fazer_aniversario(self):
        self.__idade += 1
        return self.__idade 

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self, valor):
        self.__sexo = valor


class Aluno(Pessoa):
    def __init__(self):
        self.__matricula = 'Ativa'
        self.__curso = None

    def cancelar_matricula(self):
        return f'Matricula cancelada com sucesso!'

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self, valor):
        self.__curso = valor


class Professor(Pessoa):
    def __init__(self, especialidade, salario) -> None:
        self.__especialidade = especialidade
        self.__salario = salario

    def receber_aumento(self, aum):
        self.__salario += aum
        return self.__salario

    @property
    def especialidade(self):
        return self.__especialidade
    @especialidade.setter
    def especialidade(self, valor):
        self.__especialidade = valor

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, valor):
        self.__salario = valor

class Funcionario(Pessoa):
    def __init__(self, setor, trabalhando):
        self.__setor = setor
        self.__trabalhando = trabalhando

    def mudar_trabalho(self):
        if self.__trabalhando:
            return f'O funcionário {self.__nome} está trabalhando.'
        return f'O funcionário {self.__nome} não está trabalhando.'    

    @property
    def setor(self):
        return self.__setor
    @setor.setter
    def setor(self, valor):
        self.__setor = valor 

    @property
    def trabalhando(self):
        return self.__trabalhando
    @trabalhando.setter
    def trablhando(self, valor):
        self.__trabalhando = valor     


aluno = Aluno()

aluno.nome = 'jhones'
aluno.idade = 30
aluno.sexo = 'M'
aluno.curso = 'informatica'
print(aluno.__dict__)


    
