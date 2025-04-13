import random

number = int(20*random.random())
print(number)
guess = int(input("Enter number : "))

if guess > number:
    print("Your guess is too high")
elif guess < number:
    print("Your guess is too low")
else:
    print("Your guess is correct")