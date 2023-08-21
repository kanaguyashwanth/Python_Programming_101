# Picking a Random word

word_list = ['ardvark', 'baboon', 'camel']

'''
Task 1 - Randomly choose a word from List
Task 2 - Ask user to guess a letter and assign their ans to a variable. Make it lowercase.
Task 3 - Check if the guess and the randomly chosen word has the letter in common.
'''

# CODE:

import random

random_int = random.randint(1,3)
guess = word_list[random_int-1]

u_guess = input('Guess a letter: ').lower()

for n in range (len(guess)):
    if u_guess == guess[n]:
        print('Correct')
    else:
        print('Incorrect')
