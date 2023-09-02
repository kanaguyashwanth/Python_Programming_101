# EXERCISE - NUMBER GUESSING GAME

'''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': hard

[HARD] - Total 5 attempts
You have 5 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess: 25
Too low.
Guess again.
You have 3 attempts remaining to guess the number.
Make a guess: 30
Too low.
Guess again.
You have 2 attempts remaining to guess the number.
Make a guess: 40
Too high.
Guess again.
You have 1 attempts remaining to guess the number.
Make a guess: 45
Too high.
You have run out of guesses. You lose.




Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': hard

[EASY] - Total 10 attempts
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too high.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 10
Too low.
Guess again.
You have 7 attempts remaining to guess the number.
Make a guess: 15
Too high.
Guess again.
You have 6 attempts remaining to guess the number.
Make a guess: 12
Too low.
You have 5 attempts remaining to guess the number.
Make a guess: 13
Too low.
You have 4 attempts remaining to guess the number.
Make a guess: 14
You got it! The answer was 14.
'''



import random

random_number = random.randint(1, 100)

print ("Welcome to the Number Guessing Game!")
print ("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choice == 'hard':
    attempts = 5
elif choice == 'easy':
    attempts = 10
    
while attempts>0:
    print(f'You have {attempts} remaining to guess the number')
    
    if attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            attempts = 0   # Exits the while loop
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
            
    elif attempts == 0:
        print("You have run out of guesses.")
    
    attempts -= 1