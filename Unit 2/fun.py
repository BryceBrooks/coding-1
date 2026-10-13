HTML_PAGE = r"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fifteen Puzzle</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            padding: 1rem;
            background: #f1f5f9;
            color: #0f172a;
            font: 16px/1.5 system-ui, sans-serif;
        }
        main { width: min(100%, 28rem); text-align: center; }
        h1 { margin: 0 0 .75rem; }
        #status { min-height: 1.5em; margin: .5rem 0; }
        #board {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: .5rem;
            width: 100%;
            aspect-ratio: 1;
            padding: .5rem;
            border-radius: 12px;
            background: #cbd5e1;
            touch-action: manipulation;
        }
        .tile {
            border: 0;
            border-radius: 8px;
            background: #2563eb;
            color: white;
            font: 700 clamp(1.25rem, 8vw, 2rem) system-ui, sans-serif;
            cursor: pointer;
        }
        .tile:hover:not(:disabled) { background: #1d4ed8; }
        .tile:focus-visible, #restart:focus-visible {
            outline: 3px solid #f59e0b;
            outline-offset: 2px;
        }
        .tile:disabled { cursor: default; }
        .empty { visibility: hidden; }
        #restart {
            margin-top: 1rem;
            padding: .65rem 1rem;
            border: 0;
            border-radius: 8px;
            background: #0f172a;
            color: white;
            font: inherit;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <main>
        <h1>Fifteen Puzzle</h1>
        <p id="status" aria-live="polite">Moves: 0</p>
        <div id="board" role="group" aria-label="Fifteen puzzle board"></div>
        <button id="restart" type="button">New game</button>
        <p>Use the arrow keys or select a tile next to the empty space.</p>
    </main>
    <script>
        (() => {
            const board = document.getElementById('board');
            const status = document.getElementById('status');
            const restart = document.getElementById('restart');
            const side = 4;
            const solved = Array.from({ length: side * side }, (_, i) => (i + 1) % 16);
            let tiles = [];
            let moves = 0;
            let complete = false;

            function neighbors(index) {
                const row = Math.floor(index / side);
                const col = index % side;
                return [
                    row > 0 ? index - side : -1,
                    col < side - 1 ? index + 1 : -1,
                    row < side - 1 ? index + side : -1,
                    col > 0 ? index - 1 : -1
                ].filter(i => i >= 0);
            }

            function render() {
                board.replaceChildren();
                tiles.forEach((value, index) => {
                    const button = document.createElement('button');
                    button.type = 'button';
                    button.className = value === 0 ? 'tile empty' : 'tile';
                    button.textContent = value || '';
                    button.setAttribute('aria-label', value ? `Tile ${value}` : 'Empty space');
                    button.disabled = complete || (value !== 0 && !neighbors(index).includes(tiles.indexOf(0)));
                    if (value === 0) button.setAttribute('aria-hidden', 'true');
                    button.addEventListener('click', () => move(index));
                    board.append(button);
                });
                status.textContent = complete ? `Solved in ${moves} moves!` : `Moves: ${moves}`;
            }

            function move(index) {
                const empty = tiles.indexOf(0);
                if (complete || !neighbors(empty).includes(index)) return;
                [tiles[index], tiles[empty]] = [tiles[empty], tiles[index]];
                moves += 1;
                complete = tiles.every((value, i) => value === solved[i]);
                render();
            }

            function newGame() {
                tiles = solved.slice();
                let previous = -1;
                // Shuffling through legal moves guarantees every board is solvable.
                for (let i = 0; i < 200; i += 1) {
                    const empty = tiles.indexOf(0);
                    const choices = neighbors(empty).filter(index => index !== previous);
                    const next = choices[Math.floor(Math.random() * choices.length)];
                    [tiles[empty], tiles[next]] = [tiles[next], tiles[empty]];
                    previous = empty;
                }
                moves = 0;
                complete = false;
                render();
            }

            document.addEventListener('keydown', event => {
                const empty = tiles.indexOf(0);
                const row = Math.floor(empty / side);
                const col = empty % side;
                const target = {
                    ArrowUp: row < side - 1 ? empty + side : -1,
                    ArrowDown: row > 0 ? empty - side : -1,
                    ArrowLeft: col < side - 1 ? empty + 1 : -1,
                    ArrowRight: col > 0 ? empty - 1 : -1
                }[event.key];
                if (target !== undefined && target >= 0) {
                    event.preventDefault();
                    move(target);
                }
            });

            restart.addEventListener('click', newGame);
            newGame();
        })();
    </script>
</body>
</html>"""