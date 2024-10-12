import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Ask the player to enter a guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                guessed = True

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
