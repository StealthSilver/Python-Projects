# nested conditional statement

height = int(input("enter your height in cm : "))
age = int(input("enter your age : "))

if height >= 130:
    if age <= 12:
        print("You need to pay $12")
    elif age <= 18:
        print("you need to pay $10") 
    else:
        print("you need to pay $7")
else:
    print("you cannot ride")