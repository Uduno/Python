# Antichess Simulation - Python

Ce projet est une implémentation du jeu **Antichess**, avec un moteur de simulation permettant à différentes IA de s'affronter. Antichess est une variante des échecs où le but est de perdre toutes ses pièces. L'algorithme de simulation prend en charge plusieurs IA et permet de jouer sur un échiquier de taille **6x6** ou **8x8**.

## Objectif du projet

- Simuler des parties d'**Antichess** entre plusieurs IA.
- Permettre l'utilisation de différents algorithmes pour les IA, avec la possibilité de comparer leurs performances.

## Intelligence Artificielle

Le projet inclut les algorithmes suivants pour les IA :

1. **Random** : L'IA effectue des mouvements aléatoires.
2. **Minimax** : L'algorithme Minimax est utilisé pour choisir les meilleurs mouvements.
3. **Alpha-Beta** : Optimisation du Minimax avec élagage Alpha-Beta pour réduire la recherche d'espace.
4. **MCTS** (Monte Carlo Tree Search) : Algorithme de recherche arborescente basé sur des simulations aléatoires pour prendre des décisions.

## Fonctionnalités

- **Échiquier 6x6 ou 8x8** : Les simulations peuvent être réalisées sur deux tailles d'échiquier différentes.
- **Simulation d'IA contre IA** : Le moteur permet de faire jouer les différentes IA entre elles.
- **Comparaison des stratégies** : Les résultats des simulations peuvent être utilisés pour comparer la performance des IA.

## Prérequis

Assurez-vous d'avoir installé les librairies suivantes avant d'exécuter le projet :

- **Python 3.x** (version recommandée)
- **pygame** : Pour afficher l'échiquier et visualiser les parties.
- **time** : Gestion du temps dans certaines fonctions.
- **random** : Utilisé pour l'algorithme d'IA Random et dans MCTS.

### Installation des dépendances

Pour installer les dépendances, exécutez la commande suivante :

```bash
pip install pygame
``` 

## Installation 
 
1. Clonez ce dépôt GitHub sur votre machine locale :
```bash
git clone https://github.com/votre-utilisateur/nom-du-repo.git
``` 

2. Accédez au dossier du projet :
```bash
cd nom-du-repo
``` 

3. Installez les dépendances du projet :
```bash
python main.py
``` 
 
## Comment jouer 

1. Choisissez la taille de l'échiquier (6x6 ou 8x8).
2. Sélectionnez le type d'IA que vous souhaitez faire jouer dans l'interface du programme.
3. Lancez une partie pour visualiser la simulation dans l'interface Pygame.

## Technologies Utilisées

- Python : Langage principal du projet.
- Pygame : Pour l'interface graphique et l'affichage du plateau de jeu.