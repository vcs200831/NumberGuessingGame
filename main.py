import random


def play_game():
    random_number = random.randint(1, 100)
    attempts_left = 5

    while attempts_left > 0:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            return

        if guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts_left -= 1
        print("Attempts left:", attempts_left)

    print("Out of attempts. The number was", random_number)


def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"


# Main game loop
while True:
    print("Welcome to the Number Guessing Game!")
    play_game()

    if not play_again():
        print("Thank you for playing. Goodbye!")
        break
