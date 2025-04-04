# pizza pricing

print("Welcome to the pizza shop")

size = input("What is the size of your pizza? S , M , L : ")
paperroni = input("do you want paperroni on your pizza? Y , N : ")
cheese = input("do you want extra cheese on your pizza? Y , N : ")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("you have typed wrong inputs")

if paperroni == 'Y':
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == 'Y':
    bill += 1
    

print(f"Your total bill is {bill}")