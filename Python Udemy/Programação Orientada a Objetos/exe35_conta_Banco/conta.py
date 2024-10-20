import abc

class Account(abc.ABC):
    def __init__(self, agency:int, account:int, balance:float=0 ) -> None:
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value:float):
        self._balance = value

    @abc.abstractmethod
    def withdraw(self, value:float) -> float: ...

    def deposit(self, value:float) -> float:
        self._balance += value
        self.details(f'DEPÓSITO DE {value}')
        return self._balance

    def details(self, msg:str='') -> None:
        print(f'O seu saldo é {self._balance:.2f} {msg}')

class SavingsAccount(Account):
    def withdraw(self, value:float) -> float:
        post_withdrawal_value = self._balance - value

        if post_withdrawal_value >= 0:
            self._balance -= value
            self.details(f'SAQUE DE {value}')
            return self._balance
        
        print(f'Não foi possível sacar o valor desejado')
        self.details(f'SAQUE NEGADO {value}')
        return self._balance
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'(Agência {self._agency!r}, Conta {self._account!r}, Saldo {self._balance})'
        return f'{class_name} {attrs}'

class CheckingAccount(Account):
    def __init__(self, agency:int, account:int, balance:float=0, limit:float=0) -> None:
        super().__init__(agency, account, balance)
        self._limit = limit

    def withdraw(self, value:float) -> float:
        post_withdrawal_value = self._balance - value
        maximum_limit = -self._limit

        if post_withdrawal_value >= maximum_limit:
            self._balance -= value
            self.details(f'SAQUE DE {value}')
            return self._balance
        
        print(f'Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self._limit:.2f}')
        self.details(f'SAQUE NEGADO {value}')
        return self._balance

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'(Agência {self._agency!r}, Conta {self._account!r}, Saldo {self._balance}, Limite {self._limit})'
        return f'{class_name} {attrs}'       





if __name__ == '__main__':
    #cp1 = SavingsAccount(111, 222, 10)
    #print(cp1.balance)
    #cp1.withdraw(11)
    #cp1.deposit(2)
    #print(cp1.balance)

    cc1 = CheckingAccount(111, 222, 0, 100)
    cc1.withdraw(11)
    cc1.deposit(2)