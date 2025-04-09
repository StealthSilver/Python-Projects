# Blackjack 
import random 
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user = input("Do you want to play a game of Blackjack? type 'y' or 'n': " )

initial_cards = random.sample(cards, 2) 
print(initial_cards)
if user == 'y':
    print(f"your cards: {initial_cards}, current score: {score}")