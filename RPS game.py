from random import choice

# Define possible actions
possible_actions = ["rock", "paper", "scissors"]

while True:  # Infinite loop to keep the game running
    # Get user input
    user_action = input("Rock, paper, or scissors? ").lower()

    # Check if user input is valid
    while user_action not in possible_actions:  # Inner loop for invalid input
        print("Invalid input. Please select 'rock', 'paper', or 'scissors'.")
        user_action = input("Rock, paper, or scissors? ").lower()

    # Generate computer's choice
    computer_action = choice(possible_actions)

    # Determine the winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! Computer wins!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beat paper! Computer wins!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors beat paper! You win!")
        else:
            print("Rock beats scissors! Computer wins!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break  # Exit the loop
