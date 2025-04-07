# Hangman game

import random

lives = 6

fruits = ['APPLE' , 'BANANA' , 'ORANGE' , 'MANGO' , 'GRAPES' , 'PINEAPPLE' , "STRAWBERRY"]

chosen_word = random.choice(fruits)


placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

game_over = False 

correct_letters = []

while not game_over:

    guess = input("Guess a letter : ").upper()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else: 
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True 
            print("Game over")

    if "_" not in display:
        game_over = True 
        print("You won")