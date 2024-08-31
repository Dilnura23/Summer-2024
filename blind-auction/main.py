from replit import clear

from art import logo

print(logo)
print('Welcome to the secret auction program.')
bid_info = {}
def info():
  name = input("What's your name? ")
  price = int(input("What's your bid? "))
  bid_info[name] = price
info()

bid_more = input('Is there anyone who wants to bid (yes/no)? ').lower()
while bid_more == "yes":
    clear()
    info()
    bid_more = input('Is there anyone who wants to bid (yes/no)? ').lower()

max_price = 0
winner = ""
for x in bid_info:
  current_price = bid_info[x]
  if current_price>max_price:
    max_price = current_price
    winner = x
clear()
print(f'The auction is closed! The winner is {winner} with the bid of ${max_price}')
  


