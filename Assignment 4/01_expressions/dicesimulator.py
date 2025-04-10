'''
Simulate rolling a die three times.
Prints the results of each die roll.
This program is used to show how variable scope works.
'''

import random

dice_roll = 6  # max number on a die

def dice():
    die1 = random.randint(1, dice_roll)
    die2 = random.randint(1, dice_roll)
    die3 = random.randint(1, dice_roll)
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Third die: {die3}")

def dice2():
    die1:int=40
    print(f'Value of Die1 in second function is :{die1}')
    dice()
    print(f'Value of Die1 after is still :{die1}')


if __name__ == "__main__":
    dice2()
