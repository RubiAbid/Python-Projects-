'''Write a program which continuously asks the user to enter values which are added
 one by one into a list. When the user presses enter without typing anything,
   print the list.
'''


def main():
    lst = []  # Initialize an empty list
    while True:
        user_input = input("Enter a value (press Enter to finish): ")
        if user_input == "":
            break  # Exit the loop if the input is empty
        lst.append(user_input)  # Add the input to the list
    print("Final list:", lst)

if __name__ == "__main__":
    main()
