# from art import logo
#
# import random
#
#
# def dealer_dealer():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     choosing_card = random.choice(cards)
#     return choosing_card
#
#
#
# def calculate_score(cards):
#     if sum(cards) == 21 and  len(cards) == 2:
#         return 0
#
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#
#     return sum(cards)
#
# def compare(user_score, dealer_score):
#     if user_score == dealer_score:
#         return "Draw 🙃"
#     elif dealer_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif user_score == 0:
#         return "Win with a Blackjack 😎"
#     elif user_score > 21:
#         return "You went over. You lose 😭"
#     elif dealer_score > 21:
#         return "Opponent went over. You win 😁"
#     elif user_score > dealer_score:
#         return "You win 😃"
#     else:
#         return "You lose 😤"
#
# def play_game():
#     print(logo)
#     user_card = []
#     dealer_card = []
#     computer_score = -1
#     user_score = -1
#     is_game_over = False
#
#     for _ in range(2):
#         user_card.append(dealer_dealer())
#         dealer_card.append(dealer_dealer())
#
#     while not is_game_over:
#         user_score = calculate_score(user_card)
#         computer_score = calculate_score(dealer_card)
#         print(f"Your cards: {user_card}, current score: {user_score}")
#         print(f"Computer's first card: {dealer_card[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'Y' to get another card, type 'n' to pass")
#             if user_should_deal == "y":
#                 user_card.append(dealer_dealer())
#             else:
#                 is_game_over = True
#         while computer_score == 0 or computer_score > 21:
#             dealer_card.append(dealer_dealer())
#             computer_score = calculate_score(dealer_card)
#
#         print(f"Your final hand: {user_card}, final score: {user_score}")
#         print(f"Computer's final hand: {dealer_card}, final score: {computer_score}")
#         print(compare(user_score, computer_score))
#
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     print("\n" * 20)
#     play_game()

from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    choosing_card = random.choice(cards)
    return choosing_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_card = []
    dealer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(dealer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {dealer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # PREVIOUS MISTAKE: You prompted the user to type a capital 'Y', but checked if it equaled lowercase 'y'.
            # If the user obeyed and typed 'Y', the game thought they typed 'n' and ended their turn early.
            # FIX: Added .lower() to the input so it safely accepts both 'Y' and 'y'.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    # PREVIOUS MISTAKE: In your original code, the dealer's turn and the final print statements were indented
    # one level deeper, trapping them INSIDE the user's `while not is_game_over:` loop.
    # This meant the dealer drew cards and the game printed the final score every time the user drew a single card.
    # FIX: I unindented the code below so it aligns with the `while` loop. Now, this block only triggers
    # AFTER the user's loop is completely finished.

    # PREVIOUS MISTAKE: Your logic was `while computer_score == 0 or computer_score > 21:`.
    # This meant the dealer ONLY drew cards if they had a Blackjack (0) or if they had ALREADY gone over 21.
    # FIX: In standard Blackjack rules, the dealer must keep drawing cards as long as their score is under 17.
    while computer_score != 0 and computer_score < 17:
        dealer_card.append(deal_card())
        computer_score = calculate_score(dealer_card)

    # (These print statements were also unindented to sit outside the user's loop, as mentioned above)
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# PREVIOUS MISTAKE: Just like the drawing prompt, if the user typed a capital 'Y' here, the game would instantly shut down.
# FIX: Added .lower() to ensure the game starts regardless of capitalization.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()