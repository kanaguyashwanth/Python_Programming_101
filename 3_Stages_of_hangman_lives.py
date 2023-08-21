# Stages of hangman and remaining lives

import random

word_list = ['ardvark', 'baboon', 'camel']
rand_num = random.randint(0, len(word_list)-1)
guess = word_list[rand_num]
print (f'Word: {guess}')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Printing a blank list with the length of the guess word
blank_list=[]
for n in range (len(guess)):
    blank_list.append("_")		#When list functions are used, we do not have to assign or specify the Index number.

print (blank_list)



# Replacing blanks with guesses

i = len(guess) # Decrease the count for every correct guess

guess_list = []
prev_list = []
for n in range (len(guess)):
    guess_list.append(guess[n])

lives = 6
print(f'Remaining lives: {lives}')

while (i>0 and lives>0):
    
    u_guess = input ('Guess a letter: ').lower()
    
    '''
    if u_guess != guess[n]:
        print(f"Remaining attempts: {remaining_choices}")
        remaining_choices -= 1
    '''
    
    # Lose condition
    prev_list = blank_list
    
    # Updating the list
    for n in range (len(guess)):
        if u_guess == guess[n]:
            blank_list[n] = u_guess
            i -= 1
    print(blank_list)
    
    # Lose condition
    if (prev_list == blank_list):
        lives -= 1
        print(f'Remaining lives: {lives}')
    
    # Win condition
    if blank_list == guess_list:
        print ('You Win!')
        

