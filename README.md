# 2048 Command-Line Game

This project is a Python version of the game **2048**. The game board is shown in the command line, and moves are controlled with the keyboard using a small Pygame window.

## Project Files

- `main.py` - Starts the game, handles keyboard input, and prints the board.
- `board.py` - Contains the `Board` class and the game logic for moving, merging, spawning tiles, and checking for game over.

## Requirements

- Python 3
- Pygame

Install Pygame with:

```bash
pip install pygame
```

## How to Run

Open a terminal in this project folder, then run:

```bash
python main.py
```

When the game starts, a Pygame window will open. Keep that window selected so the game can read your keyboard input. The 2048 board will print in the terminal after each successful move.

## Controls

- `W` - Move tiles up
- `A` - Move tiles left
- `S` - Move tiles down
- `D` - Move tiles right
- Close the Pygame window to quit

## How to Play

The goal of 2048 is to combine matching numbered tiles to make larger values. Each move slides all tiles in one direction. When two tiles with the same number collide, they merge into one tile with double the value.

After every successful move, a new tile appears on the board. The game ends when there are no legal moves left.

