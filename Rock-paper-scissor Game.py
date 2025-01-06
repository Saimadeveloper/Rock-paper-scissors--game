import random

emojis = {'r': '🎨', 'p': '📰', 's': '✂'}  # Emoji dictionary
choices = ('r', 'p', 's')  # Available choices

while True: 
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()  # Prompt user input
    if user_choice not in choices:  # Validate user input
        print("Invalid choice, please try again.")
        continue
    
    computer_choice = random.choice(choices)  # Computer makes a random choice

    print(f"You chose {emojis[user_choice]}")  # Display user choice
    print(f"Computer chose {emojis[computer_choice]}")  # Display computer choice

    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')
    ):
        print("You win!")
    else:
        print("You lose the game.")

    # Ask if the user wants to continue
    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break
