import random

# List of words to guess
words = ["python", "hangman", "programming", "developer", "computer"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = set()
attempts_left = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

while attempts_left > 0:
    # Display the word with blanks
    print(HANGMAN_PICS[6 - attempts_left])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print(f"Attempts left: {attempts_left}")
    print("Guessed letters:", " ".join(sorted(guessed_letters)))

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word!")
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Check guess
    if guess not in secret_word:
        attempts_left -= 1
        print("❌ Wrong guess!")

# Game over
if attempts_left == 0:
    print("\n💀 Game Over! The word was:", secret_word)
