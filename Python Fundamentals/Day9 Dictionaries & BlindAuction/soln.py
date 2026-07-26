# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from os import name

from art import logo
print(logo)
value = True
max_value = 0
bid = {}
while(value):
    your_name = input("enter your name")
    amount= input("enter your amount of bid")
    bid[your_name] = amount
    answer=input("is there anyone behind you who will going to bid(yes or no)").lower()

    if answer == "yes":
        print("\n" * 100 )
        value =True

    elif answer == "no":
        value =False
        print()
    else:
        print("please enter yes or no")
        answer = input("is there anyone behind you who will going to bid(yes or no)").lower()

winner=""

for key in bid:
    bid[key] = int(bid[key])
    if bid[key]>max_value:
        max_value=bid[key]
for key,value in bid.items():
    if value==max_value:
        winner = key
print(f"the winner of the bid is {winner}  with  {max_value}$")

