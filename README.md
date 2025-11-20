[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ulo7n3dd)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17127886&assignment_repo_type=AssignmentRepo)

# Hangman Game Implementation

## Description

This is an implementation of the classic Hangman game in Python. The game randomly selects a word from a word list and allows the player to guess it one letter at a time.

## Features

- Random word selection from a word list file
- 10 initial guesses
- 3 warnings for invalid inputs
- Special rules for vowels (cost 2 guesses)
- Score calculation based on remaining guesses and unique letters
- Input validation and error handling

## How to Play

1. Run the game using Python 3:
   ```bash
   python3 hangman.py
   ```
2. Follow the on-screen prompts to guess letters
3. Try to guess the word before running out of guesses

## Game Rules

- Start with 10 guesses and 3 warnings
- Guessing a vowel incorrectly costs 2 guesses
- Guessing a consonant incorrectly costs 1 guess
- Invalid inputs or repeated guesses cost a warning (or a guess if no warnings remain)
- Win by guessing all letters before running out of guesses
