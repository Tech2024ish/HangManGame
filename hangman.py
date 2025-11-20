import random
import string

# Load words from file
def load_words(filename="words.txt"):
    with open(filename, "r") as f:
        words = f.read().split()
    return words

# Choose a random word
def choose_word(words):
    return random.choice(words)

# Display current guessed word
def get_display_word(secret_word, guessed_letters):
    return "".join([char if char in guessed_letters else "-" for char in secret_word])

# Check if the player has guessed all letters
def is_word_guessed(secret_word, guessed_letters):
    return all(char in guessed_letters for char in secret_word)

# Hangman game
def hangman():
    words = load_words()
    secret_word = choose_word(words).lower()
    guessed_letters = set()
    remaining_guesses = 10
    warnings = 3
    vowels = "aeiou"

    print("\nWelcome to Hangman!")
    print(f"The secret word has {len(secret_word)} letters: {get_display_word(secret_word, guessed_letters)}")

    while remaining_guesses > 0 and not is_word_guessed(secret_word, guessed_letters):
        print("\n------------")
        print(f"You have {remaining_guesses} guesses left.")
        print(f"Warnings left: {warnings}")
        available_letters = "".join([c for c in string.ascii_lowercase if c not in guessed_letters])
        print(f"Available letters: {available_letters}")

        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! That is not a valid letter. You have {warnings} warnings left.")
            else:
                remaining_guesses -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left, so you lose one guess.")
            continue

        if guess in guessed_letters:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings} warnings left.")
            else:
                remaining_guesses -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left, so you lose one guess.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess: {get_display_word(secret_word, guessed_letters)}")
        else:
            print(f"Oops! That letter is not in the word: {get_display_word(secret_word, guessed_letters)}")
            if guess in vowels:
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1

    print("\n------------")
    if is_word_guessed(secret_word, guessed_letters):
        unique_letters = len(set(secret_word))
        score = remaining_guesses * unique_letters
        print(f"Congratulations, you won! The word was '{secret_word}'.")
        print(f"Your score is: {score}\n")
    else:
        print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.\n")

# Run the game
if __name__ == "__main__":
    hangman()