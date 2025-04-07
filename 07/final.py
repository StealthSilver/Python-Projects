import random

fruits = ['APPLE' , 'BANANA' , 'ORANGE' , 'MANGO' , 'GRAPES']

name = fruits[random.randint(1,4)]

guess = []

while(n <= 5):
    inp = input("ENTER THE FIRST LETTER : ")
    guess.append(inp)
    n += 1


if name == str(guess):
    print("won")
else:
    print("lost")