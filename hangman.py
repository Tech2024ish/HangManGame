"""
Hangman Game Implementation
Author: ISHIMWE Jean Claude (224010238)
"""
import random
import string
def load_words(filename='words.txt'):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
        return words
    except FileNotFoundError:
        return False
def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)
def get_guessed_word(secret_word, letters_guessed):
    return ' '.join(letter if letter in letters_guessed else '-' for letter in secret_word)
def get_available_letters(letters_guessed):
    return ','.join(sorted(set(string.ascii_lowercase) - letters_guessed))
def calculate_score(guesses_remaining, secret_word):
    return guesses_remaining * len(set(secret_word))
def play_hangman():
    words = load_words()
    if words == False:
        print("Error: File words.txt not found")
        return
    secret_word = random.choice(words).lower()
    guesses_remaining = 10
    warnings_remaining = 3
    letters_guessed = set()
    vowels = set('aeiou')
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    while guesses_remaining > 0:
        print("-" * 50)
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Warning: Invalid input! You have {warnings_remaining} warnings left.")
            else:
                guesses_remaining -= 1
                print("Warning: Invalid input! You have no warnings left, so you lose a guess.")
            continue
        if guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"You've already guessed that letter. You have {warnings_remaining} warnings left.")
            else:
                guesses_remaining -= 1
                print("You've already guessed that letter. You have no warnings left, so you lose a guess.")
            continue
        letters_guessed.add(guess)
        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            if guess in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
        if is_word_guessed(secret_word, letters_guessed):
            score = calculate_score(guesses_remaining, secret_word)
            print("-" * 50)
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {score}")
            return
    print("-" * 50)
    print(f"Sorry, you ran out of guesses. The word was {secret_word}")
play_hangman()
