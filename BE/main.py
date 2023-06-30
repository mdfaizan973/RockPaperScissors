import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Invalid choice. Please try again.")

def print_score(user_wins, computer_wins, draws):
    print("Score:")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Draws: {draws}")

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    print("Let's play Rock, Paper, Scissors!")

    while True:
        print("--------------------")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("You win!")
            user_wins += 1
        elif winner == "computer":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("It's a draw!")
            draws += 1

        print_score(user_wins, computer_wins, draws)

        if not play_again():
            break

    print("Thanks for playing!")

# Start the game
play_game()
