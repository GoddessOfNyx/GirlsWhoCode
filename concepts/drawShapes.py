from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)

### Write your code below:

def drawPolygon(sideSize): #Creates the function that draws a polygon
    sides = int(input('How many sides?'))
    degrees = 360 #determines the amount of degrees that the pen turns
    color = input('What color would you like the shape to be?')

    degrees /= sides #Degrees the pen turns to make a shape
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.goto(0,0) #Resets position
    while sides > 0:
        t.forward(sideSize)
        t.right(degrees)
        sides -= 1
    t.end_fill()

def drawCircles(sideSize): #creates a function that draws a circle
    radius = 50
    color = input('What color would you like the shape to be?')
    userCircle = input('Do you want a full circle or half of a circle?')

    if userCircle == 'full' or 'full circle' or 'a full circle':
        extent = 360
    if (userCircle == 'half') or (userCircle == 'half circle') or (userCircle == 'a half circle'):
        extent = 180

    print(extent)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.goto(0,0)
    t.circle(radius, extent, sideSize)
    t.end_fill()

sideSize = 50
shape = str(input('Do you want to draw a polygon or a circle?'))
if shape == 'circle':
    drawCircles(sideSize)
elif shape == 'polygon':
    drawPolygon(sideSize)

# Close window on click.
exitonclick()
