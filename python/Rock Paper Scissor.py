import random as r
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Choices and game result matrix
choice = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
game = ((0, -1, 1), (1, 0, -1), (-1, 1, 0))

# Keep track of scores
score = {"Wins": 0, "Losses": 0, "Ties": 0}

# User input function
def User_ip():
    user = int(input("Enter your choice (0-Rock/1-Paper/2-Scissor): "))
    while user not in choice:
        user = int(input("\rWrong input. Enter your choice again (0-Rock/1-Paper/2-Scissor): "))
    return user

# Computer input function with dramatic rolling effect
# Computer input function with dramatic rolling effect
def Comp_ip():
    print("\nRolling the computer's choice...")
    time.sleep(0.5)
    # List of possible choices to display while rolling
    rolling_choices = ["Rock", "Paper", "Scissor"]
    
    # Simulate the rolling effect for 5 cycles
    for i in range(12):
        for comp in range(0,3):
            print(f"\r{Fore.YELLOW}{rolling_choices[comp]}{' '*10}", end="")
            time.sleep(0.15)  # Delay for the rolling effect
    
    # Final computer choice after rolling
    comp = r.randint(0, 2)
    print(f"\r{' '*30}", end="")  # Clear the line
    # time.sleep(1)
    return comp


# Check the result of the round
def check(user, comp):
    return game[comp][user]

# Start the game with dramatic timing and colors
def startgame():
    while True:
        user = User_ip()
        comp = Comp_ip()

        print(f"\nYou chose {Fore.CYAN}{choice[user]}")
        print(f"Computer chose {Fore.MAGENTA}{choice[comp]}")

        result = check(user, comp)

        if result == 1:
            print(f"{Fore.GREEN}You Win!")
            score["Wins"] += 1
        elif result == -1:
            print(f"{Fore.RED}You Lose!")
            score["Losses"] += 1
        else:
            print(f"{Fore.BLUE}It's a Tie!")
            score["Ties"] += 1

        # Display current score
        print(f"\n{Style.BRIGHT}Current Score:")
        print(f"Wins: {score['Wins']}, Losses: {score['Losses']}, Ties: {score['Ties']}")

        # Ask if user wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"\n{Fore.YELLOW}Thanks for playing! Final Score:")
            print(f"Wins: {score['Wins']}, Losses: {score['Losses']}, Ties: {score['Ties']}")
            break

# Start the game
startgame()
