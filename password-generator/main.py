import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
type_password = int(input('Choose if you want ordered, Type 1, or unordered, Type 2, password based on your requirements above: '))

password = ""  
for letter in range(1,nr_letters+1):
  password = password+random.choice(letters)
for symbol in range(1, nr_symbols+1):
  password = password + random.choice(symbols)
for number in range(1, nr_numbers+1):
  password = password +random.choice(numbers)
if type_password == 1:
  print(f'Your ordered password is {password}')
else:
  password_list = list(password)
  random.shuffle(password_list)
  final_password = ""
  for char in password_list:
    final_password+= char
  print(f'Your unordered password is {final_password}')

