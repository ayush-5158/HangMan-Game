# Hangman Game

A simple Hangman game implemented in Python where the player has 7 chances to guess a randomly selected word from a predefined list. 

## How to Play

1. The game selects a word at random from a list of possible words.
2. You start with 7 chances to guess the word correctly.
3. Each time you guess a letter:
   - If the letter is in the word, it fills in the corresponding blank(s).
   - If the letter is not in the word, you lose one chance.
4. The game continues until you either guess the word correctly or run out of chances.

## Features

- Random word selection.
- Feedback on correct and incorrect guesses.
- Countdown of remaining guesses.
- End-game messages indicating success or game over with the correct word displayed.

## Code Structure

- **List of Words**: The list of possible words for the game.
- **Random Word Selection**: Uses Python’s `random.choice()` function to pick a word.
- **Game Loop**: Runs until the player has guessed the word or used all their chances.
- **Input**: Prompts the player to enter a guessed letter each round.
- **Output**: Displays the word with correctly guessed letters revealed, remaining chances, and end-game messages.

## Requirements
Python 3.x

## To run the repository
git clone https://github.com/ayush-5158/HangMan-Game.git

## Run the script
python hangman.py

