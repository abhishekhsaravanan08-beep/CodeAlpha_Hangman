import random

# List of predefined words
words = ["python", "computer", "apple", "school", "engineer"]

# Choose a random word
word = random.choice(words)

# Display word with underscores
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

incorrect_guesses = 0
max_attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)