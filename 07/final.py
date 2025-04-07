# Hangman game

import random

fruits = ['APPLE' , 'BANANA' , 'ORANGE' , 'MANGO' , 'GRAPES' , 'PINEAPPLE' , "STRAWBERRY"]

chosen_word = random.choice(fruits)
print(chosen_word)

placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

game_over = False 

while not game_over:
    
    guess = input("Guess a letter : ").upper()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
        else: 
            display += "_"

    print(display)