import random

WORD_LIST = ["python", "hangman", "challenge", "programming", "developer"]

def get_random_word():
    return random.choice(WORD_LIST)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word by entering one letter at a time.")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue
        elif guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word '{word}' correctly.")
                break
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was '{word}'.")

hangman()
