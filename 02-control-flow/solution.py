import random

number_to_guess = random.randint(1, 10)

count_number_of_tries = 0

max_attempts = 4

print("Welcome to the number guess game!")
while True:
    while count_number_of_tries < max_attempts:
        guess = int(input("Please guess a number between 1 and 10: "))

        if guess == -1:
            print(f"Ssh! the answer is {number_to_guess}")
            continue
        count_number_of_tries += 1
        if guess == number_to_guess:
            print(f"Well done you won! You did in {count_number_of_tries} tries.")
            break
        elif abs(guess - number_to_guess) == 1:
            print("You are one away!")
        elif guess > number_to_guess:
            print("Whoops! You were too high!")
        elif guess < number_to_guess:
            print("Whoops! You were too low!")

    play_again = input("Do you want to play again? (y/n)")
    if play_again == "n":
        break
    else:
        count_number_of_tries = 0
        number_to_guess = random.randint(1,10)

print("Game over!")