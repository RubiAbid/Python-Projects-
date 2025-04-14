import time

def countdown_timer(seconds):
    print(f"\nTimer set for {seconds} seconds. Go run a round! 🏃‍♂️\n")
    
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(f"⏳ Time left: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up! Great job finishing your round! 🎉")

# Main
try:
    total_time = int(input("Enter time in seconds (go run a round!): "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter a valid number.")
