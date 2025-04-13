class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

a = Animal()
b = Dog()
c = Cat()

a.speak()
b.speak()
c.speak()

print("=============================")



print("=============================")

def sound(animal):
    animal.speak()

sound(Dog())
sound(Cat())

print("======= 실전 ================")

class Bird:
    def speak(self):
        print("짹쨱")

animals = [Dog(), Cat(), Animal(), Bird()]

for animal in animals:
    animal.speak()

