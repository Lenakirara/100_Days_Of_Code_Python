import os
from art import logo

bids = {}
finished_bid = False

def highest_bidder(bidding):
  highest_bid = 0
  winner = ""
  for bidder in bidding:
    amount = bidding[bidder]
    if amount > highest_bid: 
      highest_bid = amount
      winner = bidder
  print(f"\nThe winner is {winner} with a bid of ${highest_bid:.2f}")

while not finished_bid:
  print(logo)
  print("""
  =========================================================
  ======== Welcome to the private bidding auction! ========
  =========================================================
  """)
  name = input('Type your name: ').title().strip()
  price = float(input('Type your bid: $'))
  bids[name] = price
  others = input('Are there any other bidders? Type "yes" or "no": ').lower()
  if others == 'no':
    finished_bid = True
    highest_bidder(bids)
  elif others == 'yes':
    os.system('clear') or None
