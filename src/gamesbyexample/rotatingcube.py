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

# Several of the data structures are lists/tuples with x, y, z at indexes 0, 1, and 2 respectively:
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
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    isReversed = x1 > x2  # True if the line goes right-to-left.

    if isReversed:  # Get the points on the line going right-to-left.
        x1, x2 = x2, x1
        y1, y2 = y2, y1

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


def transformPoint(point):
    """Converts the 3D xyz point to a 2D xy point. Resizes this 2D point
    by a scale of scalex and scaley, then moves the point by translatex
    and translatey."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


origPoints = [[-1, -1, -1],
              [ 1, -1, -1],
              [-1, -1,  1],
              [ 1, -1,  1],
              [-1,  1, -1],
              [ 1,  1, -1],
              [-1,  1,  1],
              [ 1,  1,  1]]
rotatedPoints = [None] * len(origPoints)
rx = ry = rz = 0.0  # Rotation amounts for each axis.

try:
    while True:  # Main program loop.
        # Rotate the cube:
        rx += 0.03
        ry += 0.08
        rz += 0.13
        for i in range(len(origPoints)):
            rotatedPoints[i] = rotatePoint(*origPoints[i], rx, ry, rz)

        # Get the points of the cube lines:
        cubePoints = []
        for start, end in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
            transformedPoint1 = transformPoint(rotatedPoints[start])
            transformedPoint2 = transformPoint(rotatedPoints[end])
            cubePoints.extend(line(transformedPoint1[X], transformedPoint1[Y], transformedPoint2[X], transformedPoint2[Y]))
        # Get rid of duplicate points:
        cubePoints = tuple(frozenset(cubePoints))
        # Draw the cube:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    # Draw full block:
                    print(chr(9608), end='', flush=False)
                else:
                    # Draw empty space:
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
