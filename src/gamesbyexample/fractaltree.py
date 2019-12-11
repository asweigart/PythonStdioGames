# Fractal Tree Drawer, by Al Sweigart al@inventwithpython.com
# Draws fractal trees with turtle graphics.
__version__ = 1

import random
import time
import turtle

turtle.tracer(1000, 0) # Make the turtle draw faster.
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

def drawBranch(startPosition, direction, branchLength):
    if branchLength < 5:
        # Base case; the branches are two small to keep drawing more:
        return

    # Go to the starting point & direction:
    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(direction)

    # Draw the branch (thickness is 1/7 the length):
    turtle.pendown()
    turtle.pensize(max(branchLength / 7.0, 1))
    turtle.forward(branchLength)

    # Record the position of the branch's end:
    endPosition = turtle.position()
    leftDirection = direction + LEFT_ANGLE
    leftBranchLength = branchLength - LEFT_DECREASE
    rightDirection = direction - RIGHT_ANGLE
    rightBranchLength = branchLength - RIGHT_DECREASE

    # Recursive case; draw two more branches:
    drawBranch(endPosition, leftDirection, leftBranchLength)
    drawBranch(endPosition, rightDirection, rightBranchLength)

try:
    seed = 0
    while True: # Main program loop.
        # Get psuedorandom numbers for the branch properties:
        random.seed(seed)
        LEFT_ANGLE     = random.randint(10,  30)
        LEFT_DECREASE  = random.randint( 6,  15)
        RIGHT_ANGLE    = random.randint(10,  30)
        RIGHT_DECREASE = random.randint( 6,  15)
        START_LENGTH   = random.randint(80, 120)

        # Write out the seed number:
        turtle.clear()
        turtle.penup()
        turtle.goto(10, 10)
        turtle.write('Seed: %s' % (seed))

        # Draw the tree:
        drawBranch((350, 10), 90, START_LENGTH)
        turtle.update() # Finish drawing the screen.
        time.sleep(2)

        seed = seed + 1 # Use the next number for the next seed.
        # At this point, go back to the start of the main program loop.
except turtle.Terminator:
    pass # Do nothing when the turtle window is closed.
