import random

def random_number():
    number = int(20 * random.random())
    return number

def higher_or_lower(guess, number):
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

def modes(guess, number):
    if guess == 'x':
        print("Game over")
        return True

    if not guess.isdigit():
        print("Invalid input. Please enter a number between 0 and 20, or a valid command.")
        return False

    return higher_or_lower(int(guess), number)

def main():
    number = random_number()
    while True:
        guess = input("Guess a number between 0 and 20: ")
        if modes(guess, number):
            break

if __name__ == "__main__":
    main()

