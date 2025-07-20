import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: "))

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! 📉")
            elif guess > secret_number:
                print("Too high! 📈")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    else:
        print(f"😞 You've used all {max_attempts} attempts. The number was {secret_number}.")

number_guessing_game()
