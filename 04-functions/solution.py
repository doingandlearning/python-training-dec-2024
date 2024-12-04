import random

def initialize_game():
    """Initialize game configuration and return a dictionary with initial values."""
    return {
        "min_number": 1,
        "max_number": 10,
        "max_attempts": 4,
        "number_to_guess": random.randint(1, 10),
        "count_number_of_tries": 0,
        "guess_history": []
    }


def display_welcome_message():
    """Print the welcome message."""
    print("Welcome to the number guess game!")


def get_guess(min,max):
    """Prompt the user for a guess and return it as an integer."""
    try:
        return int(input(f"Please guess a number between {min} and {max}: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return get_guess(min,max)


def check_guess(guess, number_to_guess):
    """Check the guess against the target number and return feedback."""
    if guess == number_to_guess:
        return "correct", f"Well done! You guessed it!"
    elif abs(guess - number_to_guess) == 1:
        return "near", "You are one away!"
    elif guess > number_to_guess:
        return "high", "Whoops! You were too high!"
    else:
        return "low", "Whoops! You were too low!"


def play_game():
    """Main game loop."""
    game_config = initialize_game()
    display_welcome_message()

    while True:
        while game_config["count_number_of_tries"] < game_config["max_attempts"]:
            if game_config["guess_history"]:
                print(f"You've already guessed: {game_config['guess_history']}")

            guess = get_guess(game_config["min_number"], game_config["max_number"])
            if guess == -1:
                print(f"Ssh! The answer is {game_config['number_to_guess']}")
                continue

            game_config["count_number_of_tries"] += 1
            result, feedback = check_guess(guess, game_config["number_to_guess"])
            game_config["guess_history"].append((guess, feedback))
            print(feedback)

            if result == "correct":
                print(f"You guessed it in {game_config['count_number_of_tries']} tries!")
                break

        print("Your guess history:", game_config["guess_history"])
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break
        else:
            game_config = initialize_game()

    print("Game over!")


# Run the game
play_game()
