import random
from hp_bar import Hp_bar

class Battle:
    
    @staticmethod
    def battle_turn(attacker, target):
        """Effectue un tour de bataille entre l'attaquant et la cible."""
        if not attacker.is_alive() or not target.is_alive():
            return None

        dice_result = random.randint(1, 10)
        result = f"Dice Result: {dice_result}/10\n"

        damage, event = Battle._calculate_damage(dice_result, attacker, target)

        result += event

        target.hp = max(0, target.hp)
        attacker.hp = max(0, attacker.hp)

        if target.hp > 0:
            result += f"\n{target.name} now has: {Hp_bar.draw(target.hp, target.max_hp)} HP"
        if attacker.hp > 0:
            result += f"\n{attacker.name} now has: {Hp_bar.draw(attacker.hp, attacker.max_hp)} HP"

        return result

    @staticmethod
    def _calculate_damage(dice_result, attacker, target):
        """Calculer les dégâts selon le résultat du lancer de dés."""
        if dice_result == 1:  # Fumble
            damage = 10
            attacker.hp -= damage
            event = f"😱 Fumble! {attacker.name} accidentally deals {damage} damage to themselves!"
            if attacker.is_dead():
                event += f"\n💀 {attacker.name} is dead due to a fumble!"
        elif dice_result == 10:  # Critical hit
            damage = 20
            target.hp -= damage
            event = f"💥 Critical hit! {attacker.name} deals {damage} damage to {target.name}!"
            if target.is_dead():
                event += f"\n💀 {target.name} is dead!"
        else:  # Normal attack
            damage = dice_result
            target.hp -= damage
            event = f"{attacker.name} attacks {target.name} for {damage} damage!"
            if target.is_dead():
                event += f"\n💀 {target.name} is dead!"

        return damage, event

    @staticmethod
    def play_game(team1, team2):
        """Joue une bataille entre les deux équipes."""
        print("\n--- Battle Start! ---")
        log = []
        rounds = 0

        all_characters = sorted(team1 + team2, key=lambda c: c.speed, reverse=True)

        while any(char.is_alive() for char in team1) and any(char.is_alive() for char in team2):
            rounds += 1
            log.append(f"\n--- Turn {rounds} ---")

            attacker = next((char for char in all_characters if char.is_alive()), None)
            if attacker is None:
                break

            target_team = team2 if attacker in team1 else team1
            alive_targets = [char for char in target_team if char.is_alive()]

            if not alive_targets:
                break

            target = max(alive_targets, key=lambda c: c.stamina_type, default=min(alive_targets, key=lambda c: c.hp))

            result = Battle.battle_turn(attacker, target)
            if result:
                log.append(result)

            if not any(char.is_alive() for char in team1):
                log.append("\n--- Team 2 Wins! ---")
                return log, rounds
            if not any(char.is_alive() for char in team2):
                log.append("\n--- Team 1 Wins! ---")
                return log, rounds

            all_characters = all_characters[1:] + [all_characters[0]]

        return log, rounds
