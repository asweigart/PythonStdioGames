"""Roomba Simulator, by Al Sweigart al@inventwithpython.com
Watch a roomba move around and collect dirt.
Tags: large, artistic, simulation"""
__version__ = 0
# This program MUST be run in a Terminal/Command Prompt window.

import math, random, shutil, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Get the size of the terminal window:
WIDTH, HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1
HEIGHT -= 1  # Make room for the battery indicator text at the bottom.

ROOMBA = 'O'
BASE = 'U'
EMPTY = ' '
DIRT1 = chr(9617)  # Character 9617 is '░'
DIRT2 = chr(9618)  # Character 9618 is '▒'
DIRT3 = chr(9619)  # Character 9619 is '▓'
DIRT_CHARS = (EMPTY, DIRT1, DIRT2, DIRT3)
CHARGING  = 'CHARGING '  # Note the space at the end.
CLEANING  = 'CLEANING '  # Note the space at the end.
RETURNING = 'RETURNING'

# The dirt adding frequency ranges from 0 to 100:
DIRT_ADD_FREQUENCY = 5  # (!) Try changing this to 1, 20, or 100.
DIRT_ADD_AMOUNT = 4     # (!) Try changing this to 1 or 100.
NUM_STARTING_DIRT = 5   # (!) Try changing this to 200.
MAX_BATTERY = 250       # (!) Try changing this to 20, or 9999.
RECHARGE_RATE = 10      # (!) Try changing this to 0, 1, or 9999.
PAUSE = 0.1             # (!) Try changing this to 0.0 or 1.0.


def main():
    baseX = random.randint(0, WIDTH - 1)
    baseY = random.randint(0, HEIGHT - 1)
    roombaX = baseX
    roombaY = baseY
    roombaBattery = MAX_BATTERY

    dirtPiles = {}  # Keys are (x, y) tuples, value is dirt level.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            dirtPiles[(x, y)] = 0  # Set it to no dirt to begin with.

    # Add some dirt to start with:
    bext.clear()  # Clear the terminal window.
    for i in range(NUM_STARTING_DIRT):
        newDirtX = random.randint(0, WIDTH - 1)
        newDirtY = random.randint(0, HEIGHT - 1)
        dirtPiles[(newDirtX, newDirtY)] = 1
        bext.goto(newDirtX, newDirtY)
        print(DIRT_CHARS[dirtPiles[(newDirtX, newDirtY)]], end='')

    moveTo = []  # TODO list of (x, y)
    while True:  # Main simulation loop.
        # There's a bug where sometimes the roomba ends up with a
        # battery level under 0.0. We'll ignore this bug. Uncomment
        # this assert statement to show when it happens:
        #assert roombaBattery >= 0, 'Negative bat:' + str(roombaBattery)

        roombaStatus = CLEANING

        # Add dirt to the room:
        if random.randint(0, 100) <= DIRT_ADD_FREQUENCY:
            for i in range(DIRT_ADD_AMOUNT):
                newDirtX = random.randint(0, WIDTH - 1)
                newDirtY = random.randint(0, HEIGHT - 1)
                # Dirt piles max out at 3, so only add dirt if it's less than 3.
                if dirtPiles[(newDirtX, newDirtY)] < 3:
                    dirtPiles[(newDirtX, newDirtY)] += 1  # Add dirt to this (x, y) space.
                    bext.goto(newDirtX, newDirtY)
                    print(DIRT_CHARS[dirtPiles[(newDirtX, newDirtY)]], end='')

        # The roomba has reached its destination, so find the
        # closest dirt pile:
        if len(moveTo) == 0:
            closestDirtDistance = None
            closestDirts = []
            for dirtX in range(WIDTH):
                for dirtY in range(HEIGHT):
                    if dirtPiles[(dirtX, dirtY)] == 0:
                        continue  # Skip clean spots.
                    distance = getDistance(roombaX, roombaY, dirtX, dirtY)
                    if closestDirtDistance == None or distance < closestDirtDistance:
                        closestDirtDistance = distance
                        closestDirts = [(dirtX, dirtY)]
                    elif distance == closestDirtDistance:
                        closestDirts.append((dirtX, dirtY))
            if closestDirtDistance != None:
                closestDirtX, closestDirtY = random.choice(closestDirts)
                moveTo = line(roombaX, roombaY, closestDirtX, closestDirtY)[1:] # TODO don't include index 0 because that is the current roomba xy

        # Determine if the roomba should head back to base to recharge:
        distanceToDirt = len(moveTo)
        if len(moveTo) > 0:
            distanceFromDirtToBase = len(line(moveTo[-1][0], moveTo[-1][0], baseX, baseY)[1:])# TODO don't include index 0 be
        else:
            # There is no dirt to go to, so use 0:
            distanceFromDirtToBase = 0

        if distanceToDirt + distanceFromDirtToBase > roombaBattery:
            # Make the roomba go towards the base station:
            moveTo = line(roombaX, roombaY, baseX, baseY)[1:] # TODO skip [0]
            roombaStatus = RETURNING

        # If the roomba is charging at the base station, make it stay
        # there until it is fully charged:
        if roombaX == baseX and roombaY == baseY and roombaBattery < MAX_BATTERY:
            # Make the roomba stay where it is at the base station:
            moveTo = []

        if len(moveTo) > 0:
            # Move the roomba towards its destination:
            #assert moveTo[0][0] != roombaX and moveTo[0][1] != roombaY  # roomba should always be moving.

            # The roomba is moving, so reduce its battery:
            roombaBattery -= 1
            # Erase the roomba from the screen and draw the dirt that's there:
            bext.goto(roombaX, roombaY)
            print(DIRT_CHARS[dirtPiles[(roombaX, roombaY)]], end='')

            roombaX = moveTo[0][0]
            roombaY = moveTo[0][1]
            del moveTo[0]

        # Make the roomba suck up the dirt at its current location:
        dirtPiles[(roombaX, roombaY)] = 0

        # Recharge the roomba if it's at the base station:
        if roombaX == baseX and roombaY == baseY:
            roombaStatus = CHARGING
            roombaBattery += RECHARGE_RATE
            if roombaBattery > MAX_BATTERY:
                roombaBattery = MAX_BATTERY

        # Display the roomba:
        bext.goto(roombaX, roombaY)
        print(ROOMBA, end='')

        # Display the base station:
        bext.goto(baseX, baseY)
        print(BASE, end='')

        # Display the batter indicator on the bottom row:
        bext.goto(0, HEIGHT)
        print('Press Ctrl-C to quit. ', end='')
        print(roombaStatus, end='')
        print(' Battery:', str(round(roombaBattery / MAX_BATTERY * 100, 1)) + '%    ', end='')

        sys.stdout.flush()  # TODO
        time.sleep(PAUSE)


def getDistance(x1, y1, x2, y2):
    """Returns the distance between (x1, y1) and (x2, y2) by using the
    Pythagorean Theorem."""
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def line(x1, y1, x2, y2):
    """Returns a list of points in a line between the given points.

    Uses the Bresenham line algorithm. More info at:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""

    # Check for the special case where the start and end points are
    # certain neighbors, which this function doesn't handle correctly,
    # and return a hard coded list instead:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    points = []  # Contains the points of the line.
    # "Steep" means the slope of the line is greater than 45 degrees or
    # less than -45 degrees:
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


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
