import data
import random

print("Welcome to the Higher Lower Game!\n")

score = 0
game = True


def get_random_account(exclude=None):
    while True:
        account = random.choice(data.game_data)
        if account != exclude:
            return account

account_a = get_random_account()
account_b = get_random_account(exclude=account_a)

while game:
    print(f"Compare A: {account_a['name']}, {account_a['description']}")
    print("vs")
    print(f"Compare B: {account_b['name']}, {account_b['description']}\n")
    
    user = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_followers = account_a['followers']
    b_followers = account_b['followers']

    if (user == "A" and a_followers > b_followers) or (user == "B" and b_followers > a_followers):
        score += 1
        print(f"You won! Current score: {score}\n")

        
        if user == "A":
            account_b = get_random_account(exclude=account_a)
        else:
            account_a = account_b
            account_b = get_random_account(exclude=account_a)
    else:
        print(f"You lost! Final score: {score}")
        game = False
