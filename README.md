# Pong Game

## Overview
This is a Python implementation of the classic Pong game. The game features a player paddle, an enemy paddle, and a ball that moves across the screen. The objective is to score points by hitting the ball past the enemy paddle.

## Features
- Player-controlled paddle.
- AI-controlled enemy paddle.
- Ball physics and collision detection.
- Score tracking.
- Customizable assets (images and fonts).

## Requirements
- Python 3.13 or higher.
- Pygame library.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ConnorKnoetze/Pong-Game-PyGame
   ```
2. Navigate to the project directory:
   ```bash
   cd pong
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```

## Usage
Run the game using the following command:
```bash
python main.py
```

## File Structure
- `main.py`: Entry point for the game.
- `game.py`: Contains the main game logic.
- `ball.py`: Handles ball behavior.
- `paddle.py`: Manages player paddle.
- `enemy_paddle.py`: Manages enemy paddle.
- `table.py`: Handles the game table.
- `text.py`: Manages score display.
- `images/`: Contains image assets.
- `fonts/`: Contains font assets.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Pygame library for game development.
- Classic Pong game for inspiration.
