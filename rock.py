import random

def print_choices():
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def get_player_choice():
    while True:
        print_choices()
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

def get_computer_choice():
    return random.randint(1, 3)

def print_result(player_choice, computer_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    print(f"You chose {choices[player_choice - 1]}")
    print(f"The computer chose {choices[computer_choice - 1]}")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        return "player"
    else:
        return "computer"

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print_result(player_choice, computer_choice)
        result = determine_winner(player_choice, computer_choice)

        if result == "player":
            print("You win!")
            player_score += 1
        elif result == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a draw!")

        print(f"Score - You: {player_score}  Computer: {computer_score}")

        if not play_again():
            print("Thanks for playing Rock, Paper, Scissors!")
            break

play_game()
