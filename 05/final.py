# Random password generator

import random

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

print("Welcome to the password generator")

n_letters = int(input("Enter the number of letters in your password: "))
n_symbols = int(input("Enter the number of symbols in your password: "))
n_numbers = int(input("Enter the number of numbers in your password: "))

password_chars = []

for _ in range(n_letters):
    password_chars.append(random.choice(letters))

for _ in range(n_symbols):
    password_chars.append(random.choice(symbols))

for _ in range(n_numbers):
    password_chars.append(random.choice(numbers))

random.shuffle(password_chars)

password = ''.join(password_chars)

print(f"Your generated password is: {password}")
