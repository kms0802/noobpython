class Character:
    def attack(self):
        print("공격!")
    
class Warrior(Character):
    def attack(self):
        print("검으로 공격!")

class Archer(Character):
    def attack(self):
        print("활로 공격!")

class Mage(Character):
    def attack(self):
        print("마법으로 공격")

team = [Warrior(), Archer(), Mage()]

for member in team:
    member.attack()

print("=======================")

def battle(character):
    character.attack()

battle(Warrior())
battle(Mage())
