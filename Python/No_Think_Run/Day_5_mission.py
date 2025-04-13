from abc import ABC, abstractmethod
class Payment(ABC):
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print("카드로", amount, "원 결제")

class Paypal(Payment):
    def pay(self, amount):
        print("페이팔로", amount, "원 결제")

class Cash(Payment):
    def pay(self, amount):
        print("현금으로", amount, "원 결제")

payments = [CreditCard(), Paypal(), Cash()]
for pay in payments:
    pay.pay(1000)