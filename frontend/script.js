let pyodide;
let pythonGame;
let selectedSquare = null;
let boardFlipped = false;

// Dark Mode Logic
const themeToggleBtn = document.getElementById('theme-toggle');
const htmlElement = document.documentElement;
const sunIcon = document.getElementById('sun-icon');
const moonIcon = document.getElementById('moon-icon');

// Check for saved user preference, if any, on load (default to light mode)
const isDarkMode = localStorage.getItem('color-theme') === 'dark';
if (isDarkMode) {
    htmlElement.classList.add('dark');
} else {
    htmlElement.classList.remove('dark');
}

themeToggleBtn.addEventListener('click', function() {
    if (htmlElement.classList.contains('dark')) {
        htmlElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
    } else {
        htmlElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
    }
});

const pieceSymbols = {
    'white': {
        'King': '♔\uFE0E', 'Queen': '♕\uFE0E', 'Rook': '♖\uFE0E', 'Bishop': '♗\uFE0E', 'Knight': '♘\uFE0E', 'Pawn': '♟\uFE0E'
    },
    'black': {
        'King': '♚\uFE0E', 'Queen': '♛\uFE0E', 'Rook': '♜\uFE0E', 'Bishop': '♝\uFE0E', 'Knight': '♞\uFE0E', 'Pawn': '♟\uFE0E'
    }
};

async function initPyodide() {
    document.getElementById('status').innerText = "Initializing Pyodide...";
    pyodide = await loadPyodide();
    
    // Load Python files
    // In a real deployment, we'd fetch these. For now, we assume they are served at ../backend/
    const files = ['board.py', 'chess_piece.py', 'game.py', 'pieces.py'];
    
    for (const file of files) {
        try {
            const response = await fetch(`../backend/${file}?t=${new Date().getTime()}`);
            if (!response.ok) throw new Error(`Failed to fetch ${file}`);
            const content = await response.text();
            pyodide.FS.writeFile(file, content);
            console.log(`Loaded ${file}`);
        } catch (e) {
            console.error(e);
            document.getElementById('status').innerText = `Error loading ${file}`;
            return;
        }
    }

    // Import game
    await pyodide.runPythonAsync(`
        from game import Game
        game = Game()
    `);
    
    pythonGame = pyodide.globals.get('game');
    document.getElementById('status').innerText = "White's Turn";
    renderBoard();
}

function renderBoard() {
    const boardDiv = document.getElementById('chess-board');
    boardDiv.innerHTML = '';
    
    // Get state from Python
    // state is a list of rows (top to bottom: 7 to 0)
    // But our grid CSS fills row by row.
    // Python get_board_state returns rows from y=7 down to y=0.
    // So state[0] is row 7 (Black pieces), state[7] is row 0 (White pieces).
    const state = pythonGame.get_board_state().toJs();

    // Determine rendering order based on flip state
    const yRange = boardFlipped ? [7, 6, 5, 4, 3, 2, 1, 0] : [0, 1, 2, 3, 4, 5, 6, 7];
    const xRange = boardFlipped ? [7, 6, 5, 4, 3, 2, 1, 0] : [0, 1, 2, 3, 4, 5, 6, 7];

    for (let yi = 0; yi < 8; yi++) { 
        const y = yRange[yi];
        const row = state[y];
        for (let xi = 0; xi < 8; xi++) {
            const x = xRange[xi];
            const cellData = row[x];
            const square = document.createElement('div');
            square.className = `square ${(x + y) % 2 === 0 ? 'white-square' : 'black-square'}`;
            square.dataset.x = x;
            square.dataset.y = 7 - y; // Convert array index back to board coordinate
            
            if (cellData) {
                // cellData is a Map because it came from Python dict
                const type = cellData.get('type');
                const color = cellData.get('color');
                square.innerText = pieceSymbols[color][type];
                square.dataset.color = color;
            }
            
            if (selectedSquare && selectedSquare.x === x && selectedSquare.y === (7-y)) {
                square.classList.add('selected');
            }

            square.onclick = () => handleSquareClick(x, 7 - y);
            boardDiv.appendChild(square);
        }
    }
}

