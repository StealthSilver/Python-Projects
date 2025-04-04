# nested conditional statement

height = int(input("enter your height"))
age = int(input("enter your age"))

if height >= 130:
    if age >= 7:
        print("You need to pay $12")
    else:
        print("you need to pay $7")
else:
    print("you cannot ride")