"""Fireflies, by Al Sweigart al@inventwithpython.com
A beautiful animation of fireflies. Press Ctrl-C to stop.
This program MUST be run in a Terminal/Command Prompt window.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, terminal"""
__version__ = 0
import math, time, sys, os, random

# This program draws 3D points that rotate around a center point. This
# gives the fireflies a "swirling" kind of movement.

# Set up the constants:
PAUSE_AMOUNT = 0.15  # (!) Try changing this to 0.05 or 0.5.
NUMBER_OF_FIREFLIES = 16  # (!) Try changing this to 2 or 100.
LIT_DURATION = 3  # (!) Try changing this to 100.
MIN_LIT_FREQ = 10
MAX_LIT_FREQ = 40

WIDTH, HEIGHT = 80, 24  # Width & height of the swarm, in text cells.
SCALEX = (WIDTH - 4) // 4
SCALEY = (HEIGHT - 4) // 4

# Text cells are twice as tall as they are wide, so adjust SCALEY:
SCALEY = SCALEY * 2

TRANSLATEX = (WIDTH - 4) // 2  # Put the swarm in the screen's center.
TRANSLATEY = (HEIGHT - 4) // 2
FIREFLY_DARK = '.'  # Draw a period for normal fireflies.
FIREFLY_LIGHT = chr(9604)  # Draw a block for lit up fireflies.

# Several of the data structures are lists/tuples with x, y, z at
# indexes 0, 1, and 2 respectively. We'll use constants for them:
X, Y, Z = 0, 1, 2


def main():
    # First we create data structures for our fireflies.
    # Each firefly is represented by dictionary with keys
    # 'originalPosition', 'rotationAmount', 'rotVelocity',
    # 'timeToLit', 'isLit'.
    fireflies = []
    for i in range(NUMBER_OF_FIREFLIES):
        firefly = {}  # The dictionary for a new, single firefly.

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
        firefly['rotAmounts'] = [0, 0, 0]  # x, y, and z rotation.

        # Randomly choose rotation velocity for each axis:
        firefly['rotVelocity'] = [
            random.randint(-100, 100) / 1000.0,
            random.randint(-100, 100) / 1000.0,
            random.randint(-100, 100) / 1000.0,
        ]

        # Holds time until the firefly changes between light/dark:
        firefly['timeToLit'] = random.randint(MIN_LIT_FREQ, MAX_LIT_FREQ)

        # Fireflies start off dark:
        firefly['isLit'] = False

        # Append this dictionary to the list of firefly dictionaries:
        fireflies.append(firefly)

    # Next, we animate and display the fireflies on the screen:
    while True:  # Main program loop.
        # lightPoints is a list of (x, y) tuples for where lit up
        # fireflies should be displayed on the screen. darkPoints is
        # for dark fireflies.
        lightPoints = []
        darkPoints = []

        # Move the fireflies and figure out where to display them:
        for firefly in fireflies:
            # Change the rotation amount by the rotation velocity:
            firefly['rotAmounts'][X] += firefly['rotVelocity'][X]
            firefly['rotAmounts'][Y] += firefly['rotVelocity'][Y]
            firefly['rotAmounts'][Z] += firefly['rotVelocity'][Z]

            # To avoid rounding errors from accumulating, we recalculate
            # the rotated position by rotating from the original position
            # instead of the firefly's last position.
            # For example, if the firefly rotates 5 degrees, and then 6
            # more degrees, we calculate it's rotation 5 degrees from
            # it's original position, and then 11 degrees from it's
            # original position.
            rotatedPoint = rotatePoint(
                firefly['originalPosition'][X],
                firefly['originalPosition'][Y],
                firefly['originalPosition'][Z],
                firefly['rotAmounts'][X],
                firefly['rotAmounts'][Y],
                firefly['rotAmounts'][Z],
            )
            rotatedAndTransformedPoint = transformPoint(rotatedPoint)

            # Determine if the firelies are light or dark:
            firefly['timeToLit'] -= 1  # Decrease this on each iteration.
            if firefly['timeToLit'] <= 0:
                if firefly['isLit']:
                    # Firefly will be dark for a random amount of time:
                    firefly['timeToLit'] = random.randint(MIN_LIT_FREQ,
                        MAX_LIT_FREQ)
                else:
                    # Firefly will be light for a set amount of time:
                    firefly['timeToLit'] = LIT_DURATION
                # Toggle isLit to the opposite value:
                firefly['isLit'] = not firefly['isLit']

            # Determine which character to draw on the screen:
            if firefly['isLit']:
                lightPoints.append(rotatedAndTransformedPoint)
            else:
                darkPoints.append(rotatedAndTransformedPoint)

        # Display the animate firefly scene:
        displayFireflies(lightPoints, darkPoints)
        time.sleep(PAUSE_AMOUNT)  # Pause before erasing the screen.
        clearScreen()


def rotatePoint(x, y, z, ax, ay, az):
    """Returns a 3D point that is rotated from the x, y, z point
    arguments. This new point is rotated around the (0, 0, 0) origin
    by angles ax, ay, az (in radians).
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
    """Resizes this 2D point by a scale of scalex and scaley, then moves
    the point by translatex and translatey."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


def displayFireflies(lightPoints, darkPoints):
    # Loop over every place on the screen and draw fireflies:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in lightPoints:
                print(FIREFLY_LIGHT, end='')  # Display lit firefly.
            elif (x, y) in darkPoints:
                print(FIREFLY_DARK, end='')  # Display dark firefly.
            else:
                print(' ', end='')  # Display an empty space.
        print()  # Print a newline.
    print('Press Ctrl-C to quit.', end='', flush=True)


def clearScreen():
    """Clear the terminal window screen by running cls or clear."""
    if sys.platform == 'win32':
        os.system('cls')  # Windows uses the cls command.
    else:
        os.system('clear')  # macOS and Linux use the clear command.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
