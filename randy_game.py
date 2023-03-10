import random

def play_game():
    print("Welcome to the number guessing game!")
    secret_number = random.randint(1, 100)
    num_guesses = 0
    while True:
        guess = input("Guess a number between 1 and 100: ")
        num_guesses += 1
        try:
            guess = int(guess)
            if guess == secret_number:
                print(f"Congratulations, you guessed the secret number in {num_guesses} tries!")
                break
            elif guess < secret_number:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

play_game()
