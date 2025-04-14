'''Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.'''


def double(num):
    return num * 2

def main():
    while True:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            num = int(user_input)
            result = double(num)
            print(f"Doubled number: {result}")
            if result >= 100:
                print("Result is 100 or more. Ending program.")
                break
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
