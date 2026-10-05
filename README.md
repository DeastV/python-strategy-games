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
  * **Easy (fácil):** Selects an empty cell adjacent to its own existing stones; if none exists, picks the first free cell prioritized by proximity to the board center.
  * **Normal (normal):** Evaluates lines of length $L \le k$ to either extend its own winning sequence or block the opponent from reaching $L$ consecutive stones.
  * **Hard (difícil):** Prioritizes immediate win/block opportunities, then performs full-game lookahead simulations (`tab_simulacao`) for candidate moves assuming alternating play under normal strategy, choosing the position leading to guaranteed victory or a draw.

### 2. Orbito Game Engine (`orbito/`)

A dynamic strategic board game featuring shifting concentric tracks:
* **The Orbito Mechanism:** After placing a stone, all concentric orbital rings shift by 1 position in the **counter-clockwise** direction, altering spatial alignments every turn.
* **Abstract Data Types (ADTs):** Designed around clear ADT boundaries:
  * `posicao`: Immutable coordinate pair handling alphanumeric conversions (`a1` to `d4`).
  * `pedra`: Immutable marker representations for Black (`X`), White (`O`), and Neutral (` `).
  * `tabuleiro`: Mutable matrix abstraction modified in-place across piece placements and orbital rotations.
* **Automated Opponent (AI):**
  * **Easy (fácil):** Anticipates the subsequent single orbital shift to position stones adjacent to its own pieces post-rotation.
  * **Normal (normal):** Evaluates two steps ahead (post-rotation board states) to seize immediate winning alignments or block opponent alignments.

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

## Author & Acknowledgments

* **David Vasques** ([@DeastV](https://github.com/DeastV))

Coursework projects developed for Fundamentos da Programação at Instituto Superior Técnico, Universidade de Lisboa.

*Course-Provided Specifications:* Game rules and interface specifications were formulated by the Fundamentos da Programação teaching staff. The MIT License applies to the implementation of data abstractions, heuristics, board transformation algorithms, and interactive game loops.
