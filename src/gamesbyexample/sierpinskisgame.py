"""Sierpinkski's Game, by Al Sweigart al@inventwithpython.com

Sierpinkski's "game" is an algorithm that draws Sierpinski's Triangle
with turtle graphics.
More info at https://en.wikipedia.org/wiki/Chaos_game"""
__version__ = 0

import turtle
import random, time
turtle.tracer(60, 0) # Make the turtle draw faster.
turtle.setworldcoordinates(0, 0, 960, 810)

DOT_SIZE = 3
NUMBER_OF_DOTS = 1500

def main():
    turtle.bgcolor(0.1, 0.1, 0.1)
    turtle.penup()
    while True:
        # Pick a random color to draw with:
        redAmount = random.randint(50, 100) / 100.0
        greenAmount = random.randint(50, 100) / 100.0
        blueAmount = random.randint(50, 100) / 100.0
        turtle.pencolor(redAmount, greenAmount, blueAmount)

        # Pick three random points for the triangle:
        ax = random.randint(0, 960)
        ay = random.randint(0, 810)
        bx = random.randint(0, 960)
        by = random.randint(0, 810)
        cx = random.randint(0, 960)
        cy = random.randint(0, 810)

        # Play Sierpinski's Game to draw Sierpinski's Triangle:
        playSierpinskisGame(ax, ay, bx, by, cx, cy)

        time.sleep(2) # Pause for two seconds before clearing the screen.
        turtle.clear()


def halfway(x1, y1, x2, y2):
    # Find the distance halfway between x1, y1 and x2, y2:
    if x1 > x2:
        halfwayx = int(abs(x1 - x2) / 2.0) + x2
    else:
        halfwayx = int(abs(x2 - x1) / 2.0) + x1

    if y1 > y2:
        halfwayy = int(abs(y1 - y2) / 2.0) + y2
    else:
        halfwayy = int(abs(y2 - y1) / 2.0) + y1

    return (halfwayx, halfwayy)


def playSierpinskisGame(ax, ay, bx, by, cx, cy):
    # Start the point at ax, ay:
    px = ax
    py = ay

    # Draw dots:
    for i in range(NUMBER_OF_DOTS):
        # Pick a random triangle point to move towards:
        random_point = random.randint(1, 3)

        # Move halfway to that point:
        if random_point == 1:
            # Move halfway to point A:
            px, py = halfway(px, py, ax, ay)
            turtle.goto(px, py)
            turtle.dot(DOT_SIZE) # Mark the dot.
        elif random_point == 2:
            # Move halfway to point B:
            px, py = halfway(px, py, bx, by)
            turtle.goto(px, py)
            turtle.dot(DOT_SIZE) # Mark the dot.
        elif random_point == 3:
            # Move halfway to point C:
            px, py = halfway(px, py, cx, cy)
            turtle.goto(px, py)
            turtle.dot(DOT_SIZE) # Mark the dot.
    turtle.update() # Finish drawing the screen.


try:
    main()
except turtle.Terminator:
    pass # Do nothing when the turtle window is closed.
