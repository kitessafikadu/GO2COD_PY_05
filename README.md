# Hangman Game

This is a simple Hangman game implemented in Python, created as part of my programming internship at [Go2Cod](https://go2cod.com.et/). 
In this classic word-guessing game, the player attempts to guess a secret word by suggesting letters within a limited number of tries.

## Features
- Randomly selects a word from a predefined list.
- Displays correctly guessed letters and tracks incorrect guesses.
- Limits the number of incorrect attempts before ending the game.
- Provides feedback on win or loss at the end of each game.

## How to Play
1. The game selects a secret word from a list.
2. The player guesses letters one at a time.
3. If the guessed letter is in the word, it is revealed in the correct position(s).
4. If the guessed letter is not in the word, an incorrect guess is recorded.
5. The player wins by guessing all letters in the word within the allowed attempts. The game ends if the player exceeds the maximum allowed incorrect guesses.
