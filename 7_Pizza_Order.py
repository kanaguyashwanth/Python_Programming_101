# CODING EXERCISE - Pizza Order

'''
Small Pizza:  $15
Medium Pizza: $20
Large Pizza:  $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: +$1

INPUT:
size: "L"
add_pepperoni = "Y"
extra_cheese = "N"

OUTPUT:
Your final bill is: $28.
'''


print ('Welcome to Python Pizza Deliveries!')
size = input ('What size pizza do you want? S/M/L: ')
add_pepperoni = input ('Do you want pepperoni? Y/N: ')
extra_cheese = input ('Do you want extra cheese? Y/N: ')

if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
    
if size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
        
if size == 'L':
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3
        
if extra_cheese == 'Y':
    bill += 1
    print (f'Your total bill: ${bill}')
else:
    print (f'Your total bill: ${bill}')

