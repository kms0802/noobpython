class Account:
    def __init__(self, balance):
        self.__balance = balance
    
    def desposit(self, amount):
        self.__balance = self.__balance + amount
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
    
    def check_balance(self):
        print(self.__balance)

ac = Account(2000)
ac.desposit(1000)
ac.check_balance()

class Product:
    def __init__(self, name, stock):
        self.name = name
        self._stock = stock