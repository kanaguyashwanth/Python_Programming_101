# EXERCISE - Pick a random name from the list who is gonna buy the meal today.

'''
USE OF choice function is NOT ALLOWED!
Split Function - split(", ") --> splits the string and makes a list on the occurrance of ", "

INPUT:
Enter everybody's names separated by comma: Angela, Ben, Jenny, Michael, Chloe

OUTPUT:
Michael is going to buy the meal today!
'''


# CODE:
import random

# STRING
name_str = input ("Enter everybody's names separated by a comma: ")

# LIST
name_list = name_str.split(", ")

# RANDOM GEN
rand_int = random.randint(0, (len(name_list)-1))

# PRINT
print (f'{name_list[rand_int]} is going to buy the meal today!')
