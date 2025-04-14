class User:
    def __init__(self, name, pw):
        self.name = name
        self.__password = pw
    
    def show_info(self):
        print("이름:", self.name)
        print("비밀번호:", self.__password)

u = User("홍길동", "1234")
u.show_info()

class Account:
    def __init__(self):
        self.__balance = 0
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("0 이상만 가능합니다.")

acc = Account()
acc.set_balance(1000)
print(acc.get_balance())

class Machine:
    def __init__(self,):
        self._power = 100
    
class Robot(Machine):
    def use_power(self):
        self._power -= 10
        print("남은 전력", self._power)

r = Robot()
r.use_power()