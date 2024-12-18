import random

# class Weapon:

#     def weapon_damage():
#         dice_result = random.randint(1, 3)
#         if dice_result == 1:
#             damage_weapon = 0
#             print(f"Bare-handed attack")
#         elif dice_result == 2:
#             damage_weapon = 10
#             print(f"Sword attack")
#         else:
#             damage_weapon = 15
#             print(f"Gun attack")
        
#         result = f"Dice Result: {dice_result}/10\n"

class Weapon:

    def __init__(self):
        self.index = random.randint(1, 3)
        self.name = ""
        self.damage = 0
        self.weapon_damage()

    def weapon_damage(self):
        if self.index == 1:
            self.name = "Bare-handed"
            self.damage = 0
        elif self.index == 2:
            self.name = "Sword"
            self.damage = 5
        elif self.index == 3:
            self.name = "Gun"
            self.damage = 10
        return self.damage