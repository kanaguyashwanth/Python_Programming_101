# CODING EXERCISE: TIP CALCULATOR

'''
Welcome to the tip calculator.
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
OUTPUT: Each person should pay: $19.93 (Only 2 decimal places)
'''

print ('Welcome to the Tip Calculator!')
total = float (input ('What was the total bill?($) '))
ptip = int (input ('What percentage tip would you like to give? 10,12, or 15? '))
split = int (input ('How many people to split the bill? '))

pay = ( total + ( total * (ptip / 100) ) ) / split
pay = round (pay,2)

print (f'Each person should pay: ${pay}')
