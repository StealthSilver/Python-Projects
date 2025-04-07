import random

# List of possible words
fruits = ['APPLE', 'BANANA', 'ORANGE', 'MANGO', 'GRAPES', 'PINEAPPLE', 'STRAWBERRY']
chosen_word = random.choice(fruits)

lives = 6
guessed_letters = set()
correct_letters = set()
word_display = ['_' for _ in chosen_word]

print("Welcome to Hangman!")
print(" ".join(word_display))


while lives > 0 and '_' in word_display:
    guess = input("Guess a letter: ").upper()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid alphabet letter.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        print("Correct!")
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} {'life' if lives == 1 else 'lives'} left.")

    print(" ".join(word_display))


if '_' not in word_display:
    print("Congratulations! You guessed the word!")
else:
    print(f"Game Over! The word was '{chosen_word}'.")
