# CHALLENGE:


'''
STEPS:
1. Import CLASSES - Turtle, Screen from PACKAGE - 'turtle'
2. Create OBJECTS from CLASSES
3. Calling METHODS
4. Using Loops
'''

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
screen = Screen()
screen.colormode(255)
random_num = random.randint(0, 255)
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(500):
    # Random Colour
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.pencolor(a, b, c)

    # Motion
    tim.forward(30)

    # Direction
    direction = random.choice(directions)
    tim.setheading(direction)

screen.exitonclick()
