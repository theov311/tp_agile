from team import Team
from battle import Battle

def main():
    """Démarre le jeu en créant les équipes et en lançant la bataille."""
    print("Welcome to the RPG Battle Simulator!\n")

    # Demander le nombre d'équipes et de joueurs par équipe
    try:
        nb_equipe = int(input("Choisir le nombre d'équipes: "))
        nb_player = int(input("Choisir le nombre de joueurs par équipe: "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        return

    # Initialiser les équipes
    teams = []
    team_names = []

    for i in range(nb_equipe):
        team_name = input(f"Nom de l'équipe {i + 1}: ")
        team_names.append(team_name)

        # Collecter les noms des joueurs pour chaque équipe
        players = []
        for j in range(nb_player):
            player_name = input(f"Nom du joueur {j + 1} de l'équipe {team_name}: ")
            players.append(player_name)

        # Créer l'équipe
        teams.append(Team.create(team_name, players))

    # Afficher les équipes
    Team.display(team_names, *teams)

    # Lancer la bataille avec plusieurs équipes
    log, total_rounds = Battle.play_game(teams)

    # Afficher les résultats
    print("\n".join(log))
    print(f"\nTotal Turns: {total_rounds}")
    # print("\nFinal Teams State:")
    Team.display(*teams)


if __name__ == "__main__":
    main()
