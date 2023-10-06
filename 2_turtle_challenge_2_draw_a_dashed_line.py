#STEPS:
'''
1. Import turtle, screen Classes from Package 'Turtle'
2. Create Object from the Class
3. Calling Methods
4. Use loops for efficiency
'''

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape('turtle')


for n in range(4):
    for n in range(10):
        tim.forward(10)
        tim.color('white')
        tim.forward(10)
        tim.color('black')

    tim.right(90)




screen.exitonclick()
