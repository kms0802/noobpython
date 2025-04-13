class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def bark(self):
        print("멍멍!")
d = Dog()
d.speak()
d.bark()

