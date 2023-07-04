#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '*', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?']

print("\nWelcome to the Unhackable-Password Generator!")



def password_generator():
  nr_letters= int(input("\nHow many letters would you like in your password?: ")) 
  nr_symbols = int(input(f"\nHow many symbols would you like?: "))
  nr_numbers = int(input(f"\nHow many numbers would you like?: "))
  password=''

  for num in range(nr_letters):
    letter=random.randint(0,51)
    letter=letters[letter]
    password=password+letter

  for num in range(nr_symbols):
    symbol=random.randint(0,9)
    symbol=symbols[symbol]
    password=password+symbol

  for num in range(nr_numbers):
    number=random.randint(0,9)
    number=numbers[number]
    password=password+number

  print(f'\nUnrandomized Verson of Password: {password}\n')


  new_pass=''
  for word in password:
    new_pass=new_pass+word+' '

  new_pass=new_pass.split()
  random.shuffle(new_pass)
  password=''.join(new_pass)
  print(f'Randomized Verson of Password: {password}')

  print('\nPlease note down your generated password for safe-keeping.')

  generate_again=input('\nIf you are not satisfied with this generated password, please press enter "Y" to generate a new one: ').upper()
  
  if generate_again=='Y':
    print('\n\nPlease enter in your preferences again to generate your password: ')
    password_generator()
  else:
    print('\n\nGoodbye!')
    return
password_generator()
