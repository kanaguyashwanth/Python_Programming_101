# CODING EXERCISE - Odd or Even Exercise (Using Modulo)

'''
Case 1: Odd
Which number you want to check? 35
This is an odd number.

Case 2:
Which number you want to check? 32
This is an even number.
'''

num = int (input ('Which number you want to check? '))

if num % 2 == 0:
    print ('This is an even number.')
else:
    print ('This is an odd number.')