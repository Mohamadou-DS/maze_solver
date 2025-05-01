from collections import deque

def bfs(maze):
    start, goal = maze.start, maze.goal
    frontier = deque([start])
    came_from = {start: None}
    visited_order = []

    while frontier:
        current = frontier.popleft()
        visited_order.append(current)
        if current == goal:
            break
        for nxt in maze.neighbors(current):
            if nxt not in came_from:
                frontier.append(nxt)
                came_from[nxt] = current

    # reconstruct path
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = came_from.get(cur)
    path.reverse()
    return path, visited_order
