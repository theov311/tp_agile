import random
from character import Character
from weapon import Weapon
from hp_bar import Hp_bar

class Team:


    @staticmethod
    def create(team_name, player_names):
        """Crée une équipe de personnages avec un nom d'équipe et une liste de noms de joueurs."""
        return [
            Character(name, random.randint(1, 10), random.randint(0, 10), Weapon())
            for name in player_names
        ]

    @staticmethod
    def display(team_names, *teams):
        """Affiche les informations des équipes et de leurs joueurs."""
        for i, team in enumerate(teams):
            print(f"--- {team_names[i]} ---")
            for char in team:
                # Utilisation de Hp_bar.draw pour dessiner la barre de vie
                print(f"{char.name} ({Hp_bar.draw(char.hp, char.max_hp)} {char.hp}/{char.max_hp} HP, "
                      f"Speed: {char.speed}, Stamina: {char.stamina_type}, Weapon: {char.weapon})")
            print()


