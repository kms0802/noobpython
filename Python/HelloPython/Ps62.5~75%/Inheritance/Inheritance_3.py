class Animal:
    def speak(self):
        print("동물의 소리")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("멍멍!")
    
d = Dog()
d.speak()