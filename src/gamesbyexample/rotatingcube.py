"""Rotating Cube, by Al Sweigart al@inventwithpython.com
A rotating cube animation. Press Ctrl-C to stop.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, math"""
__version__ = 0
# This program MUST be run in a Terminal/Command Prompt window.

import math, time, sys, os

# Set up the constants:
PAUSE_AMOUNT = 0.1  # Pause length of one-tenth of a second.
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
# Text cells are twice as tall as they are wide, so set scaley:
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

# (!) Try changing this to '#' or '*' or some other character:
LINE_CHAR = chr(9608)  # Character 9608 is '█'

# (!) Try setting two of these values to zero to rotate the cube only
# along a single axis:
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

# This program stores XYZ coordinates in lists, with the X coordinate
# at index 0, Y at 1, and Z at 2. These constants make our code more
# readable when accessing the coordinates in these lists.
X = 0
Y = 1
Z = 2


def line(x1, y1, x2, y2):
    """Returns a list of points in a line between the given points.

    Uses the Bresenham line algorithm. More info at:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    points = []  # Contains the points of the line.
    # "Steep" means the slope of the line is greater than 45 degrees or
    # less than -45 degrees:

    # Check for the special case where the start and end points are
    # certain neighbors, which this function doesn't handle correctly,
    # and return a hard coded list instead:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

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


def rotatePoint(x, y, z, ax, ay, az):
    """Returns an (x, y, z) tuple of the x, y, z arguments rotated.

    The rotation happens around the 0, 0, 0 origin by angles
    ax, ay, az (in radians).
        Directions of each axis:
         -y
          |
          +-- +x
         /
        +z
    """

    # Rotate around x axis:
    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Rotate around y axis:
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Rotate around z axis:
    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)


def adjustPoint(point):
    """Adjusts the 3D XYZ point to a 2D XY point fit for displaying on
    the screen. This resizes this 2D point by a scale of SCALEX and
    SCALEY, then moves the point by TRANSLATEX and TRANSLATEY."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


"""CUBE_CORNERS stores the XYZ coordinates of the corners of a cube.
The indexes for each corner in CUBE_CORNERS are marked in this diagram:
      0---1
     /|  /|
    2---3 |
    | 4-|-5
    |/  |/
    6---7"""
CUBE_CORNERS = [[-1, -1, -1], # Point 0
                [ 1, -1, -1], # Point 1
                [-1, -1,  1], # Point 2
                [ 1, -1,  1], # Point 3
                [-1,  1, -1], # Point 4
                [ 1,  1, -1], # Point 5
                [-1,  1,  1], # Point 6
                [ 1,  1,  1]] # Point 7
# rotatedCorners stores the XYZ coordinates from CUBE_CORNERS after
# they've been rotated by rx, ry, and rz amounts:
rotatedCorners = [None, None, None, None, None, None, None, None]
# Rotation amounts for each axis:
xRotation = 0.0
yRotation = 0.0
zRotation = 0.0

try:
    while True:  # Main program loop.
        # Rotate the cube along different axises by different amounts:
        xRotation += X_ROTATE_SPEED
        yRotation += Y_ROTATE_SPEED
        zRotation += Z_ROTATE_SPEED
        for i in range(len(CUBE_CORNERS)):
            x = CUBE_CORNERS[i][X]
            y = CUBE_CORNERS[i][Y]
            z = CUBE_CORNERS[i][Z]
            rotatedCorners[i] = rotatePoint(x, y, z, xRotation,
                yRotation, zRotation)

        # Get the points of the cube lines:
        cubePoints = []
        for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
            fromX, fromY = adjustPoint(rotatedCorners[fromCornerIndex])
            toX, toY = adjustPoint(rotatedCorners[toCornerIndex])
            pointsOnLine = line(fromX, fromY, toX, toY)
            cubePoints.extend(pointsOnLine)

        # Get rid of duplicate points:
        cubePoints = tuple(frozenset(cubePoints))

        # Display the cube on the screen:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    # Display full block:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    # Display empty space:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)  # Pause for a bit.

        # Erase the screen:
        if sys.platform == 'win32':
            # Clear the Windows terminal with the cls command:
            os.system('cls')
        else:
            # Clear macOS/Linux terminals with the clear command:
            os.system('clear')

except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
