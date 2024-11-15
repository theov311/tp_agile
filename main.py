import time
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10 

    def attack(self, other):
        if self.hp > 0:
            other.hp -= 1
            print(f"{self.name} attaque {other.name} !")
            if other.hp <= 0:
                other.hp = 0
                print(f"{other.name} est mort !")
            else:
                print(f"{other.name} a maintenant {other.hp} HP.")
        else:
            print(f"{self.name} ne peut pas attaquer car il est mort.")

character1 = Character("David")
character2 = Character("Goliath")

turn_counter = 1

while character1.hp > 0 and character2.hp > 0:
    print(f"\n--- Tour n°{turn_counter} ---")
    
    attacker = random.choice([character1, character2])
    defender = character2 if attacker == character1 else character1
    
    attacker.attack(defender)
    
    time.sleep(1) 

    turn_counter += 1

if character1.hp != 0:
    print("Le vainqueur est David !")
else:
    print("Le vainqueur est Goliath !")
