import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = input("Enter your guess (or 'q' to quit): ")

        if user_guess.lower() == 'q':
            print(f"Okay, the number was {number_to_guess}. Thanks for playing!")
            break

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input! Please enter a number or 'q' to quit.")
            continue

        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if user_guess == number_to_guess:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if _name_ == "_main_":
    guess_the_number()
