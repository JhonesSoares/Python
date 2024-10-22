import conta
import pessoa

class Bank:
    def __init__(
            self,
            agency: list[int] | None = None,
            customer: list[pessoa.Person] | None = None,
            account: list[conta.Account] | None = None
            ):
        self.agency = agency or []
        self.customer = customer or []
        self.account = account or []

    def _check_agency(self, account):
        if account._agency in self.agency:
            return True
        return False

    def _check_customer(self, customer):
        if customer in self.customer:
            return True
        return False

    def _check_account(self, account):
        if account in self.account:
            return True
        return False
    
    def _check_customer_account(self, customer, account):
        if account is customer.account:
            return True
        return False

    def authenticate(self, customer: pessoa.Person, account: conta.Account):
        if self._check_agency(account) and self._check_customer(customer) and self._check_account(account) and self._check_customer_account(customer, account):
            return f'AUTENTICADO!'
        return f'Conta Inválida!'
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.customer!r}, {self.account!r})'
        return f'{class_name} {attrs}'    




if __name__== '__main__':

    cliente_1 = pessoa.Customer('jhones', 30)
    cliente_1.account = conta.CheckingAccount(111, 222, 0, 100)
    
    cliente_2 = pessoa.Customer('joao', 40)
    cliente_2.account = conta.SavingsAccount(333, 444, 0)

    itau = Bank()
    itau.agency.extend([111, 333])
    itau.customer.extend([cliente_1, cliente_2])
    itau.account.extend([cliente_1.account, cliente_2.account])

    print(itau.authenticate(cliente_1, cliente_1.account)) 
    