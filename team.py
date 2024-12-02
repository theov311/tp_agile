import random
from character import Character

class Team:

    @staticmethod
    def create(team_name, size):
        """Crée une équipe de personnages avec un nom et une taille donnés."""
        return [
            Character(f"{team_name}_Player{i + 1}", random.randint(1, 10), random.randint(0, 10))
            for i in range(size)
        ]

    @staticmethod
    def display(*teams):
        """Affiche les informations de toutes les équipes données."""
        for i, team in enumerate(teams, 1):
            print(f"\n--- Team {i} ---")
            for char in team:
                print(char)
