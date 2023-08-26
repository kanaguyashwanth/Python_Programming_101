# Exercise - Days in Month [If leap year, then display 29 days as output or else 28 days if it is not a leap year]

'''
Input:
year-2022
month-2

Output: (February number of days)
28

Input:
year-2022
month-3

Output: (March number of days)
31
'''


# Leap Year Condition
'''
-> If divisible by 4, 100 and 400 - Leap
-> If NOT divisible by 100 - Leap         [Skipping centuries]
-> If NOT divisible by 4   - Not leap year
-> If NOT divisible by 400 - Not leap year
'''

def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                #print("Leap Year.")
                return "Leap year"
            else:
                #print("Not leap year.")
                return "Not leap year"
        else:
            #print("Leap year.")
            return "Leap year"
    else:
        #print("Not leap year.")
        return "Not leap year"
    
        
def days_in_month(year, month):
    
    # Valid input
    if month < 0 or month > 12:
        return "Enter a valid month."
    
    # If not a leap year
    if lp == "Not leap year":
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # If leap year
    elif lp == "Leap year":
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Days
    for n in range (len(month_days)-1):
        if month == n:
            return month_days[n-1]

year = int (input("Enter a year: "))
lp = leap_year(year)
month = int (input("Enter a month: "))
days = days_in_month(year, month)
print(days)