# Fireflies, by Al Sweigart al@inventwithpython.com

"""This program draws points that rotate on a sphere. The sphere is invisible
and projected onto the user's 2D screen, so it kind of looks like fireflies
swirling around in a circle."""

import math, time, sys, os, random

PAUSE_AMOUNT = 0.05
NUMBER_OF_FIREFLIES = 16
WIDTH, HEIGHT = 80, 50
SCALEX = (WIDTH - 4) // 4
SCALEY = (HEIGHT - 4) // 2 # Text cells are twice as tall as they are wide, so set scaley accordingly.
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2


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
    return (int(point[0] * SCALEX + TRANSLATEX),
            int(point[1] * SCALEY + TRANSLATEY))


# Create the original XYZ positions of the fireflies. (Really, they're
# just random points on a sphere that rotate around.)
originalPosition = []
for i in range(NUMBER_OF_FIREFLIES):
    # Create points on a sphere based on random latitude and longitude:
    latitude = math.acos(2 * random.random() - 1) - (math.pi / 2)
    longitude = 2 * math.pi * random.random()

    # Convert the latitude and longitude to an xyz point:
    x = math.cos(latitude) * math.cos(longitude)
    y = math.cos(latitude) * math.sin(longitude)
    z = math.sin(latitude)

    originalPosition.append((x, y, z))

# Holds how much the firefly has rotated around each axis:
rotationAmounts = []
# Holds the rate that the firefly rotates around each axis:
rotationVelocity = []
for i in range(NUMBER_OF_FIREFLIES):
    # Firefly positions start with no rotation from their original position:
    rotationAmounts.append([0, 0, 0])
    # Randomly decide how fast they rotate on each axis:
    rotationVelocity.append([random.randint(-100, 100) / 1000.0,
                             random.randint(-100, 100) / 1000.0,
                             random.randint(-100, 100) / 1000.0])

try:
    while True:
        # Rotate the fireflies:
        screenPoints = []
        for i in range(NUMBER_OF_FIREFLIES):
            # Change the rotation amount by
            rotationAmounts[i][0] += rotationVelocity[i][0]
            rotationAmounts[i][1] += rotationVelocity[i][1]
            rotationAmounts[i][2] += rotationVelocity[i][2]

            # To avoid rounding errors from accumulating, we recalculate
            # the rotation amounts based on the original position each time.
            # So when a coordinate rotates, say, 5 degrees and 6 more degrees,
            # we actually calculate "5 degrees from the original coordinate"
            # and then "11 degrees from the original coordinate", we don't
            # rotate the rotated-by-5-degrees coordinate another 6 degrees.
            screenPoints.append(transformPoint(rotatePoint(originalPosition[i][0], originalPosition[i][1], originalPosition[i][2], rotationAmounts[i][0], rotationAmounts[i][1], rotationAmounts[i][2])))

        # Draw the fireflies:
        for y in range(0, HEIGHT, 2):
            for x in range(WIDTH):
                if (x, y) in screenPoints and (x, y + 1) in screenPoints:
                    print(chr(9608), end='') # Draw a full block.
                elif (x, y) in screenPoints and (x, y + 1) not in screenPoints:
                    print(chr(9600), end='') # Draw a top half of block.
                elif not (x, y) in screenPoints and (x, y + 1) in screenPoints:
                    print(chr(9604), end='') # Draw a bottom half of block.
                else:
                    print(' ', end='') # Draw an empty space.
            print()
        print('Press Ctrl-C or Ctrl-D to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT) # Pause for a bit before erasing the screen.

        # Erase the screen:
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

except KeyboardInterrupt:
    pass # When Ctrl-C/Ctrl-D is pressed, stop looping.
