'''Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

Here's a sample run (user input is in blue):

Enter a number: 42 The ones digit is 2'''


def print_ones_digit(num):
    result = num % 10
    print(f"The ones digit is {result}")

def main():
    user_input = input("Enter a number: ")
    
    if user_input.isdigit():
        number = int(user_input)
        print_ones_digit(number)
    else:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
