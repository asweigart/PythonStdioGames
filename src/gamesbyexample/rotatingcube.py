# Rotating Cube, by Al Sweigart al@inventwithpython.com
# A rotating cube animation. Press Ctrl-C to stop.
__version__ = 1

# This program MUST be run in a Terminal/Command Prompt window.

import math, time, sys, os

PAUSE_AMOUNT = 0.05
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 4 # Text cells are twice as tall as they are wide, so set scaley accordingly.
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

# Several of the data structures are lists/tuples with x, y, z at indexes 0, 1, and 2 respectively:
X = 0
Y = 1
Z = 2


def line(x1, y1, x2, y2):
    """Returns a list of  all of the points in a line
    between `x1`, `y1` and `x2`, `y2`. Uses the Bresenham line algorithm.
    More info at https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    points = []
    isSteep = abs(y2-y1) > abs(x2-x1)
    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    isReversed = x1 > x2

    if isReversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

        deltax = x2 - x1
        deltay = abs(y2-y1)
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
        deltay = abs(y2-y1)
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


def rotatePoint(x, y, z, ax, ay, az):
    """Returns an (x, y, z) point of the x, y, z point arguments rotated
    around the 0, 0, 0 origin by angles ax, ay, az (in radians).
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
    """Converts the 3D xyz point to a 2D xy point. Resizes this 2D point by a
    scale of scalex and scaley, then moves the point by translatex and
    translatey."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


originalPoints = [[-1, -1, -1],
                  [ 1, -1, -1],
                  [-1, -1,  1],
                  [ 1, -1,  1],
                  [-1,  1, -1],
                  [ 1,  1, -1],
                  [-1,  1,  1],
                  [ 1,  1,  1]]
rotatedPoints = [None] * len(originalPoints)
rx = ry = rz = 0.0 # Rotation amounts for each axis.

try:
    while True:
        # Rotate the cube:
        rx += 0.03
        ry += 0.08
        rz += 0.13
        for i in range(len(originalPoints)):
            rotatedPoints[i] = rotatePoint(*originalPoints[i], rx, ry, rz)

        # Get the points of the cube lines:
        cubePoints = []
        for start, end in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
            transformedPoint1 = transformPoint(rotatedPoints[start])
            transformedPoint2 = transformPoint(rotatedPoints[end])
            cubePoints.extend(line(transformedPoint1[X], transformedPoint1[Y], transformedPoint2[X], transformedPoint2[Y]))
        cubePoints = tuple(frozenset(cubePoints)) # Get rid of duplicate points.

        # Draw the cube:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    print(chr(9608), end='', flush=False) # Draw full block.
                else:
                    print(' ', end='', flush=False) # Draw empty space.
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT) # Pause for a bit.

        # Erase the screen:
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.
