"""Pythons, by Al Sweigart al@inventwithpython.com
Drawing pythons with turtle graphics."""
__version__ = 0
import turtle
import random

turtle.tracer(100, 0) # Make the turtle draw faster.

NUMBER_OF_SNAKES = 1
GAP = 10
THICKNESS = 20
SNAKE_COLORS = ['#71BF2E', '#4C7F1E', '#97FF3D', '#26400F', '#88E537']

def main():
    turtle.pensize(4)
    # Draw the snakes:
    for i in range(10):
        # Go to the starting position:
        turtle.penup()
        turtle.goto(random.randint(-400, 400), random.randint(-400, 400))
        turtle.pendown()
        turtle.setheading(random.randint(0, 360))

        # Set up the snake coloration:
        turtle.pencolor(random.choice(SNAKE_COLORS))

        # (!) Uncomment the following 4 lines to use random colors.
        #redAmount = random.randint(0, 100) / 100.0
        #greenAmount = random.randint(0, 100) / 100.0
        #blueAmount = random.randint(0, 100) / 100.0
        #turtle.pencolor(redAmount, greenAmount, blueAmount)

        turtle.fillcolor(turtle.pencolor())

        # Draw the snake:
        lengths = []
        # Each snake has a random amount of segments:
        for j in range(random.randint(6, 12)):
            # Each segment has random lengths:
            lengths.append(random.randint(40, 150))
        # Draw the segments:
        drawSnake(lengths)

    turtle.update() # Finish drawing the screen.
    turtle.exitonclick() # When user clicks on the window, close it.


def drawSnakeHead(length):
    turtle.begin_fill()
    final_position = turtle.position()
    turtle.left(90)
    turtle.forward(length - THICKNESS)
    turtle.left(90)
    turtle.forward(THICKNESS * 3)
    turtle.left(90)
    turtle.forward(THICKNESS / 2.0)
    turtle.right(90) # draw tongue
    turtle.forward(THICKNESS)
    turtle.right(45)
    turtle.forward(THICKNESS / 3.0)
    turtle.backward(THICKNESS / 3.0)
    turtle.left(90)
    turtle.forward(THICKNESS / 3.0)
    turtle.backward(THICKNESS / 3.0)
    turtle.right(45)
    turtle.backward(THICKNESS)
    turtle.left(90) # end tongue
    turtle.forward(THICKNESS / 2.0)
    turtle.left(90)
    turtle.forward(THICKNESS * 2)
    turtle.right(90)
    turtle.forward(length - THICKNESS)
    turtle.left(90)
    turtle.forward(THICKNESS)
    turtle.penup()
    turtle.goto(final_position)
    turtle.left(90)
    turtle.forward(length - THICKNESS * 1.3)
    turtle.left(90)
    turtle.forward(THICKNESS * 1.5)
    turtle.dot(8, 'black') # The snake's eye is black.
    turtle.backward(THICKNESS * 1.5)
    turtle.right(90)
    turtle.backward(length - THICKNESS * 1.3)
    turtle.right(90)
    turtle.pendown()
    turtle.end_fill()


def drawTwistUpSegment(length):
    turtle.begin_fill()
    turtle.forward(GAP)
    turtle.left(90)
    turtle.forward(length - THICKNESS)
    turtle.right(90)
    turtle.forward(THICKNESS)
    final_position = turtle.position()
    turtle.right(90)
    turtle.penup()
    turtle.forward(THICKNESS)
    turtle.pendown()
    turtle.forward(length - THICKNESS)
    turtle.right(90)
    turtle.forward(THICKNESS + GAP)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(final_position)
    turtle.pendown()
    turtle.right(180)


def drawTwistDownSegment(length):
    turtle.begin_fill()
    turtle.forward(GAP + THICKNESS)
    turtle.right(90)
    turtle.forward(length - THICKNESS)
    final_position = turtle.position()
    turtle.penup()
    turtle.forward(THICKNESS)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(THICKNESS)
    turtle.right(90)
    turtle.forward(length - THICKNESS)
    turtle.left(90)
    turtle.forward(GAP)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(final_position)
    turtle.pendown()
    turtle.right(180)

def drawSnake(lengths):
    drawSnakeHead(lengths[0])
    for i in range(1, len(lengths) - 1, 2):
        drawTwistUpSegment(lengths[i])
        drawTwistDownSegment(lengths[i + 1])


try:
    main()
except turtle.Terminator:
    pass # Do nothing when the turtle window is closed.
