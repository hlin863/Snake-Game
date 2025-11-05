from flask import Flask, render_template, jsonify
from snake_backend.engine import SnakeEngine

app = Flask(__name__)

engine = SnakeEngine(n=5)
T = 0
running = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/state")
def get_state():
    global T, running
    if running:
        engine.tick()
        T += 1
    grid_data = engine.grid.grid
    snakes_data = {l: list(snake.body) for l, snake in engine.snakes.items()}
    return jsonify({
        "T": T,
        "grid": grid_data,
        "snakes": snakes_data,
        "running": running
    })

@app.route("/start")
def start():
    global running
    running = True
    return jsonify({"status": "started"})

@app.route("/pause")
def pause():
    global running
    running = False
    return jsonify({"status": "paused"})

@app.route("/reset")
def reset():
    global engine, T, running
    engine = SnakeEngine(n=5)
    T = 0
    running = False
    return jsonify({"status": "reset"})

@app.route("/game")
def game():
    return render_template("snake_game.html")

if __name__ == "__main__":
    app.run(debug=True)