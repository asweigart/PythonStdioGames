"""Bouncing Lines, by Al Sweigart al@inventwithpython.com

A bouncing line animation. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
Tags: large, artistic, bext"""
__version__ = 0

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

# Set up the constants:
WIDTH, HEIGHT = bext.size()
WIDTH -= 1  # Adjustment for Windows Command Prompt.
NUMBER_OF_POINTS = 4
COLORS = ('red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white')
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
LINE_CHAR = '#'

# Key names for point dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    """Run the bouncing lines program."""
    bext.clear()

    # Generate some points.
    points = []
    for i in range(NUMBER_OF_POINTS):
        points.append({X: random.randint(1, WIDTH - 2),
                       Y: random.randint(1, HEIGHT - 2),
                       DIR: random.choice(DIRECTIONS)})

    while True:  # Main program loop.
        oldpointPositions = []

        if random.randint(1, 50) == 1:
            bext.fg('random')

        for i, point in enumerate(points):
            # Draw our lines:
            if i == len(points) - 1:
                # The last point connects to the first point.
                pointA = point
                pointB = points[0]
            else:
                pointA = point
                pointB = points[i + 1]

            for x, y in line(pointA[X], pointA[Y], pointB[X], pointB[Y]):
                bext.goto(x, y)
                print(LINE_CHAR, end='')

                oldpointPositions.append((x, y))
        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(0.1)

        for point in points:
            # Move our points:
            if point[DIR] == UP_RIGHT:
                point[X] += 1
                point[Y] -= 1
            elif point[DIR] == UP_LEFT:
                point[X] -= 1
                point[Y] -= 1
            elif point[DIR] == DOWN_RIGHT:
                point[X] += 1
                point[Y] += 1
            elif point[DIR] == DOWN_LEFT:
                point[X] -= 1
                point[Y] += 1

            # See if our points bounce off the corners:
            if point[X] == 0 and point[Y] == 0:
                point[DIR] = DOWN_RIGHT
            elif point[X] == 0 and point[Y] == HEIGHT - 1:
                point[DIR] = UP_RIGHT
            elif point[X] == WIDTH - 1 and point[Y] == 0:
                point[DIR] = DOWN_LEFT
            elif point[X] == WIDTH - 1 and point[Y] == HEIGHT - 1:
                point[DIR] = UP_LEFT

            # See if our points bounce off the walls:
            elif point[X] == 0 and point[DIR] == UP_LEFT:
                point[DIR] = UP_RIGHT
            elif point[X] == 0 and point[DIR] == DOWN_LEFT:
                point[DIR] = DOWN_RIGHT

            elif point[X] == WIDTH - 1 and point[DIR] == UP_RIGHT:
                point[DIR] = UP_LEFT
            elif point[X] == WIDTH - 1 and point[DIR] == DOWN_RIGHT:
                point[DIR] = DOWN_LEFT

            elif point[Y] == 0 and point[DIR] == UP_LEFT:
                point[DIR] = DOWN_LEFT
            elif point[Y] == 0 and point[DIR] == UP_RIGHT:
                point[DIR] = DOWN_RIGHT

            elif point[Y] == HEIGHT - 1 and point[DIR] == DOWN_LEFT:
                point[DIR] = UP_LEFT
            elif point[Y] == HEIGHT - 1 and point[DIR] == DOWN_RIGHT:
                point[DIR] = UP_RIGHT

        for position in oldpointPositions:
            # Erase all of the points.
            bext.goto(position[0], position[1])
            print(' ', end='')
        # At this point, go back to the start of the main program loop.


def line(x1, y1, x2, y2):
    """Returns a list of points in a line between the given points.

    Uses the Bresenham line algorithm. More info at:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    points = []
    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    isReversed = x1 > x2

    if isReversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y2
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error <= 0:
                y -= ystep
                error += deltax
    else:
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if isSteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
    return points


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
