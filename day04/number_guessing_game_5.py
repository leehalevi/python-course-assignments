import random

def random_number():
    number = int(20 * random.random())
    return number


def higher_or_lower(number, debug=False, changing_game=False):
    print(f"The number is {number}") if debug else None
    if changing_game:
        print("Warning: The target number may change after each guess!")

    guess = input("Guess a number between 0 and 20: ")
    if guess == 'x':
        # Game ends
        print("Game over")
        return True
    if guess == 's':
        # Prints the number once and then ends
        print(f"The number is {number}")
        return False
    if guess == 'd':
        # Prints the number continuously throughout the game
        return 'debug'
    if guess == 'm':
        return 'changing_game'

    while not guess.isdigit() and guess not in ['x', 's', 'd', 'm']:
        print("Invalid input. Please enter a number between 0 and 20, or a valid controller letter.")
        guess = input("Guess a number between 0 and 20: ")

    guess = int(guess)
    if guess != number:
        if guess > 20 or guess < 0:
            print(f"The number {guess} is out of range (0 to 20). Please try again.")
        elif guess > number:
            print("Your guess is too high")
        elif guess < number:
            print("Your guess is too low")
        return False
    else:
        print("Your guess is correct")
        return True


def main():
    number = random_number()
    debug = False
    changing_game = False

    while True:
        result = higher_or_lower(number, debug, changing_game)

        if result == True:
            break
        elif result == 'debug':
            debug = not debug
        elif result == 'changing_game':
            changing_game = not changing_game
        elif result == False:
            if changing_game:
                change = random.randint(-2, 2)
                number += change
                number = max(0, min(20, number))


if __name__ == "__main__":
    main()

