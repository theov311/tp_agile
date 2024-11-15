Objectif: Divertir des joueurs avec un RPG automatique, lui permettant de choisir les paramètres des équipes qui s'affrontent

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

Développement: X fini - pas fini

Implémentation du système d'HP basé sur l'endurance
Tâche 1 : Ajouter un attribut d'endurance à la classe Personnage
Tâche 2 : Développer une formule pour calculer les HP initiaux basés sur l'endurance
Tâche 3 : Modifier la création des personnages pour intégrer l'endurance et les HP calculés

Affichage des HP à chaque étape
Tâche 1 : Créer une fonction d'affichage des HP pour chaque personnage
Tâche 2 : Intégrer l'affichage des HP après chaque action dans le tour de jeu
Tâche 3 : Formater l'affichage pour une meilleure lisibilité

Prévention des HP négatifs
Tâche 1 : Modifier la fonction de calcul des dégâts pour empêcher les HP de descendre en dessous de zéro
Tâche 2 : Implémenter une vérification des HP après chaque attaque
Tâche 3 : Ajouter une logique pour gérer les personnages avec 0 HP (hors combat)





Futur Développement:
Système de force et dégâts
Tâche 1 : Ajouter un attribut de force à la classe Personnage
Tâche 2 : Créer un mécanisme de calcul des dégâts incluant la force
Tâche 3 : Intégrer la force dans le système d'attaque

Amélioration du système de ciblage
Tâche 1 : Développer un algorithme de ciblage basé sur les HP les plus bas
Tâche 2 : Implémenter une alternative au ciblage aléatoire
Tâche 3 : Ajouter de la flexibilité dans le choix des cibles

Système de dés pour actions aléatoires
Tâche 1 : Créer une fonction de lancer de dés
Tâche 2 : Remplacer le système aléatoire actuel par le système de dés
Tâche 3 : Intégrer le système de dés dans les mécaniques de combat

Préparation pour support multi-équipes
Tâche 1 : Modifier la structure du jeu pour permettre plus de deux équipes
Tâche 2 : Créer une classe ou une structure de gestion des équipes
Tâche 3 : Adapter les mécaniques de tour et de combat pour multi-équipes
