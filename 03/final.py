# Treasure Island game

print("Welcome to the treasure Island \n Ypur mission is to find the treasure")

side = input("choose a side you wanna go L (left) , R (right) : ")



if side == 'R':
    print("Game over")
else:
    swim = input("Do you wanna (S) swim or (W) wait ? : ")
    if swim == 'S':
        print("Game over")
    else:
        door = input("Choose the color of the door Red (R) , Blue (B) , Green (G) : ")
        if door == 'R':
            print("Game over")
        elif door == 'B':
            print("Game over")
        else:
            print("You win")