# Lawnmower, by Al Sweigart al@inventwithpython.com
# A simple screensaver. Watch grass get cut and grow again.
# Inspired by Tondeuse by Jules Villard, https://asciinema.org/a/21743
# https://bitbucket.org/jvillard/tondeuse/src/default/

"""
This program requires the bext module, which you can install by opening
a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python3 -m pip install --user bext
"""

import time, random, bext

# Constants for the size of the grass field:
WIDTH = 79
HEIGHT = 24

# Constants for the mower text:
FACE = chr(9786)
MOWER_RIGHT = FACE + "`.=."
MOWER_LEFT  = ".=.'" + FACE
MOWER_LEN = 5

assert len(MOWER_RIGHT) == MOWER_LEN
assert len(MOWER_LEFT) == MOWER_LEN


def drawMower(x, y, direction):
    bext.fg('red')
    if direction == 'right':
        mowerText = MOWER_RIGHT
    elif direction == 'left':
        mowerText = MOWER_LEFT

    for i in range(MOWER_LEN):
        if 0 <= mowerx + i < WIDTH:
            bext.goto(x + i, mowery)
            print(mowerText[i], end='')


# Draw the initially uncut grass field:
bext.clear()
bext.hide()
bext.fg('green')
for i in range(HEIGHT):
    print(';' * WIDTH)
print('Press Ctrl-C to quit.')

# mowerx and mowery refer to the left edge of the lower, despite direction.
mowerx = -MOWER_LEN
mowery = 0
mowerDirection = 'right'
growMode = False

while True:
    # Draw the mower:
    drawMower(mowerx, mowery, mowerDirection)

    # Draw the cut grass:
    if (mowerDirection == 'right') and (mowerx - 1 >= 0):
        bext.goto(mowerx - 1, mowery)
        bext.fg('green')
        print(',', end='')
    elif (mowerDirection == 'left') and (mowerx < WIDTH - MOWER_LEN):
        bext.goto(mowerx + MOWER_LEN, mowery)
        bext.fg('green')
        print(',', end='')

    # Move the mower:
    if mowerDirection == 'right':
        mowerx += 1 # Move the mower right.
        if mowerx > WIDTH:
            # After going past the right edge, change position and direction.
            mowerDirection = 'left'
            mowery += 1
            if mowery == HEIGHT:
                growMode = True # Done mowing, let the grass grow back.
    elif mowerDirection == 'left':
        mowerx -= 1 # Move the mower left.
        if mowerx < -MOWER_LEN:
            # After going past the left edge, change position and direction.
            mowerDirection = 'right'
            mowery += 1
            if mowery == HEIGHT:
                growMode = True # Done mowing, let the grass grow back.
    time.sleep(0.4) # Pause after mowing.

    if growMode:
        # Let the grass grow back one at a time:
        mowerx = -MOWER_LEN # Reset mower position.
        mowery = 0 # Reset mower position.
        bext.fg('green')

        # Create a set of all the places the grass needs to grow:
        grassToGrow = set()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                grassToGrow.add((x, y))

        # Grow the grass:
        while len(grassToGrow) > 0:
            x, y = random.sample(grassToGrow, 1)[0]
            grassToGrow.remove((x, y))
            bext.goto(x, y)
            print(';')
            time.sleep(0.4)
        growMode = False # Done growing grass.
