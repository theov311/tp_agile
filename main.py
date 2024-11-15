import random

#class perso
class Personnage:
    def __init__(self):
        self.hp = 100
        self.vitesse = random.randint(1, 10)

    def get_hp(self):
        return self.hp

    def recevoir_attaque(self, attaquant):
        if self.hp > 0:
            degats = random.randint(0, 10)
            if random.random() < 0.05:  
                degats = 20
            elif random.random() < 0.05:  
                attaquant.hp -= 10
                return
            self.hp = max(0, self.hp - degats)

    def est_mort(self):
        return self.hp == 0


# calss equipe
class Equipe:
    def __init__(self, nombre_personnages):
        self.personnages = [Personnage() for _ in range(nombre_personnages)]

    def est_eliminee(self):
        return all(personnage.est_mort() for personnage in self.personnages)


#Fct Trier par vitesse
def trier_par_vitesse(personnages):
    return sorted(personnages, key=lambda x: x.vitesse, reverse=True)

#fct simuler combat
def simuler_combat(equipes):
    tour = 1
    while True:
        print(f"Tour {tour}")
        tous_personnages = [p for equipe in equipes for p in equipe.personnages if not p.est_mort()]
        
        for attaquant in trier_par_vitesse(tous_personnages):
            if attaquant.est_mort():
                continue
            
            cibles_possibles = [p for equipe in equipes for p in equipe.personnages if p != attaquant and not p.est_mort()]
            if not cibles_possibles:
                break
            
            cible = random.choice(cibles_possibles)
            
            hp_avant = cible.get_hp()
            
            attaquant.recevoir_attaque(cible)
            
            hp_apres = cible.get_hp()
            
            print(f"Personnage attaque et inflige {hp_avant - hp_apres} dégâts")
        
        equipes_en_vie = [equipe for equipe in equipes if not equipe.est_eliminee()]
        if len(equipes_en_vie) <= 1:
            break
        tour += 1
    
    if len(equipes_en_vie) == 1:
        print(f"L'équipe gagnante a {sum(1 for p in equipes_en_vie[0].personnages if not p.est_mort())} survivants")
    else:
        print("Match nul")
    


# Simulation
nombre_equipes = 2
personnages_par_equipe = 2
equipes = [Equipe(personnages_par_equipe) for _ in range(nombre_equipes)]
simuler_combat(equipes)

