# First Price Bid

bids = {}


name = input("Enter your name : ")
price = int(input("Enter the bid price : $ "))



bids[name] = price


should_continue = input("Are there any bidders ? Type 'yes' or 'no' : ")


# for clearing the screen
print("\n"*100)