from flask import Flask, render_template, request, jsonify
import json, os
from snake_backend.engine import SnakeEngine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)
DATA_FILE = os.path.join(str(app.static_folder), "Data", "Game_Results.json")

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

@app.route("/save_result", methods=["POST"])
def save_result():
    data = request.get_json()
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    try:
        results = json.load(open(DATA_FILE))
    except FileNotFoundError:
        results = []
    results.append(data)
    with open(DATA_FILE, "w") as f:
        json.dump(results, f, indent=2)
    return jsonify({"status": "saved"})

@app.route("/game")
def game():
    return render_template("snake_game.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")