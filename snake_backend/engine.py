# snake_backend/engine.py
from .grid import Grid
from .snake import Snake

class SnakeEngine:
    def __init__(self, n):
        self.grid = Grid(n)
        self.n = n
        self.snakes = {l: Snake(l, n) for l in range(1, n + 1)}

    def tick(self):
        for snake in self.snakes.values():
            if snake.time < 2 * self.n - 2:
                snake.move()

    def query(self, l, T):
        snake = self.snakes[l]
        while snake.time < T:
            snake.move()
        return max(self.grid.get_value(x, y) for x, y in snake.body)

    def print_state(self, T):
        for l, snake in self.snakes.items():
            if snake.time >= T:
                head = snake.get_head()
                print(f"Snake {l}: head={head}, max={self.query(l, T)}")