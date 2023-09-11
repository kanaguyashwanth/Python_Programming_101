from prettytable import PrettyTable     #Importing prettytable CLASS

table = PrettyTable()                   # Object ---> table; Constructing an Object called 'table' from the Class 'PrettyTable' ---> !Pascal Casing!
# print(table)                          # Prints the barebones version of the table.

# NOTE: In order to add columns, we must first specify Field_Name: Pokemon which followed with a comma and LIST of Data.
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])        # table.add_column('Field_Name', [LIST])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

print(table)


# Changing the Alignment of Table - "l" for left, "c" for center and "r" for right
print(table.align)          # To check the current alignment
table.align = "l"
print(table)


"""
QUIZ:

Question 1:
In OOP what is the name of the blueprint for creating objects?

a. Attribute
b. Method
c. Class
d. Instance

ANSWER: c. Class



Question 2:
Given a Class blueprint for a Car has the following attributes and methods, which line of code in the answers will produce an error?

Attributes:
num_of_seats
speed

Methods:
drive()
brake()

a. car.drive()
b. car.num_of_seats = 2
c. car.brake() = 0
d. print(car.speed)

ANSWER: c. car.brake() = 0



Question 3:
my_toyota = Car()
my_fiat = Car()
What word would you use to describe what's inside my_toyota and my_fiat?

a. Class
b. Attribute
c. Variable
d. Object
e. Method

ANSWER: d. Object
"""
