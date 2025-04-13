'''Write a program which prompts the user to type an affirmation of 
your choice (we'll use "I am capable of doing anything I put my mind 
to.") until they type it correctly. Sometimes, especially in the midst
 of such uncertain times, we just need to be reminded that we are resilient,
   capable, and strong; this little Python program may be able to help!'''


Affirmation = "I am capable of doing anything I put my mind to."

def main():
    while True:
        user = input("Please enter this affirmation: " + Affirmation + "\n")
        if user == Affirmation:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation.\n")

if __name__ == '__main__':
    main()
