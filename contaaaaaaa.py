class ContaBancaria:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__saldo = 0.0  # Inicializando o saldo como 0
    
    # Getter para o saldo
    def get_saldo(self):
        return self.__saldo
    
    # Método para realizar depósito
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")
    
    # Método para realizar saque
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")
    
    # Método para exibir dados do usuário
    def exibir_dados(self):
        print(f"Nome: {self.__nome} {self.__sobrenome}")
        print(f"CPF: {self.__cpf}")
        print(f"Saldo atual: R${self.get_saldo():.2f}")

def main():
    print("Bem-vindo ao Banco POO!")
    
    # Solicitando dados do usuário
    nome = input("Informe seu nome: ")
    sobrenome = input("Informe seu sobrenome: ")
    cpf = input("Informe seu CPF: ")
    
    # Criando uma instância da conta bancária
    conta = ContaBancaria(nome, sobrenome, cpf)
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Encerrar")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            conta.exibir_dados()
        elif opcao == '2':
            valor = float(input("Informe o valor para depósito: R$"))
            conta.depositar(valor)
        elif opcao == '3':
            valor = float(input("Informe o valor para saque: R$"))
            conta.sacar(valor)
        elif opcao == '4':
            print("Encerrando o uso da aplicação. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()