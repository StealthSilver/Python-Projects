# Python Generator 

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the password generator")

n_letters = int(input("enter the numebr of letters in your password \n"))
n_symbols = int(input("enter the numebr of symbols in your password \n"))
n_numbers = int(input("enter the numebr of numbers in your password \n"))


x = random.randint(1, len(letters))
y = random.randint(1, len(symbols))
z = random.randint(1, len(numbers))

password = ''

for num in range(1, n_letters + 1):
    for let in letters:
        password += letters[x]

for num in range(1, n_symbols + 1):
    for sym in symbols:
        password += symbols[y]

for num in range(1, n_numbers + 1):
    for number in numbers:
        password += numbers[z]

print(password)
