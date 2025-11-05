# snake_backend/grid.py
import random

class Grid:
    def __init__(self, n, shuffle=True):
        self.n = n
        values = list(range(1, n * n + 1))
        if shuffle:
            random.shuffle(values)
        self.grid = [values[i * n:(i + 1) * n] for i in range(n)]
        self.r = {}
        self.c = {}
        for i in range(n):
            for j in range(n):
                v = self.grid[i][j]
                self.r[v] = i
                self.c[v] = j

    def get_value(self, x, y):
        return self.grid[x][y]

    def print_grid(self):
        for row in self.grid:
            print(row)
