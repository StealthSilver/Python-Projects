# Higher Lower Game

import data 
import random

print("Welcome to higher lower game \n")

a = random.randint(0,20)
b = random.randint(0,20)

first = data.game_data[a]["name"]
second = data.game_data[b]["name"]

first_d = data.game_data[a]["description"]
second_d = data.game_data[b]["description"]

first_f = data.game_data[a]["followers"]
second_f = data.game_data[b]["followers"]

print(f"Compare A : {first}, {first_d} \n")
print(f"Against B : {second}, {second_d} \n")

user = input("Who has more followers? Type 'A' or 'B' : ").upper()

score = 0
game = True 


while game:
    if user == "A" and first_f > second_f:
        print(f"you won, {first} has {first_f} followers and {second} has {second_f} followers")
        score += 1
    elif user == "B" and first_f < second_f:
        print(f"you won, {first} has {first_f} followers and {second} has {second_f} followers")
        score += 1
    else:
        print("You Lost")
        print(score)
        game = False
