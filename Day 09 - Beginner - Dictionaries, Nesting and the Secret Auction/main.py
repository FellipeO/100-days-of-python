import os
import subprocess
from art import logo

print(logo)
more_bidders = True
bidders = {}
while more_bidders:
    person = input("What is your name? ")
    bidders[person] = int(input("What is your bid? $"))
    choice = input("Are there any more bidders? ").lower()
    if choice == "no":
        more_bidders = False
    print("\n"*100)

highest_bidder = ""
highest_bid = 0

for player in bidders:
    if bidders[player] > highest_bid:
        highest_bid = bidders[player]
        highest_bidder = player

print(f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}")

