import random

game_config = {
    "min_number": 1,
    "max_number": 100,
    "max_attempts": 2
}

feedback_messages = {
    "near": "You are one away!",
    "high": "Whoops! You were too high!",
    "low": "Whoops! You were too low!",
}


number_to_guess = random.randint(game_config["min_number"], game_config["max_number"])

count_number_of_tries = 0

max_attempts = game_config["max_attempts"]

print("Welcome to the number guess game!")
while True:
    guess_history = []
    while count_number_of_tries < max_attempts:
        if len(guess_history) > 0:
            print(f"You've already guessed: {guess_history}")
        guess = int(input("Please guess a number between 1 and 10: "))

        if guess == -1:
            print(f"Ssh! the answer is {number_to_guess}")
            continue
        count_number_of_tries += 1
        guess_history.append(guess)
        if guess == number_to_guess:
            message =f"Well done you won! You did in {count_number_of_tries} tries."
            print(message)
            guess_history.append((guess, message))
            break
        elif abs(guess - number_to_guess) == 1:
            message = feedback_messages["near"]
            print(message)
            guess_history.append((guess, message))
        elif guess > number_to_guess:
            message = feedback_messages["high"]
            print(message)
            guess_history.append((guess, message))
        elif guess < number_to_guess:
            message = feedback_messages["low"]
            print(message)
            guess_history.append((guess,message))
    print(guess_history)
    play_again = input("Do you want to play again? (y/n)")
    if play_again == "n":
        break
    else:
        count_number_of_tries = 0
        number_to_guess = random.randint(1,10)

print("Game over!")



