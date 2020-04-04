"""Koch Snowflake, by Al Sweigart al@inventwithpython.com
Draws a Koch snowflake fractal with turtle graphics."""
__version__ = 0
import turtle
turtle.tracer(1, 0) # Make the turtle draw faster.

LEVELS = 5 # More than 5 levels becomes too small to see.

def main():
    # Move turtle into the starting position:
    LENGTH = 300.0
    turtle.penup()
    turtle.backward(LENGTH / 2.0)
    turtle.right(90)
    turtle.backward(1.75 * LENGTH / 2.0)
    turtle.left(90)
    turtle.pendown()

    # Draw the snowflake:
    for lev in range(LEVELS):
        drawSnowflake(LENGTH, lev)

    turtle.update() # Finish drawing the screen.
    turtle.exitonclick() # When user clicks on the window, close it.


def snowflakeSide(sideLength, levels):
    # Draw a single side of the snowflake (this is called a Koch curve):
    turtle.pencolor('black')
    if levels == 0:
        turtle.forward(sideLength)
        return
    sideLength = sideLength / 3.0
    snowflakeSide(sideLength, levels-1)

    # "Erase" the middle segment by drawing a white line over it.
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.forward(sideLength)
    turtle.forward(-sideLength)
    turtle.pencolor('black')
    turtle.pensize(1)

    turtle.left(60)
    snowflakeSide(sideLength, levels-1)
    turtle.right(120)
    snowflakeSide(sideLength, levels-1)
    turtle.left(60)
    snowflakeSide(sideLength, levels-1)


def drawSnowflake(sideLength, levels):
    # Draw 6 Koch curves to draw a Koch snowflake.
    for i in range(6):
        snowflakeSide(sideLength, levels)
        turtle.right(60)


try:
    main()
except turtle.Terminator:
    pass # Do nothing when the turtle window is closed.
