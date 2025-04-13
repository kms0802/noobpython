class Animal:
    def sound(self):
        print("짖다")

class Lion:
    def sound(self):
        print("어흥!")

class Elephant:
    def sound(self):
        print("뿌우~")

class Snake:
    def sound(self):
        print("쉬이익~")

animals = [Animal(), Lion(), Elephant(), Snake()]
for animal in animals:
    animal.sound()