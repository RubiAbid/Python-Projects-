import random

def play():
    user_input = input("Enter 'r' for rock, 'p' for paper, and 's' for scissor: ")
    computer = random.choice(['r', 'p', 's'])
    if user_input == computer:
        return "It's a tie!"
    if is_win(user_input, computer):
        return "You Win!"
    return "You lost!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
       (player == 'p' and opponent == 'r') or \
       (player == 's' and opponent == 'p'):
        return True

print(play())
