# Replacing Blanks with Guesses

import random

word_list = ['ardvark', 'baboon', 'camel']
rand_num = random.randint(0, len(word_list)-1)
guess = word_list[rand_num]
print (f'Word: {guess}')

# u_guess = input ('Guess a letter: ').lower()

# Printing a blank list with the length of the guess word
blank_list=[]
for n in range (len(guess)):
    blank_list.append("_")		#When list functions are used, we do not have to assign or specify the Index number.

print (blank_list)



# Replacing blanks with guesses

i = len(guess) # Decrease the count for every correct guess
remaining_choices = 9

guess_list = []
for n in range (len(guess)):
    guess_list.append(guess[n])

while (i>0):
    
    u_guess = input ('Guess a letter: ').lower()
    
    if u_guess != guess[n]:
        print(f"Remaining attempts: {remaining_choices}")
        remaining_choices -= 1
    
    for n in range (len(guess)):
        if u_guess == guess[n]:
            blank_list[n] = u_guess
            i -= 1
    
    if blank_list == guess_list:
        print ('You Win!')

    print(blank_list)