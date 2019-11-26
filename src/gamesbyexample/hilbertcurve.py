# Hilbert Curve, by Al Sweigart al@inventwithpython.com
# Draws the Hilbert Curve fractal with turtle graphics.
# More info at: https://en.wikipedia.org/wiki/hilbertCurve
# Good videos on space-filling curves: https://youtu.be/RU0wScIj36o
# and https://youtu.be/3s7h2MHQtxc

import turtle

SIZE  = 10 # (!) Try changing the line length by a litte.
ANGLE = 90 # (!) Try changing the turning angle by a litte.
LEVEL = 5  # (!) Try changing the recursive level by a litte.

MAGENTA = '#B20059'
PINK = '#FFE6F2'
turtle.bgcolor(MAGENTA)
turtle.pencolor(PINK)
turtle.fillcolor(PINK)

turtle.tracer(1, 0) # Make the turtle draw faster.

turtle.penup()
turtle.goto(-320, 0)
turtle.pendown()

#turtle.setheading(20) # (!) Try uncommenting this line.

def hilbertCurve(level, angle):
    if level == 0:
        return

    turtle.right(angle)
    hilbertCurve(level - 1, -angle)
    turtle.forward(SIZE)
    turtle.left(angle)
    hilbertCurve(level - 1, angle)
    turtle.forward(SIZE)
    hilbertCurve(level - 1, angle)
    turtle.left(angle)
    turtle.forward(SIZE)
    hilbertCurve(level - 1, -angle)
    turtle.right(angle)

def filledInHilbert():
    turtle.begin_fill()
    hilbertCurve(LEVEL, ANGLE) # draw first quadrant
    turtle.forward(SIZE)

    hilbertCurve(LEVEL, ANGLE) # draw second quadrant
    turtle.left(ANGLE)
    turtle.forward(SIZE)
    turtle.left(ANGLE)

    hilbertCurve(LEVEL, ANGLE) # draw third quadrant
    turtle.forward(SIZE)

    hilbertCurve(LEVEL, ANGLE) # draw fourth quadrant
    turtle.left(ANGLE)
    turtle.forward(SIZE)
    turtle.left(ANGLE)
    turtle.end_fill()

filledInHilbert()
turtle.update() # Finish drawing the screen.
turtle.exitonclick() # When user clicks on the window, close it.
