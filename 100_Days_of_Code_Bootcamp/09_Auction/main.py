import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

participants = True
bids = {}

def add_bid(person_name,bid_value):
  bids[person_name] = bid_value

def get_winner():
  winner = ""
  winner_bid = 0

  for key in bids:
    if( bids[key] >= winner_bid):
      winner = key
      winner_bid = bids[key]
    #print(key)
    #print(bids[key])
  print(f"{winner} with the bid of {winner_bid} dollars")


while participants:
  person_name = input("What is your name?\n")
  bid = int(input("what is your bid?\n"))
  #Add this person to bids dictionary
  add_bid(person_name,bid)
  continue_bids = input("Are there any participants left?(yes,no)\n")

  if(continue_bids == "no"):
    participants = False

print("The winner of the auction is: ")
get_winner()
#print(bids)