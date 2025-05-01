import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time
import numpy as np

COLORS = { 
    'empty': 'white',
    'wall': 'black',
    'path': 'lightgreen',
    'visited': 'lightgray',
    'start': 'blue',
    'goal': 'orange'
}

# Ordre utilisé pour la palette
color_order = ['empty', 'wall', 'path', 'visited', 'start', 'goal']
code_to_index = {name: i for i, name in enumerate(color_order)}
cmap = mcolors.ListedColormap([COLORS[name] for name in color_order])

def draw_step(ax, maze, visited_cells=set(), path=[]):
    grid = maze.grid
    nrows, ncols = len(grid), len(grid[0])
    visual_grid = np.full((nrows, ncols), code_to_index['empty'])

    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 1:
                visual_grid[i][j] = code_to_index['wall']

    for i, j in visited_cells:
        if grid[i][j] == 0:
            visual_grid[i][j] = code_to_index['visited']

    for i, j in path:
        visual_grid[i][j] = code_to_index['path']

    si, sj = maze.start
    gi, gj = maze.goal
    visual_grid[si][sj] = code_to_index['start']
    visual_grid[gi][gj] = code_to_index['goal']

    ax.clear()
    ax.imshow(visual_grid, cmap=cmap)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Exploration + Chemin final\n")
    
    plt.pause(0.3)

def show_path(maze, path, visited_cells=None):
    visited_cells = visited_cells or []
    fig, ax = plt.subplots()
    for i in range(len(visited_cells)):
        draw_step(ax, maze, visited_cells[:i + 1], [])
    draw_step(ax, maze, visited_cells, path)
    plt.show()
