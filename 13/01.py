# try except block 

try:
    age = int(input("enter your age : "))
except ValueError:
    print("you have typed an invalid number")

if age >=18:
    print("you can drive")
else:
    print("you cannot drive")