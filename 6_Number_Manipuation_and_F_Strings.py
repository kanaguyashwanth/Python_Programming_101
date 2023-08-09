# Manipulating Numbers - ROUND, FLOOR DIVISION


# ROUNDING NUMBERS:
print (8 / 3)
print (int(8 / 3))      # CHOPS OFF THE VALUES AFTER DECIMAL PLACES 2.6 ---> 2
print (round(8 / 3))    # Next number if decimal is 5 or greater    2.6 ---> 3
print (round(8 / 3, 2)) # Rounding to 2 decimal places


# FLOOR DIVISION
print (8 // 3)			# FLOOR DIVISION ---> Results in INTEGER not FLOAT!
print (type(8 // 3))    # Floor division results in Integer


# Extras
result = 4 / 2
result /= 2				# result = result / 2, result += 2, result -= 2
print (result)


# F-string (Printing Multiple datatypes using same print statement) - Eliminating type conversions
'''
SYNTAX: f"your score is {score}, your height is {height}, you are winning is {isWinning}"
'''
# Below, it has 3 different datatypes and it is tedious to change their types and then print, use fstring instead
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
