from art import logo

import random

print(logo)
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number from 1 to 100')
mode = input("Choose 'easy' or 'hard' mode: ")

computer_choice = random.randint(1,100)

def check_range(my_guess):
  """ it will compare they guessed number with the computer's choice"""
  if my_guess>computer_choice:
    return 'Too high'
  elif my_guess<computer_choice:
    return 'Too low'
  else:
    return 'You got it right!'
    
def run_game(my_mode, attempts):
  '''Start of the game'''
  print(f'You chose {my_mode}.\nYou will have {attempts} attempts.')
  while attempts>0:
    guess = int(input("Make a guess: "))
    result = check_range(guess)
    print(result)
    if result!='You got it right!':
      
      attempts-=1
      print(f'You have {attempts} attempts left.')
    else:
      break
  if attempts == 0:
    print(f'The chosen number was {computer_choice}')

if mode == 'easy':
  run_game('easy', 10)
else:
  run_game('hard', 5)


  
  