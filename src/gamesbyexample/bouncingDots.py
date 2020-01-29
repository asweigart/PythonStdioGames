"""Bouncing Dots, by Al Sweigart al@inventwithpython.com

A bouncing dots animation. Press Ctrl-C to stop."""
__version__ = 1

import sys, random, time

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

# Setup the constants:
WIDTH, HEIGHT = bext.size()
WIDTH -= 1  # Adjustment for Windows Command Prompt.
NUMBER_OF_DOTS = 35
COLORS = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
DOT_CHAR  = 'O'

# Key names for dot dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    """Run the bouncing dots program."""
    bext.clear()

    # Generate some dots.
    dots = []
    for i in range(NUMBER_OF_DOTS):
        dots.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 2),
                      Y: random.randint(1, HEIGHT - 2),
                      DIR: random.choice(DIRECTIONS)})

    while True:  # Main program loop.
        oldDotPositions = []

        for dot in dots:
            # Draw our dots:
            bext.goto(dot[X], dot[Y])
            bext.fg(dot[COLOR])
            print(DOT_CHAR, end='')

            oldDotPositions.append((dot[X], dot[Y]))
        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(0.1)

        for dot in dots:
            # Move our dots:
            if dot[DIR] == UP_RIGHT:
                dot[X] += 1
                dot[Y] -= 1
            elif dot[DIR] == UP_LEFT:
                dot[X] -= 1
                dot[Y] -= 1
            elif dot[DIR] == DOWN_RIGHT:
                dot[X] += 1
                dot[Y] += 1
            elif dot[DIR] == DOWN_LEFT:
                dot[X] -= 1
                dot[Y] += 1

            # See if our dots bounce off the corners:
            if dot[X] == 0 and dot[Y] == 0:
                dot[DIR] = DOWN_RIGHT
            elif dot[X] == 0 and dot[Y] == HEIGHT - 1:
                dot[DIR] = UP_RIGHT
            elif dot[X] == WIDTH - 1 and dot[Y] == 0:
                dot[DIR] = DOWN_LEFT
            elif dot[X] == WIDTH - 1 and dot[Y] == HEIGHT - 1:
                dot[DIR] = UP_LEFT

            # See if our dots bounce off the walls:
            elif dot[X] == 0 and dot[DIR] == UP_LEFT:
                dot[DIR] = UP_RIGHT
            elif dot[X] == 0 and dot[DIR] == DOWN_LEFT:
                dot[DIR] = DOWN_RIGHT

            elif dot[X] == WIDTH - 1 and dot[DIR] == UP_RIGHT:
                dot[DIR] = UP_LEFT
            elif dot[X] == WIDTH - 1 and dot[DIR] == DOWN_RIGHT:
                dot[DIR] = DOWN_LEFT

            elif dot[Y] == 0 and dot[DIR] == UP_LEFT:
                dot[DIR] = DOWN_LEFT
            elif dot[Y] == 0 and dot[DIR] == UP_RIGHT:
                dot[DIR] = DOWN_RIGHT

            elif dot[Y] == HEIGHT - 1 and dot[DIR] == DOWN_LEFT:
                dot[DIR] = UP_LEFT
            elif dot[Y] == HEIGHT - 1 and dot[DIR] == DOWN_RIGHT:
                dot[DIR] = UP_RIGHT

        for position in oldDotPositions:
            # Erase all of the dots.
            bext.goto(position[0], position[1])
            print(' ', end='')
        # At this point, go back to the start of the main program loop.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
