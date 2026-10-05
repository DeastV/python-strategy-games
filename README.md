# Python Board Game Engines — m,n,k & Orbito

[![Language](https://img.shields.io/badge/Language-Python%203-blue.svg)](https://www.python.org/)
[![Paradigm](https://img.shields.io/badge/Paradigm-Functional%20%26%20ADTs-orange.svg)]()
[![AI](https://img.shields.io/badge/AI-Heuristic%20Bot-green.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collection of terminal-based strategy board game engines and automated heuristic bots implemented in Python. The projects explore grid manipulation, abstract data type (ADT / TAD) formulation, functional programming patterns, and automated game heuristics.

Developed as part of the **Foundations of Programming (Fundamentos da Programação)** course at **Instituto Superior Técnico (IST), Universidade de Lisboa**.

---

## Games Included

### 1. The m,n,k Game Engine (`mnk_game/`)

A mathematical generalization of $k$-in-a-row alignment games played on an $m \times n$ rectangular board:
* **Configurable Board Rules:** Fully parametrized dimensions where $m$ is the row count, $n$ is the column count, and $k$ represents the consecutive alignment target required to win (generalizing Tic-Tac-Toe $3,3,3$, Gomoku $15,15,5$, and Connect Four variants).
* **Alignment Detection:** Efficient directional scanning algorithms validating horizontal, vertical, and diagonal win configurations.
* **Automated Opponent (AI):**
  * **Easy (fácil):** Selects random valid empty cells.
  * **Normal (normal):** Evaluates tactical opportunities to score an immediate win or block the opponent from winning on the subsequent turn.
  * **Hard (difícil):** Deeper positional evaluation prioritizing central cells, intercepting opponent sequences, and building dual-threat winning lines.

### 2. Orbito Game Engine (`orbito/`)

A dynamic strategic board game featuring shifting concentric tracks:
* **The Orbito Mechanism:** After placing a stone, the board's concentric orbital rings shift by 1 position (clockwise on outer track, counter-clockwise on inner track), altering spatial relationships every turn.
* **Abstract Data Types (ADTs):** Built strictly following functional programming specifications with immutable data structures:
  * `posicao`: Coordinate representation handling alphanumeric conversions (`a1` to `d4`).
  * `pedra`: Marker states representing Black (`X`), White (`O`), or Neutral (` `).
  * `tabuleiro`: Matrix abstraction handling validation, piece placement, and orbital shifts.
* **Game Modes:** 2-Player local match and Player vs. Computer with automated strategy.

---

## Project Structure

```
.
├── mnk_game/
│   └── mnk_game.py         # m,n,k game implementation and AI heuristics
├── orbito/
│   └── orbito.py           # Orbito engine, ADTs, and orbital shifting logic
├── LICENSE                 # MIT License
├── .gitignore              # Python exclusions
└── README.md               # Project documentation
```

---

## How to Play

No external dependencies are required beyond Python 3.

### Running m,n,k Game
```bash
python3 mnk_game/mnk_game.py
```
* Custom parameters can be invoked programmatically:
  ```python
  from mnk_game.mnk_game import jogo_mnk
  # Format: jogo_mnk((rows, columns, k_to_win), player_piece, difficulty)
  jogo_mnk((3, 3, 3), 1, "dificil")
  ```

### Running Orbito
```bash
python3 orbito/orbito.py
```
* Custom parameters can be invoked programmatically:
  ```python
  from orbito.orbito import orbito
  # Format: orbito(board_size_n, mode, player_piece)
  # n=2 creates a standard 4x4 grid (2 concentric orbits)
  orbito(2, "normal", "X")
  ```

---

## Author

* **David Vasques** ([@DeastV](https://github.com/DeastV))

*Instituto Superior Técnico — Universidade de Lisboa (2024/2025)*
