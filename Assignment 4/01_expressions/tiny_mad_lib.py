'''Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

'''


def main():
    

    # Ask the user for the words
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    # Create and print the final sentence
    sentence = (f"The {adjective} {noun} {verb} through the forest!")
    print(sentence)

if __name__ == '__main__':
    main()
