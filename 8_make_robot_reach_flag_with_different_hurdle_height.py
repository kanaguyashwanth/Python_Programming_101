# EXERCISE - Make the robot reach the flag where hurdles are of different heights

# Website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# EXAMPLE 4: (Make the robot jump if there are hurdles of different height)
​
def turn_right():
    turn_left()
    turn_left()
    turn_left()
​
def jump_hurdle():
    turn_left()
    while wall_on_right():
        move()
    
    turn_right()
    move()
    
    turn_right()
    while not wall_on_right():
        move()
        while wall_on_right() and front_is_clear():
            move()
​
    turn_left()
​
while not at_goal():
    if wall_in_front():
        jump_hurdle()
    elif not wall_in_front():
        move()
