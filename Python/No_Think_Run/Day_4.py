from abc import ABC, abstractmethod

class Animal(ABC):
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

animals = [Dog(), Cat()]

for a in animals:
    a.speak()