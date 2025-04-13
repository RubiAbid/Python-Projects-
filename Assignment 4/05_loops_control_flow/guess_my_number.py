'''Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48'''


import random

guess = random.randint(0, 99)

while True:
    Your_guess = input("Enter a guess: ")

    if not Your_guess.isdigit():
        print("Please enter a valid number!")
        continue

    users_guess = int(Your_guess)

    if users_guess > guess:
        print("Your guess is too high")
    elif users_guess < guess:
        print("Your guess is too low")
    else:
        print(f"Congrats! The number was: {guess}")
        break



