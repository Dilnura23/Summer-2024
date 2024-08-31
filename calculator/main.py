from replit import clear

from art import logo

print(logo)
# Calculator
def division(first, second):
  return first/second
def multiplication(first, second):
  return first*second
def subtraction(first, second):
  return first-second
def addition(first, second):
  return first+second
symbols = ['*', '/', '-', '+']
operations = {
  '*': multiplication, 
  '/': division, 
  '-': subtraction, 
  '+': addition
}
def display_symbols():
  for x in symbols:
    print(x)
  return input('Please choose an operation from above: ')

  
def main(first_numb, second_numb, choose_symbol):

  function = operations[choose_symbol]
  result = function(first_numb, second_numb)
  print(f'{first_numb} {choose_symbol} {second_numb} = {result}')
  choice = input(f'Type "y" to continue to use {result} or type "n" to start a new calculation: ')
  
  end_of_operation = False
  while not end_of_operation:
    
    if choice == 'y':
      my_new_symbol = display_symbols()
      diff_numb = int(input('What is the next number? '))
      main(result, diff_numb, my_new_symbol)
     
    elif choice == 'n':
      clear()
      first_numb = int(input('What\'s the first number? '))
      my_new_symbol = display_symbols()
      second_numb = int(input('What\'s the second number? '))
      main(first_numb, second_numb, my_new_symbol)

    else:
      end_of_operation = True
      break

first_numb = int(input('What\'s the first number? '))
choosen_symbol = display_symbols()
second_numb = int(input('What\'s the second number? '))
main(first_numb, second_numb, choosen_symbol)


  

    


