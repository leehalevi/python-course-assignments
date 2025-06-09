from game_logic import *


def main():
    while True:
        number = random_number()
        debug = False
        changing_game = False

        current_game = game(number, debug, changing_game)
        if current_game == 'game_over':
            break
        elif current_game == 'new_game':
            print("---Starting new game!---")
            continue


if __name__ == "__main__":
    main()