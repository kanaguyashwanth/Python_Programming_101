# CONDITIONAL STATEMENTS WITH LOGICAL OPERATORS:

'''
if condition1 and condtion2 and condition3:
    do this
else
    do this
    

LOGICAL OPERATORS: and / or / not (keywords)
A and B
C or D
not E
'''

# CODING EXERCISE: Free tickets for people aged between 45-55. (MIDLIFE CRISIS)
height = int (input ('Enter your height(cm): '))

if height >= 120:
    print ('You can ride!')
    age = int (input ('Enter your age: '))
    
    if age < 12:
        bill = 5
        print (f'Child tickets are ${bill}')
    elif age <= 18:
        bill = 7
        print (f'Youth tickets are ${bill}')
    elif (age>18 and age<45 and age>55):
        bill = 12
        print (f'Adult tickets are ${bill}')
    else:
        bill = 0
        print (f'Middle-age tickets are ${bill}')
        print ('Everything is going to be okay. Havee a free ride with us!')


    photo = input ('Do you want photos? Y or N. ' )
    if photo == 'Y':
        bill += 3
        print (f'Please pay ${bill}')
    else:
        print (f'Please pay ${bill}')

else:
    print ('You cannot ride.')