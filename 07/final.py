import random

fruits = ['APPLE' , 'BANANA' , 'ORANGE' , 'MANGO' , 'GRAPES']

chosen_word = random.choice(fruits)
print(chosen_word)

placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

guess = input("Guess a letter : ").upper()


for letter in chosen_word:
    if letter == guess:
        print("right")
    else: 
        print("wrong")

