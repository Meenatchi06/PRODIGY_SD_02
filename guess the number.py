import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess > number_to_guess:
            print("Too high! Try again.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You've guessed the number correctly after {attempts} attempts.")
            break

guess_the_number()
