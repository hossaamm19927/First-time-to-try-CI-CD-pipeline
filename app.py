import random


def get_user_choice():
    """
    Prompts the user to enter their choice and validates the input.
    """
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        # Get user input and convert to lowercase for easy comparison
        user_input = input(
            "Enter your choice (Rock, Paper, or Scissors): ").lower()

        if user_input in valid_choices:
            return user_input
        else:
            print(
                f"Invalid choice. Please enter one of: {', '.join(valid_choices)}.")


def get_computer_choice():
    """
    Randomly selects a choice for the computer.
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the Rock-Paper-Scissors rules.
    Returns: 'win', 'lose', or 'tie'.
    """
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}\n")

    if user_choice == computer_choice:
        return 'tie'

    # Check for winning conditions
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        # If not a tie and not a win, it must be a loss
        return 'lose'


def play_game():
    """
    The main game loop for Rock-Paper-Scissors.
    """
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        try:
            # 1. Get choices
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            # 2. Determine and announce result
            result = determine_winner(user_choice, computer_choice)

            if result == 'win':
                print("🎉 You win! Great job! 🎉")
            elif result == 'lose':
                print("😞 You lose! Better luck next time. 😞")
            else:
                print("🤝 It's a tie! Go again. 🤝")

            # 3. Ask to play again
            play_again = input(
                "\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("\nThanks for playing! Goodbye.")
                break

        except KeyboardInterrupt:
            # Allows the user to exit gracefully with Ctrl+C
            print("\n\nGame interrupted. Thanks for playing! Goodbye.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


# Execute the game function when the script is run
if __name__ == "__main__":
    play_game()
