"""Lawn mower, by Al Sweigart al@inventwithpython.com

Watch grass get cut and grow again. Press Ctrl-C to stop.
Inspired by Tondeuse by Jules Villard, https://asciinema.org/a/21743
https://bitbucket.org/jvillard/tondeuse/src/default/
Tags: large, artistic"""
__version__ = 0

import time, random, sys

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

# Set up the constants:
# Constants for the size of the grass field:
WIDTH = 79
HEIGHT = 22

# Constants for the mower text:
FACE = chr(9786)  # The '☺' character.
MOWER_RIGHT = FACE + "`.=."
MOWER_LEFT = ".=.'" + FACE
MOWER_LEN = 5

MOWING_PAUSE = 0.1  # (!) Try changing this to 0.01.
GROWING_PAUSE = 0.001

assert len(MOWER_RIGHT) == MOWER_LEN
assert len(MOWER_LEFT) == MOWER_LEN


def main():
    """Run the lawn mower animation."""

    # Draw the initially uncut grass field:
    bext.clear()

    if sys.platform == 'win32':
        bext.hide()  # (Hiding the cursor only works on Windows.)

    bext.fg('green')
    for i in range(HEIGHT):
        print(';' * WIDTH)
    print('Press Ctrl-C to quit.')

    # mowerx and mowery is the left edge of the mower, despite direction.
    mowerx = -MOWER_LEN
    mowery = 0
    mowerDirection = 'right'
    growMode = False

    while True:  # Main program loop.
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
            mowerx += 1  # Move the mower right.
            if mowerx > WIDTH:
                # After going past the right edge,
                # change position and direction.
                mowerDirection = 'left'
                mowery += 1
                if mowery == HEIGHT:
                    # Done mowing, let the grass grow back:
                    growMode = True
        elif mowerDirection == 'left':
            mowerx -= 1  # Move the mower left.
            if mowerx < -MOWER_LEN:
                # After going past the left edge,
                # change position and direction.
                mowerDirection = 'right'
                mowery += 1
                if mowery == HEIGHT:
                    # Done mowing, let the grass grow back.
                    growMode = True
        sys.stdout.flush()  # (Required for bext-using programs.)

        time.sleep(MOWING_PAUSE)  # Pause after mowing.

        if growMode:
            # Let the grass grow back one at a time:
            mowerx = -MOWER_LEN  # Reset mower position.
            mowery = 0  # Reset mower position.
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
                time.sleep(GROWING_PAUSE)  # Pause after growing.
            growMode = False  # Done growing grass.
        # At this point, go back to the start of the main program loop.


def drawMower(mowerx, mowery, direction):
    """Draw the lawn mower with its left edge at mowerx, mowery."""
    bext.fg('red')
    if direction == 'right':
        mowerText = MOWER_RIGHT
    elif direction == 'left':
        mowerText = MOWER_LEFT

    for i in range(MOWER_LEN):
        if 0 <= mowerx + i < WIDTH:
            bext.goto(mowerx + i, mowery)
            print(mowerText[i], end='')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
