import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(actual_number, user_guess):
    if actual_number > user_guess:
        print("Too low!")
    elif actual_number < user_guess:
        print("Too high!")
    else:
        print(f"You win! Answer is {actual_number}.")


def set_difficulty():
    level = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def play_game():

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = set_difficulty()
    guess = 0

    while attempts > 0 and guess != number:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_answer(number, guess)
        if guess != number:
            attempts -= 1
            if attempts == 0:
                print("\nNo more attempts left! Start a new game.")


play_game()
