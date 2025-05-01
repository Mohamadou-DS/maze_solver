class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = None
        self.goal = None
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 'S':
                    self.start = (i, j)
                elif grid[i][j] == 'G':
                    self.goal = (i, j)

    def in_bounds(self, pos):
        i, j = pos
        return 0 <= i < self.rows and 0 <= j < self.cols

    def passable(self, pos):
        i, j = pos
        return self.grid[i][j] != 1

    def neighbors(self, pos):
        i, j = pos
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            nxt = (i+di, j+dj)
            if self.in_bounds(nxt) and self.passable(nxt):
                yield nxt
