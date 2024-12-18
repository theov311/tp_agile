import random
from hp_bar import Hp_bar  # Assurez-vous que vous avez une classe Hp_bar pour afficher la barre de vie.

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

        # Mise à jour de la santé de l'attaquant et de la cible
        target.hp = max(0, target.hp)
        attacker.hp = max(0, attacker.hp)

        # Affichage de l'état des personnages après le tour
        if target.hp > 0:
            result += f"\n{target.name} now has: {Hp_bar.draw(target.hp, target.max_hp)} HP"
        if attacker.hp > 0:
            result += f"\n{attacker.name} now has: {Hp_bar.draw(attacker.hp, attacker.max_hp)} HP"

        return result

    @staticmethod
    def _calculate_damage(dice_result, attacker, target):
        """Calculer les dégâts selon le résultat du lancer de dés."""
        if dice_result == 1:  # Fumble
            damage = 10 + attacker.weapon.damage
            attacker.hp -= damage
            event = f"😱 Fumble! {attacker.name} accidentally deals {damage} damage to themselves!"
            if attacker.is_dead():
                event += f"\n💀 {attacker.name} is dead due to a fumble!"
        elif dice_result == 10:  # Critical hit
            damage = 20 + attacker.weapon.damage
            target.hp -= damage
            event = f"💥 Critical hit! {attacker.name} deals {damage} damage to {target.name}!"
            if target.is_dead():
                event += f"\n💀 {target.name} is dead!"
        else:  # Normal attack
            damage = dice_result + attacker.weapon.damage
            target.hp -= damage 
            event = f"{attacker.name} attacks {target.name} for {damage} damage!"
            if target.is_dead():
                event += f"\n💀 {target.name} is dead!"

        return damage, event

    @staticmethod
    def play_game(teams):
        """Joue une bataille entre plusieurs équipes."""
        print("\n--- Battle Start! ---")
        log = []
        rounds = 0

        # Mélange tous les personnages de toutes les équipes
        all_characters = sorted([char for team in teams for char in team], key=lambda c: c.speed, reverse=True)

        while len([char for team in teams for char in team if char.is_alive()]) > 1:  # Tant qu'il y a plus d'une équipe vivante
            rounds += 1
            log.append(f"\n--- Turn {rounds} ---")

            # Chercher le prochain attaquant (le premier personnage vivant)
            attacker = next((char for char in all_characters if char.is_alive()), None)
            if attacker is None:
                break

            # Trouver les cibles : les autres équipes que celle de l'attaquant
            target_teams = [team for team in teams if attacker not in team]
            target_team = random.choice(target_teams)
            alive_targets = [char for char in target_team if char.is_alive()]

            if not alive_targets:
                continue

            # Sélectionner une cible parmi les vivants de l'équipe ennemie
            target = max(alive_targets, key=lambda c: c.stamina_type, default=min(alive_targets, key=lambda c: c.hp))

            # Effectuer le tour de combat
            result = Battle.battle_turn(attacker, target)
            if result:
                log.append(result)

            # Vérifier si une équipe a perdu tous ses membres
            for team in teams:
                if all(not char.is_alive() for char in team):
                    log.append(f"\n--- {team[0].name}'s Team is eliminated! ---")
                    teams.remove(team)

            if len(teams) == 1:
                log.append(f"\n--- {teams[0][0].name}'s Team Wins! ---")
                break

            # Réorganiser les personnages pour le tour suivant
            all_characters = all_characters[1:] + [all_characters[0]]

        # Résumé à la fin
        log.append("\n--- Game Over ---")
        if len(teams) == 1:
            log.append(f"Winning Team: {teams[0][0].name}'s Team")
        else:
            log.append("No Team Wins! All teams are eliminated.")

        log.append("\n--- Remaining Teams ---")
        for team in teams:
            alive_players = [char for char in team if char.is_alive()]
            log.append(f"{team[0].name}'s Team: {len(alive_players)} players remaining")

        # Affichage de tous les personnages et leur statut (mort ou vivant)
        log.append("\n--- All Characters Status ---")
        for team in teams:
            for char in team:
                status = "Alive" if char.is_alive() else "Dead"
                log.append(f"{char.name}: {status}")

        return log, rounds