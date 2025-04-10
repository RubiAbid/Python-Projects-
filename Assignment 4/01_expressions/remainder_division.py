'''Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

'''


def main():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))

    quotient = first_num // second_num
    remainder = first_num % second_num

    print(f"The result of {first_num} divided by {second_num} is:")
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")

if __name__ == "__main__":
    main()
