"""Fireflies, by Al Sweigart al@inventwithpython.com

A beautiful animation of fireflies. Press Ctrl-C to stop.
Tags: large, artistic"""
__version__ = 1

# This program MUST be run in a Terminal/Command Prompt window.

# This program draws points that rotate on the surface of a sphere. The
# sphere is invisible and projected onto the user's 2D screen, so the points
# kind of look like fireflies swirling around in a circle.

import math, time, sys, os, random

# Set up the constants:
PAUSE_AMOUNT = 0.15
NUMBER_OF_FIREFLIES = 16
WIDTH, HEIGHT = 80, 24  # Width & height of the swarm, in text cells.
SCALEX = (WIDTH - 4) // 4
SCALEY = (HEIGHT - 4) // 4

# Text cells are twice as tall as they are wide, so adjust SCALEY:
SCALEY = SCALEY * 2

TRANSLATEX = (WIDTH - 4) // 2 # Put the swarm in the screen's center.
TRANSLATEY = (HEIGHT - 4) // 2
FIREFLY_DARK = '.'  # Draw a period for normal fireflies.
FIREFLY_LIGHT = chr(9604)  # Draw a block for lit up fireflies.

# Several of the data structures are lists/tuples with x, y, z at
# indexes 0, 1, and 2 respectively. We'll use constants for them:
X = 0
Y = 1
Z = 2


def main():
    """Run the firefly animation."""

    # Each firefly is represented by dictionary with keys
    # 'originalPosition', 'rotationAmount', 'rotationVelocity',
    # 'changeTime', 'isLit'.
    fireflies = []
    for i in range(NUMBER_OF_FIREFLIES):
        firefly = {}

        # Create the original XYZ positions of the firefly. (Really,
        # they're just random points on a sphere that rotate around.)

        # Create points on a sphere from random latitude and longitude:
        latitude = math.acos(2 * random.random() - 1) - (math.pi / 2)
        longitude = 2 * math.pi * random.random()

        # Convert the latitude and longitude to an xyz point:
        x = math.cos(latitude) * math.cos(longitude)
        y = math.cos(latitude) * math.sin(longitude)
        z = math.sin(latitude)

        firefly['originalPosition'] = (x, y, z)

        # Firefly positions start with no rotation:
        firefly['rotationAmounts'] = [0, 0, 0]

        # Randomly choose rotation velocity for each axis:
        firefly['rotationVelocity'] = [
            random.randint(-100, 100) / 1000.0,
            random.randint(-100, 100) / 1000.0,
            random.randint(-100, 100) / 1000.0,
        ]

        # Holds time until the firefly changes between light/dark:
        firefly['changeTime'] = random.randint(10, 40) / 10.0

        # Fireflies start off dark:
        firefly['isLit'] = False

        fireflies.append(firefly)

    lastTimeCheck = time.time()

    while True:
        screenPoints = []
        screenChars = {}
        timeSinceLastCheck = time.time() - lastTimeCheck

        # Update the fireflies:
        for firefly in fireflies:
            # Change the rotation amount by the rotation velocity:
            firefly['rotationAmounts'][X] += firefly['rotationVelocity'][X]
            firefly['rotationAmounts'][Y] += firefly['rotationVelocity'][Y]
            firefly['rotationAmounts'][Z] += firefly['rotationVelocity'][Z]

            # To avoid rounding errors from accumulating, we recalculate
            # the rotation amounts based on the original position each
            # time. So when a coordinate rotates, say, 5 degrees and 6
            # more degrees, we actually calculate "5 degrees from the
            # original coordinate" and then "11 degrees from the original
            # coordinate", we don't rotate the rotated-by-5-degrees
            # coordinate another 6 degrees.
            rotatedPoint = rotatePoint(
                firefly['originalPosition'][X],
                firefly['originalPosition'][Y],
                firefly['originalPosition'][Z],
                firefly['rotationAmounts'][X],
                firefly['rotationAmounts'][Y],
                firefly['rotationAmounts'][Z],
            )
            rotatedAndTransformedPoint = transformPoint(rotatedPoint)
            screenPoints.append(rotatedAndTransformedPoint)

            # Determine if the firelies are light or dark:
            firefly['changeTime'] -= timeSinceLastCheck
            if firefly['changeTime'] < 0:
                if firefly['isLit']:
                    # Change firefly to dark for a random period:
                    firefly['changeTime'] = random.randint(10, 40) / 10.0
                else:
                    # Change firefly to light for 1 second:
                    firefly['changeTime'] = 1.0
                # Make isLit the opposite:
                firefly['isLit'] = not firefly['isLit']

            # Determine which character to draw on the screen:
            if firefly['isLit']:
                screenChars[rotatedAndTransformedPoint] = FIREFLY_LIGHT
            else:
                screenChars[rotatedAndTransformedPoint] = FIREFLY_DARK

        lastTimeCheck = time.time()

        # Draw the fireflies:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in screenPoints:
                    print(screenChars[(x, y)], end='')
                else:
                    print(' ', end='')  # Draw an empty space.
            print()
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)  # Pause before erasing the screen.

        # Clear the screen:
        if sys.platform == 'win32':
            os.system('cls')  # Clears Windows terminal.
        else:
            os.system('clear')  # Clears macOS/Linux terminal.


def rotatePoint(x, y, z, ax, ay, az):
    """Returns an (x, y, z) point a rotated point.

    This returned point is from the x, y, z point arguments rotated
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
    """Converts the 3D xyz point to a 2D xy point.

    Resizes this 2D point by a scale of scalex and scaley, then moves
    the point by translatex and translatey."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
