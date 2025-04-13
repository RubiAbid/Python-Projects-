'''imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

'''

ADULT_AGE = 18

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age_input = input("Enter age: ")
    if age_input.isdigit():
        age = int(age_input)
        print(is_adult(age))
    else:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
