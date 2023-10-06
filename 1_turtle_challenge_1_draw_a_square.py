# STEPS:
'''
1. Import turtle, screen Classes from Package 'turtle'
2. Create object from the class
3. Calling methods
4. Use loops for efficiency
'''

from turtle import Turtle, Screen

# Importing Modules
'''
WHILE IMPORTING, IF IT THROWS AN ERROR, THEN IT MIGHT NOT BE INSTALLED WITH PY STANDARD LIBRARY.
from turtle import Turtle
from turtle import *
from random import *
'''

# Working with Aliases
'''
keyword module_name  keyword   alias_name
import  turtle       as        t
'''

tim = Turtle()
screen = Screen()

# Methods:
# SHAPE:
tim.shape("turtle")

# COLOR:
tim.color("blue")

# MOTION(Distance units) & DIRECTION(Angle):

for n in range(4):
    tim.forward(100)    # MOTION
    tim.right(90)       # DIRECTION


screen.exitonclick()
