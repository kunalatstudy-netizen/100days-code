print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# checking for the price of piza

size_in_small = size.lower()
total_bill = 0;

if size_in_small == "s":
    total_bill += 15
elif size_in_small == "m":
    total_bill += 20
elif size_in_small == "l":
    total_bill += 25

# checking for pepperoni

if pepperoni == "Y":
    if size_in_small == "s":
        total_bill += 2
    else:
        total_bill += 3

#cheking for extra cheese

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is: ${total_bill}.")