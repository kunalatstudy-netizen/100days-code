from art import logo
print(logo)

biders = {}
game_over = False
def winner(bider):
    winner_win = 0
    for key in biders:
        if bid > winner_win:
            winner_win = bid
        else:
            winner_win = winner_win
    print(f"The winner is {winner_win} with a bid of ${bid}")





while game_over == False:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    more_bider = input("Are there any other bidders? Type 'yes' or 'no': ")
    biders[name] = bid
    if more_bider == "yes":
        game_over = False
    else:
        game_over = True
        winner(biders[name])

