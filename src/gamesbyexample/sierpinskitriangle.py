"""Sierpinski Triangle, by Al Sweigart al@inventwithpython.com
Draws the Sierpinski Triangle fractal with turtle graphics."""
__version__ = 0
import turtle
import math

turtle.tracer(1000, 0) # Make the turtle draw faster.
turtle.setworldcoordinates(0, 0, 960, 810)

BASE_SIZE = 13
BASE_HEIGHT = BASE_SIZE * math.sin(60 * (math.pi / 180))
START_X = 50
START_Y = 20

def main():
    turtle.bgcolor(0.9, 0.9, 0.9)

    # Loop from 5 to 0, drawing 5 levels of triangles:
    for i in range(5, -1, -1):
        red = 1 - (0.2 * i)
        green = 0.1 * i
        blue = 0.1 * i
        drawSierpinski(START_X, START_Y, i, (red, green, blue))

    turtle.hideturtle()
    turtle.update() # Finish drawing the screen.
    turtle.exitonclick() # When user clicks on the window, close it.


def drawTriangle(x, y, color):
    turtle.penup()
    turtle.pencolor(color)
    turtle.goto(x, y) # Go to bottom-left corner of the triangle.
    turtle.pendown()
    turtle.setheading(60)
    turtle.forward(BASE_SIZE) # Draw first side.
    turtle.right(120)
    turtle.forward(BASE_SIZE) # Draw second side.
    turtle.right(120)
    turtle.forward(BASE_SIZE) # Draw third side.

def drawSierpinski(x, y, level, color):
    if level == 0:
        # The base case, where triangles are too small to draw more.
        drawTriangle(x, y, color)
        drawTriangle(x + (BASE_SIZE * 0.5), y + BASE_HEIGHT, color)
        drawTriangle(x + BASE_SIZE, y, color)
    else:
        # The recursive case, where three more triangles are drawn.
        drawSierpinski(x, y, level - 1, color)
        drawSierpinski(x + (BASE_SIZE * 0.5 * (2 ** level)), y + (BASE_HEIGHT * (2 ** level)), level - 1, color)
        drawSierpinski(x + (BASE_SIZE * (2 ** level)), y, level - 1, color)


try:
    main()
except turtle.Terminator:
    pass # Do nothing when the turtle window is closed.
