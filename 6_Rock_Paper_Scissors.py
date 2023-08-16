# EXERCISE - Rock Paper Scissors

'''
RULES:

Rock wins against scissors
Scissors wins against paper
Paper wins against rock

'''



# CODE:
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input ('Rock, Paper, Scissors?\n ')

rand_num = random.randint(1,3)

if rand_num == 1:
    comp_choice = "Rock"
elif rand_num == 2:
    comp_choice = "Paper"
else:
    comp_choice = "Scissors"



if comp_choice == "Rock":
    if choice == "Paper":
        winr = "You"
        print (f'Your choice: Paper\n{paper}')
        print (f'Computer choice: Rock\n{rock}')
        print (f'Winner: {winr}')
    elif choice == "Scissors":
        winr = "Computer"
        print (f'Your choice: Scissors\n{scissors}')
        print (f'Computer choice: Rock"\n{paper}\n')
        print (f'Winner: {winr}')
    else:
        print (f'Your choice: Rock\n{rock}')
        print (f'Computer choice: Rock"\n{rock}\n')
        print (f'It is a draw!')
        
elif comp_choice == "Paper":
    if choice == "Rock":
        winr = "Computer"
        print (f'Your choice: Rock\n{rock}')
        print (f'Computer choice: Paper\n{paper}')
        print (f'Winner: {winr}')
    elif choice == "Scissors":
        winr = "You"
        print (f'Your choice: Scissors\n{scissors}')
        print (f'Computer choice: Paper"\n{paper}\n')
        print (f'Winner: {winr}')
    else:
        print (f'Your choice: Paper\n{paper}')
        print (f'Computer choice: Paper"\n{paper}\n')
        print (f'It is a draw!')
        
else:
    if choice == "Rock":
        winr = "You"
        print (f'Your choice: Rock\n{rock}')
        print (f'Computer choice: Scissors\n{scissors}')
        print (f'Winner: {winr}')
    elif choice == "Paper":
        winr = "Computer"
        print (f'Your choice: Paper\n{paper}')
        print (f'Computer choice: Scissors"\n{scissors}\n')
        print (f'Winner: {winr}')
    else:
        print (f'Your choice: Scissors\n{scissors}')
        print (f'Computer choice: Scissors"\n{scissors}\n')
        print (f'It is a draw!')
