class Hp_bar:
    
    @staticmethod
    def draw(current_hp, max_hp, length=20):
        """Retourne une représentation sous forme de barre de vie."""
        filled_length = int(length * current_hp / max_hp)
        bar = "█" * filled_length + "-" * (length - filled_length)
        return f"[{bar}] {current_hp}/{max_hp}"
