class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("안녕하세요. 제 이름은 ", self.name, "입니다.")

p1 = Person("철수", 20)
p1.greet()

class Account:
    def __init__(self,username):
        self.username = username
        self.logged_in = False
    
    def login(self):
        self.logged_in = True
        print(self.username, "님 로그인되었습니다.")

a1 = Account("admin")
a1.login()