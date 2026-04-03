import random
from art import logo



def play_game():
        print(logo)
        print("Welcome to the Number Guessing Game!")
        random_number = random.randint(1, 101)
        game_number = random_number
        print("I'm thinking of a number from 1 to 100.")
        levels = input("Choose a difficulty. Type 'easy' or 'hard': ")
        game_over = False
        while not game_over:
            total_lives = 10
            hard_lives = 5
            if levels == 'easy':
                print("You have 10 attempts to guess the number.")
                print(game_number)
                for _ in range(10):
                    user_guess = int(input("Guess the number: "))
                    if user_guess == game_number:
                        print("You guessed the number!")
                        game_over = True
                    else:
                        print("you have guessed wrong number")
                        total_lives -= 1
                        if total_lives == 0:
                            game_over = True
            elif levels == 'hard':
                print("You have 5 attempts to guess the number.")
                for _ in range(5):
                    user_guess = int(input("Guess the number: "))
                    if user_guess == game_number:
                        print("You guessed the number!")
                        game_over = True
                    else:
                        print("you have guessed wrong number")
                        hard_lives -= 1
                        if hard_lives == 0:
                            game_over = True





play_game()