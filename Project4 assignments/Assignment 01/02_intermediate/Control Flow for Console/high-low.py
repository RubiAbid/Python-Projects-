'''We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!'''

import random

print('Welcome to High-Low game!')

my_points = 0
comp_points = 0

for i in range(1, 6):
    print(f"\nRound {i}")
    
    mine = random.randint(1, 100)
    computer = random.randint(1, 100)
    
    print(f"Your number is {mine}")
    
    user_input = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()
    
    if mine > computer and user_input == "higher":
        print(f"You were right! The computer's number was {computer}")
        my_points += 1
    elif mine < computer and user_input == "lower":
        print(f"You were right! The computer's number was {computer}")
        my_points += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer}")
        comp_points += 1

# Final score
print(f"\nFinal score: You - {my_points}, Computer - {comp_points}")
if my_points > comp_points:
    print("🎉 You win!")
elif my_points < comp_points:
    print("😞 Computer wins!")
else:
    print("🤝 It's a tie!")






