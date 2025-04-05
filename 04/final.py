# rock paper scissor game

import random

choices = {1: "Rock", 2: "Paper", 3: "Scissor"}


comp = random.randint(1, 3)


player = int(input("Enter 1 (Rock), 2 (Paper), 3 (Scissor): "))
   
print(f"You chose {choices[player]}")
print(f"Computer chose {choices[comp]}")

if comp == player:
    print("It's a tie! Try again.")
elif (player == 1 and comp == 3) or (player == 2 and comp == 1) or (player == 3 and comp == 2):
    print("You won!")
elif (player == 3 and comp == 1) or (player == 1 and comp == 2) or (player == 2 and comp == 3):
    print("Computer won!")
