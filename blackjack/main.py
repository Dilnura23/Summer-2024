import random

from art import logo

from replit import clear

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
dealer = []
for x in range(2):
  user.append(random.choice(cards))
  dealer.append(random.choice(cards))

def check_blackjack(total):
  """checks black- if it contains 11"""
  summa = sum(total)
  if summa>21 and 11 in total:
    total[total.index(11)] = 1
    summa = sum(total)
  return summa

def count(total):
  summa = sum(total)
  return summa

print('Your cards:', user, ' current score:', count(user))
print("Computer's first card:", dealer[0])



end_of_the_game = False
while not end_of_the_game:
  if count(user) == 21:
    print('Your final hand:', user, ' final score:', count(user))
    print('Dealer\'s final hand:', dealer, ' final score:', count(dealer))
    print('You won, it is blackjack.')
    end_of_the_game = True
    break
  elif count(dealer) == 21:
    print('Your final hand:', user, ' final score:', count(user))
    print('Dealer\'s final hand:', dealer, ' final score:', count(dealer))
    print("Dealer won, it is blackjack.")
    end_of_the_game = True
    break


  elif check_blackjack(user)>21:
    print('Your final hand:', user, ' final score:', count(user))
    print('Dealer\'s final hand:', dealer, ' final score:', count(dealer))
    print("Dealer won, you went over.")
    end_of_the_game = True
    break

  ask_add_user = input('Type "y" to add another card or "n" to remain all cards as they are: ').lower()
  if ask_add_user == "y":
    user.append(random.choice(cards))
    clear()
    print('Your current hand:', user, 'current score:', count(user))
    print("Computer's first card:", dealer[0])
    continue
  else:
    print('You answered "no"')
    while count(dealer)<17:
      dealer.append(random.choice(cards))

    if count(dealer)>21:
      print('Your final hand:', user, ' final score:', count(user))
      print('Dealer\'s final hand:', dealer, ' final score:', count(dealer))
      print('You won, it over passed.')


    elif count(dealer)==count(user):
      print('It is a Tie')
 
    elif count(dealer)>count(user):
      print('Your final hand:', user, ' final score:', count(user))
      print('Dealer\'s final hand:', dealer, ' final score:', count(dealer))
      print("Dealer won, its score is bigger than yours.")
 
    else:
      print('Your final hand:', user, ' final score:', count(user))
      print('Dealer\'s final hand:', dealer, ' final score:', count(dealer))
      print('You won, your score is bigger than computer\'s.')
    end_of_the_game = True
    break









