# Fireflies, by Al Sweigart al@inventwithpython.com

import math, time, sys, os, random

NUMBER_OF_POINTS = 16

if len(sys.argv) == 3:
    # Set size based on command line arguments:
    WIDTH = int(sys.argv[1])
    HEIGHT = int(sys.argv[2])
else:
    WIDTH, HEIGHT = 80, 50
DEFAULT_SCALEX = (WIDTH - 4) // 4
DEFAULT_SCALEY = (HEIGHT - 4) // 2 # Text cells are twice as tall as they are wide, so set scaley accordingly.
DEFAULT_TRANSLATEX = (WIDTH - 4) // 2
DEFAULT_TRANSLATEY = (HEIGHT - 4) // 2


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


def transformPoint(point, scalex=None, scaley=None, translatex=None, translatey=None):
    if scalex is None:
        scalex = DEFAULT_SCALEX
    if scaley is None:
        scaley = DEFAULT_SCALEY
    if translatex is None:
        translatex = DEFAULT_TRANSLATEX
    if translatey is None:
        translatey = DEFAULT_TRANSLATEY

    return (int(point[0] * scalex + translatex),
            int(point[1] * scaley + translatey))



# Set up the points of the cube:
'''
 -y
  |
  +-- +x
 /
+z
'''

points = []
for i in range(NUMBER_OF_POINTS):
    lat = math.acos(2 * random.random() - 1) - (math.pi / 2)
    lon = 2 * math.pi * random.random()

    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)
    points.append((x, y, z))

rotatedPoints = [None] * len(points)
rotationAmounts = []
for i in range(len(points)):
    rotationAmounts.append([0, 0, 0])
rotationVelocity = []
for i in range(len(points)):
    rotationVelocity.append([random.randint(-100, 100) / 1000.0,
                             random.randint(-100, 100) / 1000.0,
                             random.randint(-100, 100) / 1000.0])

try:
    while True:
        # Rotate the points:
        for i in range(len(points)):
            rotationAmounts[i][0] += rotationVelocity[i][0]
            rotationAmounts[i][1] += rotationVelocity[i][1]
            rotationAmounts[i][2] += rotationVelocity[i][2]

            rotatedPoints[i] = rotateXYZ(*points[i], rotationAmounts[i][0], rotationAmounts[i][1], rotationAmounts[i][2])

        # Get the points of the cube lines:
        spherePoints = []
        for point in rotatedPoints:
            spherePoints.append(transformPoint(point))
        spherePoints = tuple(frozenset(spherePoints)) # Get rid of duplicate points.

        # Draw the cube:
        for y in range(0, HEIGHT, 2):
            for x in range(WIDTH):
                if (x, y) in spherePoints and (x, y + 1) in spherePoints:
                    print(chr(9608), end='', flush=False) # Draw full block.
                elif (x, y) in spherePoints and (x, y + 1) not in spherePoints:
                    print(chr(9600), end='', flush=False) # Draw top half of block.
                elif not (x, y) in spherePoints and (x, y + 1) in spherePoints:
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
