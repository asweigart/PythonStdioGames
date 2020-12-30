"""Hour Glass Animation, by Al Sweigart al@inventwithpython.com
An animation of an hour glass with falling sand. Press Ctrl-C to stop.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, simulation, terminal"""
__version__ = 0
import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
PAUSE_LENGTH = 0.2  # (!) Try changing this to 0.0 or 1.0.
# (!) Try changing this to any number between 0 and 100:
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0  # The index of X values in an (x, y) tuple is 0.
Y = 1  # The index of Y values in an (x, y) tuple is 1.
SAND = chr(9617)  # Character 9617 is '░'
WALL = chr(9608)  # Character 9608 is '█'

# Set up the walls of the hour glass:
HOURGLASS = set()  # Has (x, y) tuples for where hourglass walls are.
# (!) Try commenting out some HOURGLASS.add() lines to erase walls:
for i in range(18, 37):
    HOURGLASS.add((i, 1))  # Add walls for the top cap of the hourglass.
    HOURGLASS.add((i, 23))  # Add walls for the bottom cap.
for i in range(1, 5):
    HOURGLASS.add((18, i))  # Add walls for the top left straight wall.
    HOURGLASS.add((36, i))  # Add walls for the top right straight wall.
    HOURGLASS.add((18, i + 19))  # Add walls for the bottom left.
    HOURGLASS.add((36, i + 19))  # Add walls for the bottom right.
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  # Add the top left slanted wall.
    HOURGLASS.add((35 - i, 5 + i))  # Add the top right slanted wall.
    HOURGLASS.add((25 - i, 13 + i))  # Add the bottom left slanted wall.
    HOURGLASS.add((29 + i, 13 + i))  # Add the bottom right slanted wall.

# Set up the initial sand at the top of the hourglass:
INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()

    # Draw the quit message:
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # Display the walls of the hourglass:
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:  # Main program loop.
        allSand = list(INITIAL_SAND)

        # Draw the initial sand:
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        runHourglassSimulation(allSand)


def runHourglassSimulation(allSand):
    """Keep running the sand falling simulation until the sand stops
    moving."""
    while True:  # Keep looping until sand has run out.
        random.shuffle(allSand)  # Random order of grain simulation.

        sandMovedOnThisStep = False
        for i, sand in enumerate(allSand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                # Sand is on the very bottom, so it won't move:
                continue

            # If nothing is under this sand, move it down:
            noSandBelow = (sand[X], sand[Y] + 1) not in allSand
            noWallBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                # Draw the sand in its new position down one space:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Clear the old position.
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # Set the sand in its new position down one space:
                allSand[i] = (sand[X], sand[Y] + 1)
                sandMovedOnThisStep = True
            else:
                # Check if the sand can fall to the left:
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (noSandBelowLeft and noWallBelowLeft
                    and noWallLeft and notOnLeftEdge)

                # Check if the sand can fall to the right:
                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                noWallBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (noSandBelowRight and noWallBelowRight
                    and noWallRight and notOnRightEdge)

                # Set the falling direction:
                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1  # Set the sand to fall left.
                elif not canFallLeft and canFallRight:
                    fallingDirection = 1  # Set the sand to fall right.
                elif canFallLeft and canFallRight:
                    # Both are possible, so randomly set it:
                    fallingDirection = random.choice((-1, 1))

                # Check if the sand can "far" fall two spaces to
                # the left or right instead of just one space:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in allSand
                    noWallBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = (canFallLeft and noSandBelowTwoLeft
                        and noWallBelowTwoLeft and notOnSecondToLeftEdge)

                    belowTwoRight = (sand[X] + 2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in allSand
                    noWallBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] < SCREEN_WIDTH - 2
                    canFallTwoRight = (canFallRight
                        and noSandBelowTwoRight and noWallBelowTwoRight
                        and notOnSecondToRightEdge)

                    if canFallTwoLeft and not canFallTwoRight:
                        fallingDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection == None:
                    # This sand can't fall, so move on.
                    continue

                # Draw the sand in its new position:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Erase old sand.
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                print(SAND, end='')  # Draw new sand.

                # Move the grain of sand to its new position:
                allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(PAUSE_LENGTH)  # Pause after this

        # If no sand has moved on this step, reset the hourglass:
        if not sandMovedOnThisStep:
            time.sleep(2)
            # Erase all of the sand:
            for sand in allSand:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break  # Break out of main simulation loop.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
