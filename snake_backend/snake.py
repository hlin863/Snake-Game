# snake_backend/snake.py
from collections import deque

class Snake:
    def __init__(self, length, n):
        self.length = length
        self.n = n
        self.body = deque([(0, i) for i in range(length)])  # start in top row
        self.time = 0
        self.path = [list(self.body)]

    def move(self):
        head_x, head_y = self.body[0]

        # Move downward first, then right, but stay within grid bounds
        if head_x < self.n - 1:
            new_head = (head_x + 1, head_y)
        elif head_y < self.n - 1:
            new_head = (head_x, head_y + 1)
        else:
            # Snake reached bottom-right corner → stop moving
            new_head = (head_x, head_y)

        self.body.appendleft(new_head)
        if len(self.body) > self.length:
            self.body.pop()
        self.time += 1
        self.path.append(list(self.body))

    def get_head(self):
        return self.body[0]