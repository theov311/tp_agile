import random
from character import Character

class Team:

    def create(team_name, size):
        team = []
        for i in range(size):
            name = f"{team_name}_Player{i + 1}"
            speed = random.randint(1, 10)
            stamina_type = random.randint(0, 10)
            team.append(Character(name, speed, stamina_type))
        return team

    def display(team1, team2):
        print("\n--- Team 1 ---")
        for char in team1:
            print(char)
        print("\n--- Team 2 ---")
        for char in team2:
            print(char)

    