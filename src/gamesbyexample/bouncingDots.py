"""Bouncing Ball, by Al Sweigart al@inventwithpython.com

A bouncing ball animation. Press Ctrl-C to stop."""
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
NUMBER_OF_BALLS = 35
COLORS = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
BALL_CHAR = 'O'

# Key names for ball dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    """Run the bouncing dots program."""
    bext.clear()

    # Generate some balls.
    balls = []
    for i in range(NUMBER_OF_BALLS):
        balls.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 2),
                      Y: random.randint(1, HEIGHT - 2),
                      DIR: random.choice(DIRECTIONS)})

    while True:  # Main program loop.
        oldBallPositions = []

        for ball in balls:
            # Draw our balls:
            bext.goto(ball[X], ball[Y])
            bext.fg(ball[COLOR])
            print(BALL_CHAR, end='')

            oldBallPositions.append((ball[X], ball[Y]))
        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(0.1)

        for ball in balls:
            # Move our balls:
            if ball[DIR] == UP_RIGHT:
                ball[X] += 1
                ball[Y] -= 1
            elif ball[DIR] == UP_LEFT:
                ball[X] -= 1
                ball[Y] -= 1
            elif ball[DIR] == DOWN_RIGHT:
                ball[X] += 1
                ball[Y] += 1
            elif ball[DIR] == DOWN_LEFT:
                ball[X] -= 1
                ball[Y] += 1

            # See if our balls bounce off the corners:
            if ball[X] == 0 and ball[Y] == 0:
                ball[DIR] = DOWN_RIGHT
            elif ball[X] == 0 and ball[Y] == HEIGHT - 1:
                ball[DIR] = UP_RIGHT
            elif ball[X] == WIDTH - 1 and ball[Y] == 0:
                ball[DIR] = DOWN_LEFT
            elif ball[X] == WIDTH - 1 and ball[Y] == HEIGHT - 1:
                ball[DIR] = UP_LEFT

            # See if our balls bounce off the walls:
            elif ball[X] == 0 and ball[DIR] == UP_LEFT:
                ball[DIR] = UP_RIGHT
            elif ball[X] == 0 and ball[DIR] == DOWN_LEFT:
                ball[DIR] = DOWN_RIGHT

            elif ball[X] == WIDTH - 1 and ball[DIR] == UP_RIGHT:
                ball[DIR] = UP_LEFT
            elif ball[X] == WIDTH - 1 and ball[DIR] == DOWN_RIGHT:
                ball[DIR] = DOWN_LEFT

            elif ball[Y] == 0 and ball[DIR] == UP_LEFT:
                ball[DIR] = DOWN_LEFT
            elif ball[Y] == 0 and ball[DIR] == UP_RIGHT:
                ball[DIR] = DOWN_RIGHT

            elif ball[Y] == HEIGHT - 1 and ball[DIR] == DOWN_LEFT:
                ball[DIR] = UP_LEFT
            elif ball[Y] == HEIGHT - 1 and ball[DIR] == DOWN_RIGHT:
                ball[DIR] = UP_RIGHT

        for position in oldBallPositions:
            # Erase all of the balls.
            bext.goto(position[0], position[1])
            print(' ', end='')
        # At this point, go back to the start of the main program loop.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
