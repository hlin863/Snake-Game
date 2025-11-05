let interval = null;

async function fetchState() {
    const res = await fetch("/state");
    const data = await res.json();
    renderBoard(data);
}

function renderBoard(data) {
    const board = document.getElementById("board");
    board.innerHTML = "";
    const grid = data.grid;
    const snakes = data.snakes;
    const n = grid.length;

    // build base grid
    board.style.gridTemplateColumns = `repeat(${n}, 60px)`;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const cell = document.createElement("div");
            cell.classList.add("cell");
            cell.textContent = grid[i][j];

            // check if any snake covers this cell
            for (const [key, body] of Object.entries(snakes)) {
                for (const [x, y] of body) {
                    if (x === i && y === j) {
                        cell.classList.add(`snake-${key}`);
                    }
                }
            }

            board.appendChild(cell);
        }
    }

    document.getElementById("statusText").textContent = data.running
        ? `Running... (T = ${data.T})`
        : `Paused at T = ${data.T}`;
}

document.getElementById("startBtn").addEventListener("click", async () => {
    await fetch("/start");
    if (!interval) interval = setInterval(fetchState, 500);
});

document.getElementById("pauseBtn").addEventListener("click", async () => {
    await fetch("/pause");
});

document.getElementById("resetBtn").addEventListener("click", async () => {
    await fetch("/reset");
    clearInterval(interval);
    interval = null;
    fetchState();
});

fetchState();