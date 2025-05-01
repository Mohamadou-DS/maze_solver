import time
from maze import Maze
from bfs import bfs
from dfs import dfs

def compare(maze_grid):
    maze = Maze(maze_grid)

    start = time.time()
    path_bfs, visited_bfs = bfs(maze)
    t_bfs = time.time() - start

    start = time.time()
    path_dfs, visited_dfs = dfs(maze)
    t_dfs = time.time() - start

    print("Algorithm | Time (s) | Visited | Path length")
    print(f"BFS       | {t_bfs:.6f}   | {len(visited_bfs)}    | {len(path_bfs)}")
    print(f"DFS       | {t_dfs:.6f}   | {len(visited_dfs)}    | {len(path_dfs)}")
