import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # If the score is over 21 and there's an 11, change it to 1 (Ace logic)
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(user_score, comp_score):
    if user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Computer went over. You win 😁"
    elif user_score == comp_score:
        return "Draw 🙃"
    elif user_score == 21:
        return "Blackjack! You win 😎"
    elif comp_score == 21:
        return "Computer has Blackjack. You lose 😤"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😢"

def blackjack_game():
    print("Welcome to Blackjack!")
    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 21 or comp_score == 21 or user_score > 21:
            game_over = True
        else:
            user_should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn: draw until reaching 17 or more
    while calculate_score(comp_cards) < 17:
        comp_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

# Main game entry point
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    blackjack_game()
