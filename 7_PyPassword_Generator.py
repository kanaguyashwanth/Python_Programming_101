#Password Generator Project

'''
NOTE:
You can use a shuffle the list as below:

import random

password_list = ['j', 'u', 'X', 'S', '9', '8', '2', '6', ')', '#', '*', '(']
print (password_list)
random.shuffle (password_list)
print (password_list)
'''

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# LETTER RANDOMISATION
l_letters = len(letters)
rand_strings = ''
for n in range(0, n_letters):
    rand_num = random.randint(0, (l_letters - 1))
    rand_strings = rand_strings + letters[rand_num]

print(f'Random strings: {rand_strings}')

# NUMBERS RANDOMISATION
l_numbers = len(numbers)
rand_N = ''
for n in range(0, n_numbers):
    rand_num = random.randint(0, (l_numbers - 1))
    rand_N = rand_N + numbers[rand_num]

print(f'Random numbers: {rand_N}')

# NUMBERS RANDOMISATION
l_symbols = len(symbols)
rand_symbols = ''
for n in range(0, n_symbols):
    rand_num = random.randint(0, (l_symbols - 1))
    rand_symbols = rand_symbols + symbols[rand_num]

print(f'Random symbols: {rand_symbols}')

# LETTERS + NUMBERS + SYMBOLS RANDOMISED
new_str = rand_strings + rand_N + rand_symbols
print(f'New random string: {new_str}')

# Algorithm
'''
Convert the string to list
Get the length of the list
Get a random number
Swap it with the revere of the index of the list
'''

# CONVERTING FROM A STRING TO LIST
new_list = []
n1 = len(new_str)
for n in range (0, n1):
  new_list.append(new_str[n])

print (f'New List: {new_list}')


l_new_list = len (new_list)

# Shuffling the items of list by swapping index positions
for n in range (0, l_new_list):
  rand_number = random.randint(0, (l_new_list-1))
  a = new_list[n]
  new_list[n] = new_list[rand_number]
  new_list[rand_number] = a

print (f'The shuffled list: {new_list}')

shuff_str = ''
for n in range (l_new_list):
  shuff_str = shuff_str + str(new_list[n])

print (f'The shuffled string: {shuff_str}')
