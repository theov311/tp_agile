class Hp_bar:
    
    def draw(current_hp, max_hp, length=20):
        """Affiche une barre de vie visuelle."""
        filled_length = int(length * current_hp / max_hp)
        bar = "█" * filled_length + "-" * (length - filled_length)
        return f"[{bar}] {current_hp}/{max_hp}"