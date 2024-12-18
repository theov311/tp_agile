from hp_bar import Hp_bar
import random
from weapon import Weapon

class Character:
    
    def __init__(self, name, speed, stamina_type, weapon: Weapon):
        """Initialise un personnage avec un nom, une vitesse, et un type d'endurance."""
        self.name = name
        self.speed = speed
        self.stamina_type = stamina_type
        self.hp = self.calculate_hp()
        self.max_hp = self.hp
        self.weapon = weapon


    def calculate_hp(self):
        """Calcule la vie du personnage basée sur son endurance."""
        return 100 + (self.stamina_type * 10)

    def is_alive(self):
        """Vérifie si le personnage est vivant."""
        return self.hp > 0

    def is_dead(self):
        """Vérifie si le personnage est mort et met ses points de vie à zéro."""
        if self.hp <= 0:
            self.hp = 0
            return True
        return False

    def __str__(self):
        """Renvoie une chaîne de caractères représentant le personnage."""
        hp_display = "is dead" if self.hp == 0 else f"{Hp_bar.draw(self.hp, self.max_hp)} HP"
        return f"{self.name} ({hp_display}, Speed: {self.speed}, Stamina: {self.stamina_type}, Weapon: {self.weapon.name})"

