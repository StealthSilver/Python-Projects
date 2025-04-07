import random

fruits = ['APPLE' , 'BANANA' , 'ORANGE' , 'MANGO' , 'GRAPES']

chosen_word = random.choice(fruits)
print(chosen_word)

guess = input("Guess a letter : ").upper()


for letter in chosen_word:
    if letter == guess:
        print("right")
    else: 
        print("wrong")