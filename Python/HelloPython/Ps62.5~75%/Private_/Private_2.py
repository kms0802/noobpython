class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

acc = Account(1000)
print(acc.get_balance())
acc.set_balance(2000)
print(acc.get_balance)