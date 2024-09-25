import random
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

playerName = input(Fore.CYAN + "Enter your name: " + Style.RESET_ALL)
print(f"\n{Fore.YELLOW}Welcome {playerName} to the KBC Game Show!{Style.RESET_ALL}")
time.sleep(1)
print(Fore.MAGENTA + "\nGet ready for an exciting journey to become a millionaire!\n" + Style.RESET_ALL)
time.sleep(2)

# Questions, options, and answers
Question = [
    "Which of the following is the correct syntax to print \"Hello, World!\" in Python?",
    "Which of the following data types is immutable in Python?",
    "What is the correct file extension for Python files?",
    "How do you insert comments in Python?",
    "Which keyword is used to define a function in Python?"
]

Option = [
    ("A) echo \"Hello, World!\"", "B) printf(\"Hello, World!\")", "C) print(\"Hello, World!\")", "D) print(\"Hello\", \"World!\")"),
    ("A) List", "B) Dictionary", "C) Set", "D) Tuple"),
    ("A) .pyth", "B) .py", "C) .pt", "D) .python"),
    ("A) // This is a comment", "B) /* This is a comment */", "C) # This is a comment", "D) <!-- This is a comment -->"),
    ("A) def", "B) func", "C) define", "D) function")
]

Answer = ("C) print(\"Hello, World!\")", "D) Tuple", "B) .py", "C) # This is a comment", "A) def")
price = (0, 10000, 20000, 50000, 100000, 500000)

# Generate a list of unique random questions
questions_list = random.sample(range(len(Question)), 5)

# Countdown function for suspense
def countdown(seconds):
    while seconds > 0:
        print(f"{Fore.GREEN}Revealing in {seconds}...", end='\r')
        time.sleep(1)
        seconds -= 1
    print(Fore.CYAN + "Revealing now!                  ")  # Clear the countdown line

QueNo = 0
for i in questions_list:
    input("\nPress Enter to get your next question...")
    print(Fore.YELLOW + f"\nFor Rs. {price[QueNo + 1]}: {Question[i]}\n" + Style.RESET_ALL)

    for j in range(4):
        print(Fore.BLUE + Option[i][j] + Style.RESET_ALL)

    Ans = input(Fore.CYAN + "\nEnter Correct answer alphabet (A/B/C/D)\n=> " + Style.RESET_ALL).upper()
    
    # Ensure input is a single character and valid
    while len(Ans) != 1 or Ans not in ['A', 'B', 'C', 'D']:
        print(Fore.RED + "\nInvalid input! Please enter only A, B, C, or D." + Style.RESET_ALL)
        Ans = input(Fore.CYAN + "Enter Correct answer alphabet (A/B/C/D)\n=> " + Style.RESET_ALL).upper()

    print(Fore.MAGENTA + "\nLocking your answer..." + Style.RESET_ALL)
    countdown(5)  # 5-second countdown

    # Check answer and provide feedback
    if Ans == Answer[i][0]:
        print(Fore.GREEN + f"\nCORRECT ANSWER {playerName}! You have won Rs. {price[QueNo + 1]}!\n")
        QueNo += 1
    else:
        print(Fore.RED + f"\nWRONG ANSWER {playerName}. The correct answer was {Answer[i]}." + Style.RESET_ALL)
        break

# Final message with decorative lines
print("\n" + Fore.CYAN + "=" * 45)
print(Fore.MAGENTA + "               FINAL RESULT              ")
print(Fore.CYAN + "=" * 45 + Style.RESET_ALL)

if QueNo != 0:
    print(Fore.GREEN + f"Congratulations {playerName}, you won Rs. {price[QueNo]}!")
else:
    print(Fore.RED + f"Sorry {playerName}, you leave with Rs. {price[QueNo]}.")

# Dramatic end with more colorful messages
print(Fore.YELLOW + "\nThank you for playing KBC! We hope to see you again for another round!")
print(Fore.YELLOW + "Goodbye and stay tuned for more excitement!" + Style.RESET_ALL)
