# **Revue du Projet RPG**  

## **Objectif**  
Divertir des joueurs avec un RPG automatique, leur permettant de configurer des équipes qui s’affrontent dans des combats épiques.  

👉 **Définition of Done** : [Consulter le document Canva](https://www.canva.com/design/DAGWj7DGYlI/lKhDWMzfCTTZfpBwUh-WIA/view?utm_content=DAGWj7DGYlI&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h140f5926d6)  

---

## **SPRINT 1 : Lancement du projet**  

### 🎯 **Sprint Goal**  
- Créer un RPG jouable en console.  
- Implémenter des fonctionnalités de base :  
  - Deux équipes de personnages.  
  - Système de combat tour par tour avec gestion des HP.  
  - Attaques aléatoires et ordre d’attaque basé sur la vitesse.  

---

### **Progrès du développement**  

#### **Création de la structure du jeu en console**  
- **Tâche 1** : Mettre en place l’environnement de développement ✔️  
- **Tâche 2** : Créer la boucle principale du jeu ✔️  

#### **Création des équipes**  
- **Tâche 1** : Développer la classe Personnage ✔️  
- **Tâche 2** : Générer deux équipes de 10 personnages maximum ✔️  

#### **Gestion des HP des personnages**  
- **Tâche 1** : Ajouter l’attribut HP à la classe Personnage ✔️  
- **Tâche 2** : Initialiser les HP à 100 pour chaque personnage ✔️  

#### **Combat tour par tour (basé sur la vitesse)**  
- **Tâche 1** : Ajouter l’attribut vitesse aux personnages ✔️  
- **Tâche 2** : Développer une fonction pour trier les personnages par vitesse ✔️  
- **Tâche 3** : Implémenter la logique de combat tour par tour ✔️  

#### **Système d’attaque et de ciblage**  
- **Tâche 1** : Créer une fonction d’attaque infligeant des dégâts aléatoires (0-10 HP) ✔️  
- **Tâche 2** : Développer un système de ciblage aléatoire ❌  

#### **Fin de partie et affichage**  
- **Tâche 1** : Vérifier l’état des équipes pour détecter la fin de partie ✔️  
- **Tâche 2** : Afficher les résultats de chaque tour et l’état du jeu ✔️  

---

### 💬 **Feedback client**  
Le client a proposé les améliorations suivantes :  
- Intégrer un facteur d’endurance pour déterminer les HP initiaux des personnages.  
- Afficher les HP à chaque étape du jeu.  
- Empêcher les HP de descendre en dessous de zéro.  

---

## **SPRINT 2 : Améliorations prévues**  

### 🎯 **Sprint Goal**  
Rendre le système de combat plus détaillé et configurable :  
- Système d’HP basé sur l’endurance.  
- Affichage des HP à chaque étape.  
- Prévention des HP négatifs.  
- Introduction d’un système de dés pour les actions aléatoires.  
- Préparer la structure pour supporter plus de deux équipes.  

---

## **SPRINT 3 : Résolution de bugs et nouvelles mécaniques**  

### 🎯 **Sprint Goal**  
Corriger les anomalies prioritaires avant d’ajouter des fonctionnalités :  
- Indiquer lorsqu’un personnage passe à 0 HP (« est mort »).  
- Ajouter la logique de lancer de dés pour les attaques et dégâts.  
- Finaliser le système d’HP basé sur l’endurance.  

---

## **SPRINTS FUTURS : Ce qui nous attend**  

### 🌟 **Sprint 4**  
- Ajouter un complément d’information pour le lancer de dés (afficher le total).  
- Introduire un système de « tank » (personnage résistant en première ligne).  
- Réviser l’ordre des attaquants.  

### 🌟 **Sprint 5**  
- Améliorer l’attribut d’endurance (stamina).  
- Optimiser le système de tank.  
- Effectuer une review de code pour améliorer la structure existante.  

---

## **Futurs développements envisagés**  

1. **Support multi-équipes**  
   - Permettre à plus de deux équipes de s’affronter.  
   - Adapter les mécaniques de tour et de combat.  

2. **Système de ciblage stratégique**  
   - Prioriser les cibles avec les HP les plus bas.  
   - Ajouter de la flexibilité dans le choix des cibles.  

3. **Ajout d’attributs influents**  
   - Introduire un attribut de force pour calculer les dégâts.  
   - Diversifier les HP initiaux selon les attributs.  

4. **Système d’équipement**  
   - Créer des armes et armures modifiant les statistiques des personnages.  
   - Intégrer un système d’équipement au gameplay.  

5. **Calcul avancé de la vitesse**  
   - Prendre en compte le poids de l’équipement.  
   - Ajuster la vitesse selon la charge totale.  

---

Un grand merci à tous pour votre engagement dans ce projet ! Ensemble, faisons de ce RPG une expérience inoubliable. 🎮✨