import random

print("Welcome to the number guessing game!")
print("Computer chooses a number between 1 and 100")

guess = random.randint(1, 100)


diff = input("Choose your difficulty 'e' (easy) or 'h' (hard): ").lower()

if diff == 'e':
    chances = 10
else:
    chances = 5

game = True

while game:
    for n in range(chances):
        print(f"\nYou have {chances - n} attempts remaining.")
        user = int(input("Guess a number between 1 and 100: "))

        if user > guess:
            print("Too high.")
        elif user < guess:
            print("Too low.")
        else:
            print(f"You guessed the number {guess}! You won 🎉")
            game = False
            break

    if game:  
        print(f"\nYou've run out of guesses. You lose 😢 The number was {guess}")
        game = False
