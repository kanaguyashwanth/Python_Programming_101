# EXERCISE - MAZE

# Website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# CODE:

# EXAMPLE 5: MAZE

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

while not at_goal():
    
    if front_is_clear():
        if wall_on_right():
            move()
        else:
            move()
            
    elif wall_on_right() and wall_in_front():
        turn_left()
        
    elif wall_in_front() and not wall_on_right():
        turn_right()
        if front_is_clear():
            move()
            if right_is_clear():
                turn_right()