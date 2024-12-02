import random

class Character:
    def __init__(self, name, speed):
        self.name = name
        self.hp = 100
        self.speed = speed
        # self.stamina = random.randint(1, 2)

    def is_alive(self):
        return self.hp > 0
    
    #######
    def is_dead(self):
        if self.hp <= 0:
            self.hp = 0  # Utiliser '=' au lieu de '=='
            return True
        return False

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Speed: {self.speed})"



def create_team(team_name, size):
    team = []
    for i in range(size):
        name = f"{team_name}_Player{i+1}"
        speed = random.randint(1, 10)
        team.append(Character(name, speed))
    return team

def display_teams(team1, team2):
    print("\n--- Team 1 ---")
    for char in team1:
        print(char)
    print("\n--- Team 2 ---")
    for char in team2:
        print(char)

def battle_turn(attacker, target):
    if not attacker.is_alive() or not target.is_alive():
        return None

    damage = random.randint(1, 10)
    critical_hit = random.random() < 0.05
    fumble = random.random() < 0.05

    if critical_hit:
        damage = 20
        target.hp -= damage
        result = f"💥 Critical hit! {attacker.name} deals {damage} damage to {target.name}!"
    elif fumble:
        damage = 10  # Changé de -10 à 10 pour cohérence
        attacker.hp -= damage
        result = f"😱 Fumble! {attacker.name} accidentally deals {damage} damage to themselves!"
    else:
        target.hp -= damage
        result = f"{attacker.name} attacks {target.name} for {damage} damage!"

    target.hp = max(0, target.hp)  # Assure que HP ne descend pas en dessous de 0
    attacker.hp = max(0, attacker.hp)  # Idem pour l'attaquant en cas de fumble

    result += f"\n{target.name} now has {target.hp} HP"
    return result

def play_game(team1, team2):
    print("\n--- Battle Start! ---")
    log = []
    rounds = 0

    # Liste des personnages triée par vitesse décroissante
    all_characters = sorted(team1 + team2, key=lambda c: c.speed, reverse=True)

    while any(char.is_alive() for char in team1) and any(char.is_alive() for char in team2):
        rounds += 1
        log.append(f"\n--- Turn {rounds} ---")

        # Sélectionner le prochain attaquant
        attacker = next((char for char in all_characters if char.is_alive()), None)
        if attacker is None:
            break  # Tous les personnages sont morts

        # Déterminer la cible
        target_team = team2 if attacker in team1 else team1
        alive_targets = [char for char in target_team if char.is_alive()]
        if not alive_targets:
            break  # Pas de cibles restantes dans l'équipe adverse
        target = random.choice(alive_targets)

        # Résoudre l'attaque
        result = battle_turn(attacker, target)
        if result:
            log.append(result)

        # Vérifier si une équipe a perdu
        if not any(char.is_alive() for char in team1):
            log.append("\n--- Team 2 Wins! ---")
            return log, rounds
        if not any(char.is_alive() for char in team2):
            log.append("\n--- Team 1 Wins! ---")
            return log, rounds

        # Réorganiser la liste pour que le prochain joueur attaque
        all_characters = all_characters[1:] + [all_characters[0]]

    return log, rounds

if __name__ == "__main__":
    print("Welcome to the RPG Battle Simulator!")
    team1 = create_team("Team1", size=3)
    team2 = create_team("Team2", size=3)

    display_teams(team1, team2)
    log, total_rounds = play_game(team1, team2)

    # Afficher le résumé du combat une seule fois
    print("\n".join(log))
    print(f"\nTotal Turns: {total_rounds}")
    print("\nFinal Teams State:")
    display_teams(team1, team2)
    
    # Ajoutez cette ligne pour marquer la fin du programme
    print("\n--- End of Simulation ---")
