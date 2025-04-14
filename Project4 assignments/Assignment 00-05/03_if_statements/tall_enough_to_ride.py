'''Problem Statement
Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

'''


def check_height():
    min_height = 6 
    height = float(input("Enter your height: "))

    if height >= min_height:
        print("You are tall enough to ride the rollercoaster! 🎉")
    else:
        print("Sorry, you're not tall enough to ride the rollercoaster. 😢")

if __name__ == "__main__":
    check_height()
