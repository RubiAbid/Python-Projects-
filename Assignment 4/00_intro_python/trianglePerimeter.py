'''Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).'''


def main():
    side1=int(input(" WHat is the length of side 1 ?:"))
    side2=int(input(" WHat is the length of side 2 ?:"))
    side3=int(input(" WHat is the length of side 3 ?:"))
    print(f"perimeter of triangle is {side1+side2+side3}")

if __name__=="__main__":
    main()