async function handleSquareClick(x, y) {
    if (!pythonGame) return;

    const currentTurn = pythonGame.turn; // Access property directly? Or need getter?
    // Pyodide proxies attributes.
    
    if (selectedSquare) {
        // Try to move
        const startX = selectedSquare.x;
        const startY = selectedSquare.y;
        
        if (startX === x && startY === y) {
            // Deselect
            selectedSquare = null;
            renderBoard();
            return;
        }

        // Call Python play_turn
        // play_turn takes tuples. In JS we pass arrays or use pyodide.toPy
        // play_turn((x1, y1), (x2, y2))
        
        try {
            const playerColor = pythonGame.turn;
            const responseProxy = pythonGame.play_turn([startX, startY], [x, y]);
            let response;
            if (responseProxy && typeof responseProxy.toJs === 'function') {
                response = responseProxy.toJs();
            } else {
                console.warn("play_turn returned unexpected type:", responseProxy);
                response = new Map();
                response.set('success', !!responseProxy);
                response.set('message', "Unexpected response from game engine");
            }

            const success = response.get('success');
            const message = response.get('message');
            const captured = response.get('captured');
            const isCheck = response.get('is_check');
            const isCheckmate = response.get('is_checkmate');
            const winner = response.get('winner');
            
            if (responseProxy && typeof responseProxy.destroy === 'function') {
                responseProxy.destroy();
            }

            if (success) {
                const player = playerColor.charAt(0).toUpperCase() + playerColor.slice(1);
                log(`${player} moved from (${startX},${startY}) to (${x},${y})`);
                
                if (captured) {
                    log(`Captured ${captured}!`);
                }
                
                if (message && message !== "Move successful") {
                    log(message);
                }

                selectedSquare = null;
                const statusEl = document.getElementById('status');
                
                if (isCheckmate) {
                    statusEl.innerText = `Checkmate! ${winner} wins!`;
                } else if (isCheck) {
                    statusEl.innerText = `${pythonGame.turn.charAt(0).toUpperCase() + pythonGame.turn.slice(1)}'s turn (Check!)`;
                } else {
                    statusEl.innerText = `${pythonGame.turn.charAt(0).toUpperCase() + pythonGame.turn.slice(1)}'s turn`;
                }
                
                statusEl.classList.add('highlight');
                setTimeout(() => statusEl.classList.remove('highlight'), 500);
            } else {
                log(message || "Invalid move");
                selectedSquare = null; 
            }
        } catch (e) {
            console.error(e);
            log("Error executing move");
        }
        renderBoard();
    } else {
        // Select piece
        // Check if there is a piece at x,y and it matches turn
        // We can check the DOM for simplicity since we rendered it
        // Or ask Python.
        // Let's ask Python via get_piece_at or just check board state
        // But we have the state in renderBoard.
        // Let's just try to select.
        
        // We can check if the square has a piece of current color
        // But we don't have easy access to the piece info here without re-fetching state.
        // Let's just set selected and let the move fail later if invalid?
        // Better UX: only select if valid.
        
        // Let's fetch piece at position
        const piece = pythonGame.board.get_piece_at([x, y]);
        if (piece) {
             if (piece.color === pythonGame.turn) {
                 selectedSquare = {x, y};
                 renderBoard();
             } else {
                 log("Not your turn / Opponent piece");
             }
        }
    }
}

function log(msg) {
    const logDiv = document.getElementById('log');
    logDiv.innerHTML += `<div>${msg}</div>`;
    logDiv.scrollTop = logDiv.scrollHeight;
}

function resetGame() {
    if (pythonGame) {
        pyodide.runPython("game = Game()");
        pythonGame = pyodide.globals.get('game');
        selectedSquare = null;
        document.getElementById('status').innerText = "White's Turn";
        renderBoard();
        log("Game reset");
    }
}

function flipBoard() {
    boardFlipped = !boardFlipped;
    renderBoard();
    log(`Board ${boardFlipped ? 'flipped to black\'s perspective' : 'reset to white\'s perspective'}`);
}

window.onload = initPyodide;
