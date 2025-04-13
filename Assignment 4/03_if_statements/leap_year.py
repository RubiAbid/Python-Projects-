'''
Write a program that reads a year from the user and tells whether a given year is a leap year or not.'''


def leapyear():
    year = int(input("Enter a year to check: "))
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

if __name__ == "__main__":
    leapyear()
