class Shape:
    def draw(self):
        print("도형을 그립니다.")
    
class Circle(Shape):
    def draw(self):
        print("원을 그립니다.")

class Square(Shape):
    def draw(self):
        print("정사각형을 그립니다.")

shapes = [Circle(), Square()]

for s in shapes:
    s.draw()

class Animal:
    def sound(self):
        print("기본 동물 소리")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("멍멍!")

Dog().sound()

class Notifier:
    def notify(self):
        print("알림을 보냅니다.")

class EmailNotifier(Notifier):
    def notify(self):
        print("이메일 알람 전송!")

class SMSNotifier(Notifier):
    def notify(self):
        print("문자 알림 전송!")

def send_all(notifiers):
    for n in notifiers:
        n.notify()

send_all([EmailNotifier(), SMSNotifier()])