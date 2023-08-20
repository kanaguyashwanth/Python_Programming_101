# EXAMPLE 3: (Make the robot jump if there are hurdles and move if there aren't and stop at flag[Randomly generated])

# Website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Hurdle 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def move_forward():
    if front_is_clear():
        while front_is_clear() and not at_goal():
            move()


if wall_in_front():
    while wall_in_front():
        jump_hurdle()
        move_forward()
else:
    move_forward()
