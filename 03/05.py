# pizza pricing

print("Welcome to the pizza shop")

size = input("What is the size of your pizza? S , M , L : ")
paperroni = input("do you want paperroni on your pizza? Y , N : ")
cheese = input("do you want extra cheese on your pizza? Y , N : ")

bill = 0


if cheese == 'Y':
    bill += 1
    if size == 'S':
        bill = 15
        if paperroni == 'Y':
            bill += 2
    elif size == 'M':
        bill = 20
        if paperroni == 'Y':
            bill += 3
    else:
        bill = 25
        if paperroni == 'Y':
            bill += 3

print(f"Your total bill is {bill}")