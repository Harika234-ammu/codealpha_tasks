import random

def hangman():
    # List of words
    words = ['welcome','to','python', 'hangman', 'programming', 'challenge', 'students','and','developer']
    word_to_guess = random.choice(words)
    guessed_word = ['_'] * len(word_to_guess)  # Hidden word
    attempts = 6  # Maximum incorrect guesses
    guessed_letters = set()  # Track guessed letters

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters: {' '.join(guessed_word)}")

    while attempts > 0:
        print(f"\nRemaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

        # Display current progress
        print("Word: " + ' '.join(guessed_word))

        # Check if the player has won
        if '_' not in guessed_word:
            print("\nCongratulations! You've guessed the word!")
            break
    else:
        print(f"\nYou're out of attempts! The word was: {word_to_guess}")

# Run the game
hangman()
