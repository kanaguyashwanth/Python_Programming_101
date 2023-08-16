# RANDOM MODULE - Pseudo random num gen

'''
EXAMPLE 1:

import random

i = 100
j = 20e7

# Generates a random number between i and j
a = random.randrange(i, j)
try:
    b = random.randrange(j, i)
except ValueError:
    print('ValueError on randrange() since start > stop')
    
c = random.randint(100, 200)
try:
    d = random.randint(200, 100)
except ValueError:
    print('ValueError on randint() since 200 > 100')
    
print('i =', i, ' and j =', j)
print('randrange() generated number:', a)
print('randint() generated number:', c)
'''

# Printing a Random whole number
import random
random_int = random.randint(1, 10)
print (f'Random Integer: {random_int}')


# Creating OWN Module - DIRECTORY: Desktop/Python Courses/Day-4/my_module.py
import my_module
print (f'My module: {my_module.pi}')	# Calling the module - module_name.variable name (inside module file)


# Printing a Random floating point number - # 0.0000000 to 0.9999999...
import random
rand_float = random.random()
print (f'Random Float: {rand_float}')

# EXERCISE - Create a random decimal number between 0 and 5
# Range: 0.000000... - 4.999995...
import random
rand_float = random.random()
rand_float *= 5
print (f'Random Float between 1 to 5: {rand_float}')

# EXERCISE - Love Calculator (Using random gen)
love_score = random.randint(1,100)
print (f'Your love score is: {love_score}')

# EXERCISE - Coin flip, Roll dice, etc
# 1. Coin Flip
flip_f = random.randint (1,2)
if flip_f == 1:
    flip_str = 'Heads'
    print (f'Coin flip: {flip_str}')
elif flip_f == 2:
    flip_str = 'Tails'
    print (f'Coin flip: {flip_str}')

# 2. Roll Dice
dice_r = random.randint (1,6)
print (f'Die roll: {dice_r}')