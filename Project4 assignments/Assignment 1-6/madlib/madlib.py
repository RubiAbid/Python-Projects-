# Mad Libs Game 

print("Let's play Mad Libs! 🎉")
print("Fill in the blanks:")

# Getting user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

# Creating the story
mad_lib = f"""
Once upon a time, {name} went to {place}. 
It was a very {adjective} day. 
Suddenly, {name} saw a huge {noun} in the distance!
Without thinking, {name} decided to {verb} toward it.
And that’s how {name} became a legend!
"""

# Print
print("\nHere's your Mad Libs story:")
print(mad_lib)
