import matplotlib.pyplot as plt
import matplotlib.animation as animation

CELL_SIZE = 1
COLORS = {
    'wall': 'black',
    'empty': 'white',
    'visited': 'lightblue',
    'path': 'red',
    'start': 'green',
    'goal': 'gold'
}

def draw_step(ax, maze, visited, path):
    ax.clear()
    rows, cols = maze.rows, maze.cols
    for i in range(rows):
        for j in range(cols):
            cell = maze.grid[i][j]
            if (i, j) in path:
                color = COLORS['path']
            elif (i, j) == maze.start:
                color = COLORS['start']
            elif (i, j) == maze.goal:
                color = COLORS['goal']
            elif (i, j) in visited:
                color = COLORS['visited']
            elif cell == 1:
                color = COLORS['wall']
            else:
                color = COLORS['empty']
            rect = plt.Rectangle((j, rows-i-1), CELL_SIZE, CELL_SIZE, facecolor=color, edgecolor='gray')
            ax.add_patch(rect)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticks([])
    ax.set_yticks([])


def animate_search(maze, visited_order, path):
    fig, ax = plt.subplots()
    def update(frame):
        visited = visited_order[:frame]
        draw_step(ax, maze, visited, [])
    ani = animation.FuncAnimation(fig, update, frames=len(visited_order), interval=50)
    plt.show()


def show_path(maze, path, visited):
    fig, ax = plt.subplots()
    draw_step(ax, maze, visited, path)
    plt.show()
