import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(count, length):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords

# Main program
try:
    num_passwords = int(input("How many passwords do you want to generate? "))
    password_length = int(input("Enter the length of each password: "))

    print("\nHere are your generated passwords:\n")
    for i, pwd in enumerate(generate_multiple_passwords(num_passwords, password_length), 1):
        print(f"{i}. {pwd}")

except ValueError:
    print("Please enter valid numbers for password count and length.")
