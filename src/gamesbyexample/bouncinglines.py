"""Bouncing Lines, by Al Sweigart al@inventwithpython.com
A bouncing line animation. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, bext, terminal"""
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

NUMBER_OF_POINTS = 4  # (!) Try changing this to 3 or 5.
PAUSE_AMOUNT = 0.1  # (!) Try changing this to 1.0.

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
LINE_CHAR = '#'  # (!) Try changing this to 'O' or '.' or '*' or '_'

# Key names for point dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # Generate some points.
    points = []
    for i in range(NUMBER_OF_POINTS):
        points.append({X: random.randint(1, WIDTH - 2),
                       Y: random.randint(1, HEIGHT - 2),
                       DIR: random.choice(DIRECTIONS)})

    while True:  # Main program loop.
        # There's a 1 in 50 chance of changing the color.
        if random.randint(1, 50) == 1:
            bext.fg('random')

        # Erase the lines drawn previously at these points.
        drawLinesBetweenPoints(points, ' ')

        for point in points:
            # Move the points in the direction of point[DIR]:
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

            # See if the point bounces off the corners:
            if point[X] == 0 and point[Y] == 0:
                point[DIR] = DOWN_RIGHT
            elif point[X] == 0 and point[Y] == HEIGHT - 1:
                point[DIR] = UP_RIGHT
            elif point[X] == WIDTH - 1 and point[Y] == 0:
                point[DIR] = DOWN_LEFT
            elif point[X] == WIDTH - 1 and point[Y] == HEIGHT - 1:
                point[DIR] = UP_LEFT

            # See if the dot bounces off the left edge:
            elif point[X] == 0 and point[DIR] == UP_LEFT:
                point[DIR] = UP_RIGHT
            elif point[X] == 0 and point[DIR] == DOWN_LEFT:
                point[DIR] = DOWN_RIGHT

            # See if the dot bounces off the right edge:
            elif point[X] == WIDTH - 1 and point[DIR] == UP_RIGHT:
                point[DIR] = UP_LEFT
            elif point[X] == WIDTH - 1 and point[DIR] == DOWN_RIGHT:
                point[DIR] = DOWN_LEFT

            # See if the dot bounces off the top edge:
            elif point[Y] == 0 and point[DIR] == UP_LEFT:
                point[DIR] = DOWN_LEFT
            elif point[Y] == 0 and point[DIR] == UP_RIGHT:
                point[DIR] = DOWN_RIGHT

            # See if the dot bounces off the bottom edge:
            elif point[Y] == HEIGHT - 1 and point[DIR] == DOWN_LEFT:
                point[DIR] = UP_LEFT
            elif point[Y] == HEIGHT - 1 and point[DIR] == DOWN_RIGHT:
                point[DIR] = UP_RIGHT

        # Draw the points in their new position:
        drawLinesBetweenPoints(points, LINE_CHAR)

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(PAUSE_AMOUNT)


def drawLinesBetweenPoints(points, character):
    for i, point in enumerate(points):
        pointA = point
        if i == len(points) - 1:
            # The last point draws a line to the first point:
            pointB = points[0]
        else:
            # Draw the line to the next point:
            pointB = points[i + 1]

        # Loop over every x, y point from pointA to pointB:
        for x, y in line(pointA[X], pointA[Y], pointB[X], pointB[Y]):
            bext.goto(x, y)
            print(character, end='')


def line(x1, y1, x2, y2):
    """Returns a list of points in a line between the given points.

    Uses the Bresenham line algorithm. More info at:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""

    # Check for the special case where the start and end points are
    # certain neighbors, which this function doesn't handle correctly,
    # and return a hard coded list instead:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    points = []  # Contains the points of the line.
    # "Steep" means the slope of the line is greater than 45 degrees or
    # less than -45 degrees:
    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        # This algorithm only handles non-steep lines, so let's change
        # the slope to non-steep and change it back later.
        x1, y1 = y1, x1  # Swap x1 and y1
        x2, y2 = y2, x2  # Swap x2 and y2
    isReversed = x1 > x2  # True if the line goes right-to-left.

    if isReversed:  # Get the points on the line going right-to-left.
        x1, x2 = x2, x1  # Swap x1 and x2
        y1, y2 = y2, y1  # Swap y1 and y2

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Calculate the y for every x in this line:
        for currentx in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:  # Only change y once extray <= 0.
                currenty -= ydirection
                extray += deltax
    else:  # Get the points on the line going left-to-right.
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Calculate the y for every x in this line:
        for currentx in range(x1, x2 + 1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray < 0:  # Only change y once extray < 0.
                currenty += ydirection
                extray += deltax
    return points


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing Lines, by Al Sweigart al@inventwithpython.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.
