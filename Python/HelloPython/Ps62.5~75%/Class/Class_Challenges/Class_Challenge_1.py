print("1. 사람 클래스 만들기")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("안녕하세요, 저는 ", self.name, "이고, ", self.age, "입니다.")

p1 = Person("홍길동", 20)
p1.introduce()
print()

print("2. 계산기 클래스 만들기")
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(self.num1 + self.num2)
    
    def sub(self):
        print(self.num1 - self.num2)

c1 = Calculator(3, 2)
c1.add()
c1.sub()
print()

print("3. 로그인 시스템 클래스")
class User_1:
    def __init__(self , input_id, input_pw):
        self.input_id = input_id
        self.input_pw = input_pw
    
    def login(self):
        if self.input_id == "admin" and self.input_pw == "1234":
            print("로그인 성공")
        else:
            print("로그인 실패")
    
user = User_1("admin", "1234")
user.login()
print()

print("4. 은행 계좌 클래스")
class Account:
    def __init__(self,balance):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("잔액 부족")

    def check_balance(self):
        print(self.balance)


print("5. 자동 증가 ID 부여하기")
class User:
    next_id = 1
    def __init__(self,name):
        self.name = name
        self.user_id = User.next_id
        User.next_id += 1
    
    def show(self):
        print(f"{self.name}님의 고유번호 : {self.user_id}")

u1 = User("홍길동")
u2 = User("철수")
u1.show()
u2.show()
