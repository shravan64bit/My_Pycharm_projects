from art import logo
from replit import clear

fianl_bid = []

def bidder_details(bidder_name,bid_amount):
    bidd = {}
    bidd["name"] = bidder_name
    bidd["amount"] = bid_amount
    fianl_bid.append(bidd)
print(logo)
condition = False
while not condition:
    bidder_name = input("What is your name ?")
    bid_amount = int(input("What is your bid ? $"))
    bidder_details(bidder_name, bid_amount)
    choice = input("Are there any other bidders?type 'yes' or 'no'")
    if choice == "yes":
        clear()
        condition = False
    elif choice == "no":
        print("hai")
        for numbers in range(len(fianl_bid)-1):
            winner_amount = 0
            print(f"{fianl_bid[numbers]['amount']},{fianl_bid[numbers+1]['amount']}")
            if fianl_bid[numbers]["amount"] > fianl_bid[numbers + 1]["amount"]:
                winner_amount = fianl_bid[numbers]["amount"]

            elif fianl_bid[numbers]["amount"] < fianl_bid[numbers + 1]["amount"]:
                winner_amount = fianl_bid[numbers + 1]["amount"]

            elif fianl_bid[numbers]["amount"]>winner_amount:
                winner_amount=fianl_bid[numbers]["amount"]
        print(f"The winner is how bid the amoont of $ {winner_amount}")
        condition = True








