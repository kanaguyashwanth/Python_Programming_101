# While loop - Loop will continue to go while a particular condition is satisfied

'''
for loop versions:

for item in list_of_items:
    #Do something to each item
    
    OR
    
for number in range (a, b):
    print(number)
    
    
    
while loop:

while something_is_true:
    #Do something repeatedly
'''

# Reborg's World:

# Website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json


# EXAMPLE 1: (Number of Hurdles)

# HURDLE JUMP using WHILE LOOP

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump_hurdle()
    number_of_hurdles -= 1
    print (number_of_hurdles)
    
    
    
# EXAMPLE 2: (We do not know where the flag is now!)

# Hurlde 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    jump_hurdle()

