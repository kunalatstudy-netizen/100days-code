# import random
# from art import logo
#
#
#
# def play_game():
#         print(logo)
#         print("Welcome to the Number Guessing Game!")
#         random_number = random.randint(1, 101)
#         game_number = random_number
#         print("I'm thinking of a number from 1 to 100.")
#         levels = input("Choose a difficulty. Type 'easy' or 'hard': ")
#         game_over = False
#         while not game_over:
#             total_lives = 10
#             hard_lives = 5
#             if levels == 'easy':
#                 print("You have 10 attempts to guess the number.")
#                 print(game_number)
#                 for _ in range(10):
#                     user_guess = int(input("Guess the number: "))
#                     if user_guess == game_number:
#                         print("You guessed the number!")
#                         game_over = True
#                     else:
#                         print("you have guessed wrong number")
#                         total_lives -= 1
#                         if total_lives == 0:
#                             game_over = True
#             elif levels == 'hard':
#                 print("You have 5 attempts to guess the number.")
#                 for _ in range(5):
#                     user_guess = int(input("Guess the number: "))
#                     if user_guess == game_number:
#                         print("You guessed the number!")
#                         game_over = True
#                     else:
#                         print("you have guessed wrong number")
#                         hard_lives -= 1
#                         if hard_lives == 0:
#                             game_over = True
#
#
#
#
#
# play_game()

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns-1
    elif user_guess < actual_answer:
        print("Too Low")
        return -1
    else:
        print(f"you got it! The answer was {actual_answer}")

# set difucutly

def set_difficulty():
    level = input("Choose a difficulty level (easy/hard): ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()