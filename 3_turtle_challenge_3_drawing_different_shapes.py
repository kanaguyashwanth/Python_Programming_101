#CHALLENGE: Draw the following shapes - One side common for all shapes, each shape must be a random colour, all shapes in sequence.
# 1. Triangle,
# 2. Square,
# 3. Pentagon,
# 4. Hexagon,
# 5. Heptagon,
# 6. Octagon,
# 7. Nonagon,
# 8. Decagon.

'''
Finding angles for each shape:
( (180 * num_of_sides) - 360 ) / num_of_sides

Turning angle, (180 - shape_angle)
'''

#STEPS:
'''
1. Import CLASSES - turtle, screen from PACKAGE 'turtle'
2. Create OBJECTS from CLASSES
3. Calling METHODS
4. Using loops (if needed)
'''

from turtle import Turtle, Screen
import random

random_num = random.randint(0, 255)
# print(random_num)

tim = Turtle()
tim.shape('turtle')

screen = Screen()
# Colormode() - To resolve 'bad color sequence' error.
screen.colormode()      # Prints current color mode = 1
screen.colormode(255)   # Color mode is being set to 255
screen.colormode()      # Prints current colour mode = 255




# 1. TRIANGLE:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(3):
    tim.forward(100)
    tim.right(120)




# 2. SQUARE:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(4):
    tim.forward(100)
    tim.right(90)




# 3. PENTAGON:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(5):
    tim.forward(100)
    tim.right(72)




# 4. HEXAGON:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(6):
    tim.forward(100)
    tim.right(60)




# 5. HEPTAGON:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(7):
    tim.forward(100)
    tim.right(51.428571429)




# 6. OCTAGON:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(8):
    tim.forward(100)
    tim.right(45)




# 7. NONAGON:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(9):
    tim.forward(100)
    tim.right(40)




# 7. DECAGON:
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
tim.pencolor(a, b, c)

for n in range(10):
    tim.forward(100)
    tim.right(36)

screen.exitonclick()
