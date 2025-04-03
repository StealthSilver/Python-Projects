# Tip calculator

print("Welcome to the tip calculator")

bill = int(input("what was the total bill? $"))
tip = int(input("Huw mush tip woult you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total = str((((bill / 100) * tip) / people))

print("Each person should pay: $" + total)