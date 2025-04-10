# Number Guessing game

import random

print("Welcome to the numebr gussing game")
print("Computer chooses a number between 1 and 100")

game = True

guess = random.randint(0,100)
print(guess)


while game:
    user = int(input("guess a number between 1 and 100"))
    if user > guess:
        print("too high")
    elif user < guess:
        print("too low")
    else:
        print("you guessed the numebr you won")
        game = False