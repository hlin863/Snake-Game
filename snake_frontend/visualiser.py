import pygame
import sys
import time
from snake_backend.engine import SnakeEngine

# Colour constants
WHITE = (240, 240, 240)
BLACK = (10, 10, 10)
GREEN = (50, 205, 50)
BLUE = (70, 130, 180)
RED = (220, 20, 60)
GRAY = (200, 200, 200)

CELL_SIZE = 60
MARGIN = 2
FPS = 2  # ticks per second

def draw_grid(screen, engine, n):
    for i in range(n):
        for j in range(n):
            val = engine.grid.get_value(i, j)
            pygame.draw.rect(
                screen,
                GRAY,
                (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN),
            )
            # Draw value number
            font = pygame.font.SysFont(None, 24)
            img = font.render(str(val), True, BLACK)
            screen.blit(img, (j * CELL_SIZE + 20, i * CELL_SIZE + 20))

def draw_snakes(screen, engine):
    for l, snake in engine.snakes.items():
        colour = BLUE if l == 1 else (RED if l % 2 == 0 else GREEN)
        for (x, y) in snake.body:
            pygame.draw.rect(
                screen,
                colour,
                (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN),
            )

def run_visualisation(n=5):
    pygame.init()
    engine = SnakeEngine(n)
    screen = pygame.display.set_mode((CELL_SIZE * n, CELL_SIZE * n))
    pygame.display.set_caption("Snake Simulation")
    clock = pygame.time.Clock()

    T = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(screen, engine, n)
        draw_snakes(screen, engine)

        pygame.display.flip()
        clock.tick(FPS)
        time.sleep(0.5)

        engine.tick()
        T += 1
        if T > 2 * n:
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_visualisation()