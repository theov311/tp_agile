Objectif: Divertir des joueurs avec un RPG automatique, lui permettant de choisir les paramètres des équipes qui s'affrontent

Définition of Done Projet RPG : https://www.canva.com/design/DAGWj7DGYlI/lKhDWMzfCTTZfpBwUh-WIA/watch

SPRINT 1:

Sprint Goal:
Un RPG en console
2 équipes de personnages
Mécaniques de base de combat
Tour par tour
Système de HP
Attaques aléatoires
Ordre d’attaque basé sur la vitesse 

Développement: X fini - pas fini

Créer la structure de base du jeu en console
Tâche 1 : Mettre en place l'environnement de développement X
Tâche 2 : Créer la boucle principale du jeu X

Implémenter la création de deux équipes avec jusqu'à 10 personnages chacune
Tâche 1 : Développer la classe Personnage X
Tâche 2 : Créer la fonction de génération d'équipes X

Attribuer 100 HP à chaque personnage au début de la partie
Tâche 1 : Ajouter l'attribut HP à la classe Personnage -
Tâche 2 : Initialiser les HP lors de la création des personnages X

Implémenter le système de tour par tour basé sur le score de vitesse
Tâche 1 : Ajouter l'attribut vitesse aux personnages X
Tâche 2 : Développer la fonction de tri des personnages par vitesse X
Tâche 3 : Implémenter la logique de tour par tour X

Développer le système d'attaque avec dégâts aléatoires (0-10 HP)
Tâche 1 : Créer la fonction d'attaque X
Tâche 2 : Implémenter le calcul de dégâts aléatoires X

Ajouter la logique de fin de partie (tous les personnages d'une équipe à 0 HP)
Tâche 1 : Développer la fonction de vérification de l'état de l'équipe X
Tâche 2 : Implémenter la condition de fin de partie X

Développer le système de ciblage aléatoire pour les attaques
Tâche 1 : Créer la fonction de sélection aléatoire de cible X
Tâche 2 : Intégrer le ciblage aléatoire dans la fonction d'attaque -

Afficher les résultats de chaque tour et l'état du jeu
Tâche 1 : Développer les fonctions d'affichage pour chaque action X
Tâche 2 : Implémenter l'affichage de l'état du jeu après chaque tour X


FeedBack Client:
Améliorer le système de gestion des points de vie (HP) du RPG en console en intégrant un facteur d’endurance pour déterminer les HP initiaux des personnages.
Assurer un affichage constant des HP à chaque étape du jeu et empêche que les HP descendent en dessous de zéro.


SPRINT 2:
Sprint Goal:
Améliorer le prototype du RPG en console en intégrant un système de combat plus détaillé et configurable.
Ce sprint se concentrera sur l’affichage des HP à chaque étape.
L’ajout d’un attribut de force pour influencer les dégâts.
La diversification des HP initiaux basés sur l’endurance, l’implémentation d’un nouveau système de ciblage.
Utilisation d’un système de dés pour les actions aléatoires.
Nous préparons le terrain pour supporter plus de 2 équipes.

- Implémentation du système d'HP basé sur l'endurance
- Affichage des HP à chaque étape
- Prévention des HP négatifs


SPRINT 3:
Sprint Goal:
Résoudre les bugs et les anomalies rencontrés en priorité. Avant de pouvoir implémenter de nouvelles features, principalement l'affichage "est mort" lorsqu'un personnage passe à 0hp, implémenter un système d'endurance pour les personnages ou encore implémenter la logique de lancer de dés pour les attaques, dégâts, etc.

- Prévention des HP négatifs
- Implémentation d'une logique de lancer de dés pour les attaques, dégâts, etc.
- Implémentation du système d'HP basé sur l'endurance

SPRINT 4:
- Ajout d'un complément d'information pour le lancé de dé, le total du dé
- Implémentation du système d'HP basé sur l'endurance
- Implémentation du système de "tank"
- Ordre a suivre pour les attaquants

SPRINT 5:
- Amélioration endurance (stamina)
- Amélioration système tank
- Review de code, amélioration

Futur Développement:

Préparation pour support multi-équipes
Tâche 1 : Modifier la structure du jeu pour permettre plus de deux équipes
Tâche 2 : Créer une classe ou une structure de gestion des équipes
Tâche 3 : Adapter les mécaniques de tour et de combat pour multi-équipes

Amélioration du système de ciblage
Tâche 1 : Développer un algorithme de ciblage basé sur les HP les plus bas
Tâche 2 : Implémenter une alternative au ciblage aléatoire
Tâche 3 : Ajouter de la flexibilité dans le choix des cibles

Système de force et dégâts
Tâche 1 : Ajouter un attribut de force à la classe Personnage
Tâche 2 : Créer un mécanisme de calcul des dégâts incluant la force
Tâche 3 : Intégrer la force dans le système d'attaque

Créer un système d'équipement :
Tâche 1 : Implémenter des classes pour les armes et les armures
Tâche 2 : Créer une variété d'armes avec différentes statistiques d'attaque
Tâche 3 : Créer une variété d'armures avec différentes statistiques de défense 
Tâche 4 : Implémenter un système pour équiper les personnages avec des armes et des armures

Modifier le calcul de la vitesse des personnages :
Tâche 1 : Prendre en compte le poids de l'équipement
Tâche 2 : Ajuster la vitesse en fonction de la charge totale