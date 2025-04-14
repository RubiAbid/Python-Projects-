import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print(f"Congrats! You've guessed the number {random_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one possible number left
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!!")


guess(20)
computer_guess(20)
