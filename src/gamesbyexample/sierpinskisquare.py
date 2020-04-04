"""Sierpinski Square, by Al Sweigart al@inventwithpython.com
Draws the Sierpinski Square (also called Carpet) with turtle graphics.
More info at: https://en.wikipedia.org/wiki/Sierpinski_carpet"""
__version__ = 0
import turtle
turtle.tracer(100, 0) # Make the turtle draw faster.

# Setup the colors:
LIGHT_ORANGE = '#FFD78E'
BLUE = '#517DB2'
FG_COLOR = LIGHT_ORANGE
BG_COLOR = BLUE

def main():
    turtle.bgcolor(BG_COLOR)
    turtle.pencolor(FG_COLOR)

    # Start the recursive drawing:
    drawCarpet(-350, 350, 700, 700)

    turtle.update() # Finish drawing the screen.
    turtle.exitonclick() # When user clicks on the window, close it.


def drawCarpet(left, top, width, height):
    if width < 5 or height < 5:
        return

    # Draw the outer rectangle:
    turtle.penup()
    turtle.goto(left, top)
    turtle.pendown()
    turtle.fillcolor(FG_COLOR)

    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()

    www = width / 3.0
    hhh = height / 3.0

    # Draw the inner rectangle:
    turtle.penup()
    turtle.goto(left + www, top - hhh)
    turtle.pendown()
    turtle.fillcolor(BG_COLOR)

    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(www)
    turtle.right(90)
    turtle.forward(hhh)
    turtle.right(90)
    turtle.forward(www)
    turtle.right(90)
    turtle.forward(hhh)
    turtle.end_fill()

    # Recursive calls for the eight surrounding sections:

    # Draw in the top-left section:
    drawCarpet(left, top, www, hhh)
    # Draw in the top section:
    drawCarpet(left + www, top, www, hhh)
    # Draw in the top-right section:
    drawCarpet(left + (www * 2), top, www, hhh)
    # Draw in the left section:
    drawCarpet(left, top - hhh, www, hhh)
    # Draw in the right section:
    drawCarpet(left + (www * 2), top - hhh, www, hhh)
    # Draw in the bottom-left section:
    drawCarpet(left, top - (hhh * 2), www, hhh)
    # Draw in the bottom:
    drawCarpet(left + www, top - (hhh * 2), www, hhh)
    # Draw bottom-right:
    drawCarpet(left + (www * 2), top - (hhh * 2), www, hhh)


try:
    main()
except turtle.Terminator:
    pass # Do nothing when the turtle window is closed.
