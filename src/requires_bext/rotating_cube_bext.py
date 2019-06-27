# Rotating Cube (Bext Version), by Al Sweigart al@inventwithpython.com

"""
This program requires the bext module, which you can install by opening
a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python3 -m pip install --user bext
"""

import math, time, sys
try:
    import bext
except:
    sys.exit('Bext is required to run this. Run `pip install bext` from the shell to install it.')

BLOCK = chr(9608) # Character 9608 is '█'

if len(sys.argv) == 3:
    # Set size based on command line arguments:
    WIDTH = int(sys.argv[1])
    HEIGHT = int(sys.argv[2])
else:
    WIDTH, HEIGHT = 80, 25
DEFAULT_SCALEX = (WIDTH - 4) // 8
DEFAULT_SCALEY = (HEIGHT - 4) // 4 # Text cells are twice as tall as they are wide, so set scaley accordingly.
DEFAULT_TRANSLATEX = (WIDTH - 4) // 2
DEFAULT_TRANSLATEY = (HEIGHT - 4) // 2


def line(x1, y1, x2, y2):
    """Returns a list of  all of the points in a line
    between `x1`, `y1` and `x2`, `y2`. Uses the Bresenham line algorithm.
    More info at https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # TODO - Do we want this line?

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
                yield (y, x)
            else:
                yield (x, y)
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
                yield (y, x)
            else:
                yield (x, y)
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax


def rotateXYZ(x, y, z, ax, ay, az):
    # NOTE: Rotates around the origin (0, 0, 0)

    # Rotate along x axis:
    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Rotate along y axis:
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Rotate along z axis:
    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)


def transformPoint(point1, point2, scalex=None, scaley=None, translatex=None, translatey=None):
    if scalex is None:
        scalex = DEFAULT_SCALEX
    if scaley is None:
        scaley = DEFAULT_SCALEY
    if translatex is None:
        translatex = DEFAULT_TRANSLATEX
    if translatey is None:
        translatey = DEFAULT_TRANSLATEY


    return (int(point1[0] * scalex + translatex),
            int(point1[1] * scaley + translatey),
            int(point2[0] * scalex + translatex),
            int(point2[1] * scaley + translatey))


bext.fg('random')

# Set up the points of the cube:
'''
Cube points:
   0+-----+1
   /     /|
  /     / |  -y
2+-----+3 |   |
 | 4+  |  +5  +-- +x
 |     | /   /
 |     |/   +z
6+-----+7
'''
points = [[-1, -1, -1],
          [ 1, -1, -1],
          [-1, -1,  1],
          [ 1, -1,  1],
          [-1,  1, -1],
          [ 1,  1, -1],
          [-1,  1,  1],
          [ 1,  1,  1]]
rotatedPoints = [None] * 10
rx = ry = rz = 0
step = 0

bext.clear()
try:
    while True:
        # Change color every 15 steps:
        if step % 15 == 0:
            bext.fg('random')
        step += 1

        # Rotate cube:
        rx += 0.03
        ry += 0.08
        rz += 0.13
        for i in range(len(points)):
            rotatedPoints[i] = rotateXYZ(*points[i], rx, ry, rz)

        # Get points of the cube lines:
        screenPoints = []
        screenPoints.extend(line(*transformPoint(rotatedPoints[0], rotatedPoints[1])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[1], rotatedPoints[3])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[3], rotatedPoints[2])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[2], rotatedPoints[0])))

        screenPoints.extend(line(*transformPoint(rotatedPoints[0], rotatedPoints[4])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[1], rotatedPoints[5])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[2], rotatedPoints[6])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[3], rotatedPoints[7])))

        screenPoints.extend(line(*transformPoint(rotatedPoints[4], rotatedPoints[5])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[5], rotatedPoints[7])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[7], rotatedPoints[6])))
        screenPoints.extend(line(*transformPoint(rotatedPoints[6], rotatedPoints[4])))

        screenPoints = tuple(frozenset(screenPoints)) # Get rid of duplicate points.

        # Draw cube:
        for x, y in screenPoints:
            # (Writing to the terminal will by far be the slowest part of this program.)
            bext.goto(x, y)
            print(BLOCK, end='')

        time.sleep(0.2) # Pause for a bit.

        # Erase cube:
        for x, y in screenPoints:
            bext.goto(x, y)
            print(' ', end='')

        # Print quit message:
        bext.goto(0, HEIGHT - 1)
        print('Press Ctrl-C to quit.', end='')
except KeyboardInterrupt:
    pass
