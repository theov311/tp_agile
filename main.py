from team import Team
from battle import Battle

def main():
    """Démarre le jeu en créant les équipes et en lançant la bataille."""
    print("Welcome to the RPG Battle Simulator!")

    # Créer les équipes
    team1 = Team.create("Team1", size=3)
    team2 = Team.create("Team2", size=3)

    # Afficher les équipes
    Team.display(team1, team2)

    # Lancer la bataille
    log, total_rounds = Battle.play_game(team1, team2)

    # Afficher les résultats
    print("\n".join(log))
    print(f"\nTotal Turns: {total_rounds}")
    print("\nFinal Teams State:")
    Team.display(team1, team2)

if __name__ == "__main__":
    main()
