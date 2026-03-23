from art import logo
print(logo)

def auction_winner(bider_list):
    winner_name = ""
    win_amount = 0

    for key in bider_list:
        if bider_list[key] > win_amount:
            win_amount = bider_list[key]
            winner_name += key
        else:
            winner_name = winner_name
            win_amount = win_amount
    print(f"{winner_name} won the auction with the bid of ${win_amount}")

auction_over = False
while not auction_over:
    bider_list = {}
    name = input("What is your name?")
    bid = int(input("What is your bid?$ "))
    bider_list[name] = bid
    more_bider = input("Are there any other bidders? Type 'yes or 'no'")

    if more_bider == 'yes':
        print("\n" * 20)
        auction_over = False
    else:
        auction_winner(bider_list)
        auction_over = True





