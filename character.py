from hp_bar import Hp_bar

class Character:
    
    def __init__(self, name, speed, stamina_type):
        self.name = name
        self.speed = speed
        self.stamina_type = stamina_type
        self.hp = 100+(self.stamina_type*10)
        self.max_hp = self.hp

    def is_alive(self):
        return self.hp > 0

    def is_dead(self):
        if self.hp <= 0:
            self.hp = 0 
            return True
        return False

    def __str__(self):
        hp_display = "is dead" if self.hp == 0 else f"{Hp_bar.draw(self.hp, self.max_hp)} HP"
        return f"{self.name} ({hp_display}, Speed: {self.speed}, Stamina Type: {self.stamina_type})"