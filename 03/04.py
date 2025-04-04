# rollercoster with pic

height = int(input("Ente your height in cm : "))
bill = 0


if height >= 130:
    print("you can ride")
    age = int(input("enter your age : "))
    if age <= 12:
        bill = 5
        print("you need to pay $5")
    elif age <= 18:
        bill = 10
        print("you need to pay $10")
    else:
        bill = 12
        print("you need to pay $12")

    pic = input("do you want the pic Y , N : ")

    if pic == 'Y':
        bill += 3

    print(f"you need to pay ${bill}")

else:
    print("Sorry you cannot ride")