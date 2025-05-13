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

def main():
    number = random_number()
    while True:
        guess_input = input("Guess a number between 0 and 20: ")
        if not guess_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        guess = int(guess_input)
        if higher_or_lower(guess, number):
            break

if __name__ == "__main__":
    main()