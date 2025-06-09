from controls import *

def game(number, debug, changing_game):
    while True:
        result = higher_or_lower(number, debug, changing_game)

        if result == True or result == 'game_over':
            return 'game_over'
        elif result == 'debug':
            debug = not debug
        elif result == 'changing_game':
            changing_game = not changing_game
        elif result == False:
            if changing_game:
                change = random.randint(-2, 2)
                number += change
                number = max(0, min(20, number))
        elif result == 'new_game':
            return 'new_game'