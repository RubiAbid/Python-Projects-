'''Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

Here's a sample run of the program (user input is in blue):

Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!'''


def print_multiple(message, repeats):
    result=message * repeats
    return result



def main():
    message = input("Please type a message: ")
    repeat = input("Enter a number of times to repeat your message: ")
    
    if repeat.isdigit():
        repeat = int(repeat)
        result = print_multiple(message, repeat)
        print(result)
    else:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()