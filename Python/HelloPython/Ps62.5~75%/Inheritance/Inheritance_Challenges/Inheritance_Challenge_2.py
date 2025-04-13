class Animal:
    def move(self):
        print("움직입니다.")
    
class Bird(Animal):
    def fly(self):
        print("하늘을 납니다.")

bird = Bird()
bird.move()
bird.fly()