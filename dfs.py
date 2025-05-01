import sys
sys.setrecursionlimit(10000)

def dfs(maze):
    start, goal = maze.start, maze.goal
    visited_order = []
    came_from = {start: None}
    found = False

    def explore(u):
        nonlocal found
        if found:
            return
        visited_order.append(u)
        if u == goal:
            found = True
            return
        for nxt in maze.neighbors(u):
            if nxt not in came_from:
                came_from[nxt] = u
                explore(nxt)
 
    explore(start)

    # reconstruct path
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = came_from.get(cur)
    path.reverse()
    return path, visited_order
