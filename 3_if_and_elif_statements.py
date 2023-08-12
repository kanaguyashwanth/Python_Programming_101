# NESTED if STATEMENTS AND elif STATEMENTS:

'''
Welcome to the rollercoaster!
What is your height in cm? 121
You can ride the rollercoaster

CONDITION: Height > 120 cm
           age  < 12 ---> Pay $5
           age <= 18 ---> Pay $7
           age  > 18 ---> Pay $12
'''

print ('Welcome to the rollercoaster')
height = int (input ('What is your height in cm? '))

if height >= 120:
    print ('You can ride the rollercoaster')
    age = int (input ("What's your age? "))
    if (age < 12):
        print ('Please pay $5')
    elif (age <= 18):
        print ('Please pay $7')
    else:
        print ('Please pay $12')
else:
    print ('You cannot ride the rollercoaster')