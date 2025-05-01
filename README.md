<!-- README.md -->
# Maze Solver

Ce projet implémente deux algorithmes de recherche (BFS et DFS) pour résoudre un labyrinthe et compare leurs performances.

## Installation

1. Clone le dépôt et place-toi dans le dossier :
   ```bash
   git clone <url>
   cd maze_solver
2. Créez un environnement virtuel et installez les dépendances :
    python -m venv venv
    source venv/bin/activate    # sous Linux/Mac
    venv\Scripts\activate       # sous Windows
    pip install matplotlib

3. Usage
Préparer un fichier texte maze.txtoù chaque caractère est 0(chemin), 1(mur), S(debut), G(but). Exemple :


S01 0
10101
00000
01110
000G1

Lance la résolution :
