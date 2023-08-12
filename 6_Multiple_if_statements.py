# MULTIPLE if STATEMENTS: if /elif / else

'''
!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!

if / elif / else - ONLY A / B / C IS PERFORMED
if condition1:
    do A
elif condition2:
    do B
else:
    do C


Multiple if - ALL A, B, C IS PERFORMED
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C

!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!
'''


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
    else:
        bill = 12
        print (f'Adult tickets are ${bill}')


    photo = input ('Do you want photos? Y or N. ' )
    
    
    if photo == 'Yes':
        bill += 3
        print (f'Please pay ${bill}')
    else:
        print (f'Please pay ${bill}')

else:
    print ('You cannot ride.')
    
