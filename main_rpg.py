import random

class Character:
    def __init__(self, name, speed, stamina_type):
        self.name = name
        self.speed = speed
        self.stamina_type = stamina_type
        if stamina_type == 1:
            self.hp = 50
        elif stamina_type == 2:
            self.hp = 75
        else:
            self.hp = 100

    def is_alive(self):
        return self.hp > 0

    def is_dead(self):
        if self.hp <= 0:
            self.hp = 0 
            return True
        return False

    def __str__(self):
        hp_display = "is dead" if self.hp == 0 else f"HP: {self.hp}"
        return f"{self.name} ({hp_display}, Speed: {self.speed}, Stamina Type: {self.stamina_type})"


def create_team(team_name, size):
    team = []
    for i in range(size):
        name = f"{team_name}_Player{i+1}"
        speed = random.randint(1, 10)
        stamina_type = random.randint(1, 3)
        team.append(Character(name, speed, stamina_type))
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

    dice_result = random.randint(1, 10)  # Simule le lancer de dés
    result = f"Dice Result: {dice_result}/10\n"  # Ajoute le résultat du dé au début

    if dice_result == 1:  # Fumble
        damage = 10
        attacker.hp -= damage
        result += f"😱 Fumble! {attacker.name} accidentally deals {damage} damage to themselves!"
        if attacker.is_dead():
            result += f"\n💀 {attacker.name} is dead due to a fumble!"
        # Pas d'affichage des HP de la cible lors du fumble
    elif dice_result == 10:  # Critical hit
        damage = 20
        target.hp -= damage
        result += f"💥 Critical hit! {attacker.name} deals {damage} damage to {target.name}!"
        if target.is_dead():
            result += f"\n💀 {target.name} is dead!"
    else:  # Normal attack
        damage = dice_result
        target.hp -= damage
        result += f"{attacker.name} attacks {target.name} for {damage} damage!"
        if target.is_dead():
            result += f"\n💀 {target.name} is dead!"

    # Assure que les HP ne descendent pas en dessous de 0
    target.hp = max(0, target.hp)
    attacker.hp = max(0, attacker.hp)

    # Affiche les HP seulement si ce n'est pas un fumble
    if dice_result != 1:  # Éviter d'afficher les HP de la cible lors d'un fumble
        if target.hp > 0:
            result += f"\n{target.name} now has: {target.hp} HP"
    if attacker.hp > 0:
        result += f"\n{attacker.name} now has: {attacker.hp} HP"

    return result

def play_game(team1, team2):
    print("\n--- Battle Start! ---")
    log = []
    rounds = 0

    # Combine and sort all characters by speed
    all_characters = sorted(team1 + team2, key=lambda c: c.speed, reverse=True)

    while any(char.is_alive() for char in team1) and any(char.is_alive() for char in team2):
        rounds += 1
        log.append(f"\n--- Turn {rounds} ---")

        attacker = next((char for char in all_characters if char.is_alive()), None)
        if attacker is None:
            break

        # Determine the target team
        target_team = team2 if attacker in team1 else team1
        alive_targets = [char for char in target_team if char.is_alive()]

        if not alive_targets:
            break

        # Check if the highest stamina target is still alive
        highest_stamina_target = max(alive_targets, key=lambda c: c.stamina_type, default=None)
        if highest_stamina_target and highest_stamina_target.is_alive():
            target = highest_stamina_target
        else:
            # If the tank is dead, attack the character with the lowest HP
            target = min(alive_targets, key=lambda c: c.hp)

        # Execute the attack
        result = battle_turn(attacker, target)
        if result:
            log.append(result)

        # Check win condition
        if not any(char.is_alive() for char in team1):
            log.append("\n--- Team 2 Wins! ---")
            return log, rounds
        if not any(char.is_alive() for char in team2):
            log.append("\n--- Team 1 Wins! ---")
            return log, rounds

        # Rotate the character list for the next turn
        all_characters = all_characters[1:] + [all_characters[0]]

    return log, rounds


if __name__ == "__main__":
    print("Welcome to the RPG Battle Simulator!")
    team1 = create_team("Team1", size=3)
    team2 = create_team("Team2", size=3)

    display_teams(team1, team2)
    log, total_rounds = play_game(team1, team2)

    print("\n".join(log))
    print(f"\nTotal Turns: {total_rounds}")
    print("\nFinal Teams State:")
    display_teams(team1, team2)
