class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("안녕하세요",self.name)
    
p1 = Person("홍길동")
p1.greet()

class Dog:
    def __init__(self,name):
        self.name = name

dog1 = Dog("멍멍이")

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def hit(self):
        self.hp -= 10
        print(self.name, "공격받음! 남은 HP:", self.hp)

e1 = Enemy("고블린", 100)
e2 = Enemy("슬라임", 50)

e1.hit()
e2.hit()