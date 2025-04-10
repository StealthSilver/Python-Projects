player_health = 90

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    # can only be accesesed inside the game()
    drink_potion()


print(player_health)