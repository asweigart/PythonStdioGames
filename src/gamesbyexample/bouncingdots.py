"""Bouncing Dots, by Al Sweigart al@inventwithpython.com
A bouncing dots animation. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
This and other games are available at https://nostarch.com/XX
Tags: short, artistic, bext, terminal"""
__version__ = 0
import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_DOTS = 35  # (!) Try changing this to 1 or 100.
PAUSE_AMOUNT = 0.1  # (!) Try changing this to 1.0.
# (!) Try changing this list to fewer colors:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

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
    bext.clear()

    # Generate some dots.
    dots = []
    for i in range(NUMBER_OF_DOTS):
        dots.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 2),
                      Y: random.randint(1, HEIGHT - 2),
                      DIR: random.choice(DIRECTIONS)})

    while True:  # Main program loop.
        for dot in dots:  # Handle each dot in the dots list.
            # Erase the dot's current location:
            bext.goto(dot[X], dot[Y])
            print(' ', end='')

            # Move the dot:
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

            # Draw the dots at their new location:
            bext.goto(dot[X], dot[Y])
            bext.fg(dot[COLOR])
            print(DOT_CHAR, end='')

            # See if the dot bounces off the corners:
            if dot[X] == 0 and dot[Y] == 0:
                dot[DIR] = DOWN_RIGHT
            elif dot[X] == 0 and dot[Y] == HEIGHT - 1:
                dot[DIR] = UP_RIGHT
            elif dot[X] == WIDTH - 1 and dot[Y] == 0:
                dot[DIR] = DOWN_LEFT
            elif dot[X] == WIDTH - 1 and dot[Y] == HEIGHT - 1:
                dot[DIR] = UP_LEFT

            # See if the dot bounces off the left edge:
            elif dot[X] == 0 and dot[DIR] == UP_LEFT:
                dot[DIR] = UP_RIGHT
            elif dot[X] == 0 and dot[DIR] == DOWN_LEFT:
                dot[DIR] = DOWN_RIGHT

            # See if the dot bounces off the right edge:
            elif dot[X] == WIDTH - 1 and dot[DIR] == UP_RIGHT:
                dot[DIR] = UP_LEFT
            elif dot[X] == WIDTH - 1 and dot[DIR] == DOWN_RIGHT:
                dot[DIR] = DOWN_LEFT

            # See if the dot bounces off the top edge:
            elif dot[Y] == 0 and dot[DIR] == UP_LEFT:
                dot[DIR] = DOWN_LEFT
            elif dot[Y] == 0 and dot[DIR] == UP_RIGHT:
                dot[DIR] = DOWN_RIGHT

            # See if the dot bounces off the bottom edge:
            elif dot[Y] == HEIGHT - 1 and dot[DIR] == DOWN_LEFT:
                dot[DIR] = UP_LEFT
            elif dot[Y] == HEIGHT - 1 and dot[DIR] == DOWN_RIGHT:
                dot[DIR] = UP_RIGHT

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(PAUSE_AMOUNT)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing Dots, by Al Sweigart al@inventwithpython.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.
