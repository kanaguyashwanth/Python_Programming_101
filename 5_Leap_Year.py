# CODING EXERCISE - LEAP YEAR

'''
Write a program that works out whether
if a given year is a leap year. A normal
year has 365 days. leap years have 366,
with an extra day in February.

CONDITION:
on every year that is evenly divisible by 4
        except every year that is evenly divisible by 100
            unless the year is also evenly divisible by 400
            
Example:
The year 2000:
2000 / 4   = 500.0 (If divisble by 4 then Check divisiblity by 100, else not leap)
2000 / 100 = 20.0 (If divisible by 100 then Check divisibilty by 400, else LEAP)
2000 / 400 = 5.0 (If divisible by 400, then LEAP, else NOT LEAP)
The year 2000 is a leap year.

The year 2100:
2100 / 4   = 525.0 (Checking if divisible by 100)
2100 / 100 = 21.0  (Checking if divisible by 400)
2100 / 400 = 5.25  (If not divisible, then it is NOT LEAP!)
The year 2100 is not a leap year.
'''


year = int (input ("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print (f'{year} is a leap year.')
        else:
            print (f'{year} is not a leap year')
    else:
        print (f'{year} is a leap year')
else:
    print (f'{year} is not a leap year')
