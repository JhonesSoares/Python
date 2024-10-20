import abc
import conta

class Person(abc.ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value: int):
        self._age = value

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name} {attrs}'     


class Customer(Person):
    def __init__(self, name: str, age: int, ) -> None:
        super().__init__(name, age)
        self.account: conta.Account | None = None





if __name__== '__main__':

    cliente_1 = Customer('jhones', 30)
    cliente_1.account = conta.CheckingAccount(111, 222, 0, 100)
    print(cliente_1)
    print(cliente_1.account)
