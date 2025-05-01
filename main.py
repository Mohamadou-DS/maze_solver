import argparse
from maze import Maze
from bfs import bfs
from dfs import dfs
from visualizer import animate_search, show_path
from compare import compare

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Maze Solver")
    parser.add_argument('file', help="Path to maze file (python list format)")
    parser.add_argument('--algo', choices=['bfs','dfs','compare'], default='compare')
    parser.add_argument('--visual', action='store_true', help="Show visualization")
    args = parser.parse_args()

    # load grid
    maze_grid = eval(open(args.file).read())
    maze = Maze(maze_grid)

    if args.algo == 'bfs':
        path, visited = bfs(maze)
    elif args.algo == 'dfs':
        path, visited = dfs(maze)
    else:
        compare(maze_grid)
        exit(0)

    print(f"Visited: {len(visited)}, Path length: {len(path)}")
    if args.visual:
        animate_search(maze, visited, path)
        show_path(maze, path, visited)
