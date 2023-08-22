# Positional vs. Keyword Arguments

'''
NOTE:

POSITONAL ARGUMENTS:
def my_function(a, b, c): (More ERROR prone)
    #Do this with a
    #Then do this with b
    #Finally do this with c
    
my_function(1, 2, 3)


KEYWORD ARGUMENTS: (Less ERROR prone, but can make your code lil longer)
def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
    
my_function(a=1, b=2, c=3) or my_function(c=3, a=1, b=2)  #HERE, the position does not matter

'''

# Positional Arguments
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')
    
greet_with ("Yashwanth", "India")


# Keyword Arguments
def greet_with(NAME, LOCATION):
    print(f'Hello {NAME}')
    print(f'What is it like in {LOCATION}?')
greet_with (LOCATION= "Pune",NAME= "Max" )