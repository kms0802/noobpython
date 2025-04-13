class Animal:
    def speak(self):
        print("???")

class Cat(Animal):
    def speak(self):
        print("야옹!")

c = Cat()
c.speak()