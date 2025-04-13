class Animal:
    def sound(self):
        print("동물 소리")

class Dog(Animal):
    def sound(self):
        print("멍멍!")

d = Dog()
d.sound()

