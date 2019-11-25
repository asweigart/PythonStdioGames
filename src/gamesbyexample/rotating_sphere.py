# Rotating Sphere, by Al Sweigart al@inventwithpython.com
# A rotating sphere animation.

# This program MUST be run in a Terminal/Command Prompt window.

import math, time, sys, os

NUMBER_OF_POINTS = 40
NUM_LAT_POINTS = 6
NUM_LON_POINTS = 6

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
    if scalex == None:
        scalex = DEFAULT_SCALEX
    if scaley == None:
        scaley = DEFAULT_SCALEY
    if translatex == None:
        translatex = DEFAULT_TRANSLATEX
    if translatey == None:
        translatey = DEFAULT_TRANSLATEY

    return (int(point[0] * scalex + translatex),
            int(point[1] * scaley + translatey))


# Directions of each axis:
#  -y
#   |
#   +-- +x
#  /
# +z

# Set up the points of the sphere:
points = [(0, 0, 1.0), (0, 0, -1.0)]
for latitude in range(NUM_LAT_POINTS):
    for longitude in range(NUM_LON_POINTS):
        lat = math.acos(2 * (latitude / float(NUM_LAT_POINTS)) - 1) - (math.pi / 2)
        lon = 2 * math.pi * (longitude / float(NUM_LON_POINTS))

        x = math.cos(lat) * math.cos(lon)
        y = math.cos(lat) * math.sin(lon)
        z = math.sin(lat)
        points.append((x, y, z))


rotatedPoints = [None] * len(points)
rx = ry = rz = 0.0 # Rotation amounts for each axis.

try:
    while True:
        # Rotate the cube:
        rx += 0.01# + random.randint(1, 20) / 100
        ry += 0.05# + random.randint(1, 20) / 100
        #rz += 0.05# + random.randint(1, 20) / 100
        for i, point in enumerate(points):
            rotatedPoints[i] = rotateXYZ(*point, rx, ry, rz)

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

        time.sleep(0.05) # Pause for a bit.

        # Erase the screen:
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

except KeyboardInterrupt:
    pass # When Ctrl-C is pressed, stop looping.
