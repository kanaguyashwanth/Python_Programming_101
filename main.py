'''
Turtle Graphics,
Tuples,
Importing Modules
'''

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()                  # Object -> timmy_the_turtle(variable which contains object), Class -> Turtle()

# Methods - Shape, Color(Tk Color specification string), Motion, Direction
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("brown")              # Color - https://trinket.io/docs/colors
# timmy_the_turtle.pencolor("aquamarine")    # https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html

# Motion
timmy_the_turtle.forward(100)

# Direction
timmy_the_turtle.right(90)


'''
How to use these modules?
- Documentation
'''

screen = Screen()
screen.exitonclick()
