# Nonuniform Fractal Tree Drawer, by Al Sweigart al@inventwithpython.com
# Draws nonuniform fractal trees with turtle graphics.
__version__ = 1

import turtle
import random
import time

PALE_TAN = '#FEF9EE'
DARK_BROWN = '#130d0f'
turtle.bgcolor(PALE_TAN)
turtle.pencolor(DARK_BROWN)

turtle.tracer(10000, 0) # Make the turtle draw faster.

def drawBranch(x, y, direction, branchLength):
    # if the branch is too small, just quit
    if branchLength < 5:
        return

    # Draw the branch:
    branchThickness = max(branchLength / 7.0, 1) + random.randint(-1, 1)
    turtle.pensize(branchThickness)
    for i in range(4):
        turtle.forward(branchLength / 4.0 + random.randint(-10, 10))
        turtle.left(random.randint(-8, 8))

        if random.randint(0, 5) == 0:
            tinyBranchAngle = random.randint(-LEFT_ANGLE, RIGHT_ANGLE)
            turtle.right(tinyBranchAngle)
            drawBranch(turtle.xcor(), turtle.ycor(), turtle.heading(), branchLength / 2)
            turtle.left(tinyBranchAngle)
            turtle.pensize(branchThickness)

    if random.randint(0, 5) == 0:
        branchLength = branchLength * 0.9

    # Draw the two recursive branches:
    if random.randint(0, 9) != 0:
        turtle.left(LEFT_ANGLE)
        drawBranch(turtle.xcor(), turtle.ycor(), turtle.heading(), branchLength - LEFT_DECREASE)
        turtle.right(LEFT_ANGLE)

    if random.randint(0, 9) != 0:
        turtle.right(RIGHT_ANGLE)
        drawBranch(turtle.xcor(), turtle.ycor(), turtle.heading(), branchLength - RIGHT_DECREASE)
        turtle.left(RIGHT_ANGLE)

    # Return back to the starting point:
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(direction)
    turtle.pendown()

def drawTree(x, y, direction, seed):
    global LEFT_ANGLE, RIGHT_ANGLE, LEFT_DECREASE, RIGHT_DECREASE

    # Go to the starting point:
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(direction)
    turtle.pendown()

    # Try changing these values and looking at the results:
    random.seed(seed)
    LEFT_ANGLE     = random.randint(10,  30)
    RIGHT_ANGLE    = random.randint(10,  30)
    LEFT_DECREASE  = random.randint( 6,  15)
    RIGHT_DECREASE = random.randint( 6,  15)
    START_SIZE     = random.randint(80, 120)

    # Draw the tree:
    drawBranch(x, y, direction, START_SIZE)
    turtle.update() # Finish drawing the screen.

seed = 0
while True:
    # Get psuedorandom numbers for the branch properties:
    random.seed(seed)
    drawTree(0, -310, 90, seed)
    time.sleep(2)
    turtle.clear()
    seed += 1

turtle.update() # Finish drawing the screen.
turtle.exitonclick() # When user clicks on the window, close it.
