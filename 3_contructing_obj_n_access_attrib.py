"""

"""



"""
import another_module
print(another_module.another_variable)
"""

"""
# Turtle Module
import turtle
timmy = turtle.Turtle()
"""

# OR

# CONSTRUCTING A NEW OBJECT
from turtle import Turtle, Screen
timmy = Turtle()        #    car = CarBlueprint()    obj <-----> class
print(timmy)            #    the object is being saved at a memory location
timmy.shape("turtle")

# CHALLENGE 1: Change the color of the turtle ---> https://cs111.wellesley.edu/reference/colors
timmy.color("cadetBlue")

# CHALLENGE 2: Move the turtle forward by 100 paces ---> https://docs.python.org/3/library/turtle.html
timmy.forward(100)

# OBJECT ATTRIBUTES
"""
car.speed  ---> Identifies the object, from this object, get the speed attribute
"""
my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()


# METHODS:
"""
ATTRIBUTE:
speed = 0
fuel = 32

METHODS:
def move():
    speed = 60
    
def stop():
    speed = 0

GETTING HOLD OF OBJECT AND CALLING FUNCTION: [ object.method() ]
car.stop()
"""
