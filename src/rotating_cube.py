# Rotating Cube, by Al Sweigart al@inventwithpython.com

import math, time, random, sys, os

if len(sys.argv) == 3:
    # Set size based on command line arguments:
    WIDTH = int(sys.argv[1])
    HEIGHT = int(sys.argv[2])
else:
    WIDTH, HEIGHT = 80, 50
DEFAULT_SCALEX = (WIDTH - 4) // 8
DEFAULT_SCALEY = (HEIGHT - 4) // 4 # Text cells are twice as tall as they are wide, so set scaley accordingly.
DEFAULT_TRANSLATEX = (WIDTH - 4) // 2
DEFAULT_TRANSLATEY = (HEIGHT - 4) // 2


def line(x1, y1, x2, y2):
    """Returns a generator that produces all of the points in a line
    between `x1`, `y1` and `x2`, `y2`. Uses the Bresenham line algorithm."""

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
rotatedPoints = [None] * len(points)
rx = ry = rz = 0 # Rotation amounts for each axis.

try:
    while True:
        # Rotate the cube:
        rx += 0.03 + random.randint(1, 20) / 100
        ry += 0.08 + random.randint(1, 20) / 100
        rz += 0.13 + random.randint(1, 20) / 100
        for i in range(len(points)):
            rotatedPoints[i] = rotateXYZ(*points[i], rx, ry, rz)

        # Get the points of the cube lines:
        cubePoints = []
        cubePoints.extend(line(*transformPoint(rotatedPoints[0], rotatedPoints[1])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[1], rotatedPoints[3])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[3], rotatedPoints[2])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[2], rotatedPoints[0])))

        cubePoints.extend(line(*transformPoint(rotatedPoints[0], rotatedPoints[4])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[1], rotatedPoints[5])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[2], rotatedPoints[6])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[3], rotatedPoints[7])))

        cubePoints.extend(line(*transformPoint(rotatedPoints[4], rotatedPoints[5])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[5], rotatedPoints[7])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[7], rotatedPoints[6])))
        cubePoints.extend(line(*transformPoint(rotatedPoints[6], rotatedPoints[4])))

        cubePoints = tuple(frozenset(cubePoints)) # Get rid of duplicate points.

        # Draw the cube:
        for y in range(0, HEIGHT, 2):
            for x in range(WIDTH):
                if (x, y) in cubePoints and (x, y + 1) in cubePoints:
                    print(chr(9608), end='', flush=False) # Draw full block.
                elif (x, y) in cubePoints and (x, y + 1) not in cubePoints:
                    print(chr(9600), end='', flush=False) # Draw top half of block.
                elif not (x, y) in cubePoints and (x, y + 1) in cubePoints:
                    print(chr(9604), end='', flush=False) # Draw bottom half of block.
                else:
                    print(' ', end='', flush=False) # Draw empty space.
            print()
        print('', end='', flush=True)

        time.sleep(0.1) # Pause for a bit.

        # Erase the screen:
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

except KeyboardInterrupt:
    pass # When Ctrl-C is pressed, stop looping.
