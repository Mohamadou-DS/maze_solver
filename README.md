**`README.md`**

> **Résumé**  
> Ce projet implémente deux algorithmes de recherche (BFS et DFS) pour résoudre un labyrinthe représenté sous forme de grille, avec une **visualisation animée** du parcours et du chemin final. Vous pourrez comparer en direct le **nombre de cellules visitées**, le **temps d’exécution** et la **longueur du chemin** pour chaque algorithme.

---

## 🚀 Overview  
Un labyrinthe est modélisé par une matrice 2D (`0`=chemin, `1`=mur, `S`=start, `G`=goal). Le programme :  
1. Charge dynamiquement la grille depuis un fichier Python.  
2. Exécute **BFS** (recherche en largeur) ou **DFS** (recherche en profondeur).  
3. Affiche **en temps réel** l’animation des explorations (cells visit) et du résultat final, avec un encadré montrant le nombre de cellules visitées, le temps écoulé et la longueur du chemin.  
4. Compare automatiquement performances et qualité du chemin.

---

## ✨ Features  
- 🔍 **BFS & DFS** : implémentations garantissant respectivement optimalité (BFS) et rapidité (DFS)
- 🎨 **Visualisation animée** : cases visitées (gris), chemin final (vert clair), start (bleue), goal (or)    
- ⏱️ **Statistiques en direct** : affichage de  
  - nombre de cellules visitées,  
  - temps d’exécution,  
  - longueur du chemin.  
- 🧩 **Personnalisable** : palette de couleurs via un dictionnaire `COLORS` (mur, chemin, etc.)  

---

## 🛠️ Getting Started  

### Prerequisites  
- Python ≥ 3.7  
- `matplotlib`, `numpy`  

### Installation  
```bash
git clone https://github.com/<votre-utilisateur>/maze-solver.git
cd maze-solver
pip install -r requirements.txt
```  

## ▶️ Usage  
1. Préparez votre grille dans un fichier `my_maze.py` :  
   ```python
   maze = [
     ['S', 0, 1, 0],
     [0, 0, 0, 'G']
   ]
   ```  
2. Lancez la résolution :  
   ```bash
   python main.py my_maze.py --algo bfs --visual
   ```  
   - `--algo [bfs|dfs]` : choix de l’algorithme  
   - `--visual` : active l’animation et les statistiques en direct

---

## 📂 File Structure  
```
maze-solver/
├── maze.py          # classe Maze : représentation et voisins
├── bfs.py           # implémentation Breadth-First Search
├── dfs.py           # implémentation Depth-First Search
├── visualizer.py    # animation & affichage statistiques
├── main.py          # point d’entrée CLI
├── my_maze.py       # exemple de labyrinthe (à personnaliser)
├── requirements.txt # bibliothèques Python requises
└── README.md        # documentation du projet
```

## 📄 License  
Ce projet est sous licence **MIT**. Voir [LICENSE](LICENSE) pour plus de détails.


> *Merci d’avoir jeté un œil ! Toute suggestion d’amélioration est la bienvenue.*
