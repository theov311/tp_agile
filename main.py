import random
from character import Character
from hp_bar import Hp_bar
from team import Team
from battle import Battle

if __name__ == "__main__":
    print("Welcome to the RPG Battle Simulator!")
    team1 = Team.create("Team1", size=3)
    team2 = Team.create("Team2", size=3)

    Team.display(team1, team2)
    log, total_rounds = Battle.play_game(team1, team2)

    print("\n".join(log))
    print(f"\nTotal Turns: {total_rounds}")
    print("\nFinal Teams State:")
    Team.display(team1, team2)
