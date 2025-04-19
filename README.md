# Rock, Paper, Scissors Game

## Overview
This project is a command-line Rock, Paper, Scissors game written in Python, allowing users to play against the computer. It uses the `random` module to generate computer moves (`rock`, `paper`, `scissors`), tracks user and computer scores across rounds, and includes an exit confirmation prompt (`Y/N`).

## Features
- **Play Rounds**: Users can play by selecting `rock`, `paper`, or `scissors`, competing against the computer’s random move, with outcomes (win, lose, tie) displayed each round.
- **Score Tracking**: Tracks user and computer scores, as well as the current round number, updated after each round.
- **Random Computer Moves**: The computer’s move is randomly selected using `random.choice` from the list `['rock', 'paper', 'scissors']`.
- **Exit with Confirmation**: Users can exit the game with a confirmation prompt (`Y/N`) to confirm or return to the main menu.

## Setup
1. **Prerequisites**:
   - Python 3.6 or later (uses `random` module, which is built-in)
2. **Clone the Repository**:

## Usage
1. **Run the Program**:
- Execute the script in your terminal or command prompt:
  ```
  python rock_paper_scissors.py
  ```
2. **Interact with the Game**:
- The program displays: `Rock, Paper, Scissors Game` and prompts: `Insert '1' to start game, '2' to quit application:`
- **Play a Game**: Select `1` to start playing. Each round shows the current round number, user score, and computer score. Enter your move (e.g., `rock`, `paper`, or `scissors`). The computer randomly selects its move, and the outcome is displayed (e.g., `You win! Paper covers rock.`).
- **Quit the Game**: Select `2`, then confirm by typing `Y` (or `y`) to exit, or `N` (or `n`) to return to the main menu.
3. **View Screenshots**:
- Screenshots of the program in action (e.g., playing a round, quitting the game) are in the `screenshots/` folder.

## File Structure
- `rock_paper_scissors.py`: Python script containing the Rock, Paper, Scissors game.
- `README.md`: This file.

## Limitations
- **Command-Line Only**: The application runs in the terminal with no graphical user interface (GUI).
- **No Persistent Scores**: Scores and rounds reset when the program exits (no file or database storage).
- **Static Computer Move**: The computer’s move (`computer_selection`) is selected once at the start and doesn’t change during the game, reducing randomness per session.
- **Basic Error Handling**: Handles invalid move inputs (e.g., not `rock`, `paper`, or `scissors`), but does not validate non-numeric inputs for the main menu (e.g., entering `abc` instead of `1` or `2` causes a crash).

## Future Improvements
- Update the computer’s move to be randomly selected each round (e.g., call `get_random_string` inside the game loop).
- Add error handling for non-numeric inputs in the main menu to prevent crashes.
- Implement persistent storage (e.g., using JSON) to save scores between sessions.
- Add a feature to play a set number of rounds (e.g., best of 5) and declare a final winner.
