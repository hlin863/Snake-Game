# snake_backend/main.py
from snake_backend.engine import SnakeEngine

def main():
    n = 5
    engine = SnakeEngine(n)
    engine.grid.print_grid()
    print("\n--- Simulation Start ---\n")

    # simulate time steps
    for T in range(1, 2 * n):
        print(f"Time T = {T}")
        for l in range(1, n + 1):
            val = engine.query(l, T)
            print(f"Snake length {l}: max value = {val}")
        engine.tick()
        print()

if __name__ == "__main__":
    main()
