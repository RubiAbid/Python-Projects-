'''Simulate rolling two dice, and prints results of each roll as well as the total.

'''


import random

def main():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    total = die1 + die2

    # Print results
    print(f"First die rolled: {die1}")
    print(f"Second die rolled: {die2}")
    print(f"Total of both dice: {total}")

if __name__ == '__main__':
    main()
