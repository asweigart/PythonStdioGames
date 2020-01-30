"""Hour Glass Animation, by Al Sweigart al@inventwithpython.com

An animation of an hour glass filled with falling sand.
Press Ctrl-C to stop."""
__version__ = 1
import random, time, sys

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

# Setup the constants:
WIDTH = 80
HEIGHT = 25

X = 0
Y = 1
PAUSE_LENGTH = 0.20
WIDE_FALL_CHANCE = 0.50
SAND = chr(9617)  # Character 9617 is '░'
WALL = chr(9608)  # Character 9608 is '█'

# Setup the walls and initial sand at the top of the hourglass:
ALL_WALLS = set([(18, 1), (36, 1), (18, 2), (36, 2), (18, 3), (36, 3), (18, 4), (36, 4), (19, 5), (35, 5), (20, 6), (34, 6), (21, 7), (33, 7), (22, 8), (32, 8), (23, 9), (31, 9), (24, 10), (30, 10), (25, 11), (29, 11), (26, 12), (28, 12), (25, 13), (29, 13), (24, 14), (30, 14), (23, 15), (31, 15), (22, 16), (32, 16), (21, 17), (33, 17), (20, 18), (34, 18), (19, 19), (35, 19), (18, 20), (36, 20), (18, 21), (36, 21), (18, 22), (36, 22), (18, 23), (36, 23)])
for i in range(18, 37):
    ALL_WALLS.add((i, 1))
    ALL_WALLS.add((i, 23))
INITIAL_SAND = set([(23, 8), (24, 8), (25, 8), (26, 8), (27, 8), (28, 8), (29, 8), (30, 8), (31, 8), (24, 9), (25, 9), (26, 9), (27, 9), (28, 9), (29, 9), (30, 9), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10), (26, 11), (27, 11), (28, 11)])
for i in range(19, 36):
    INITIAL_SAND.add((i, 3))
    INITIAL_SAND.add((i, 4))
for i in range(20, 35):
    INITIAL_SAND.add((i, 5))
for i in range(21, 34):
    INITIAL_SAND.add((i, 6))
for i in range(22, 33):
    INITIAL_SAND.add((i, 7))


def main():
    bext.fg('yellow')
    bext.clear()

    # Draw the quit message:
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # Draw the walls:
    for wall in ALL_WALLS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:  # Main program loop.
        allSand = list(INITIAL_SAND)
        # Mix up the order that the grains of sand are simulated:
        random.shuffle(allSand)

        # Draw the initial sand:
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        while True:  # Keep looping until sand has run out.
            # Simulate all sand in the sandspace:
            random.shuffle(allSand)  # Random order of grain simulation.

            sandMovedOnThisStep = False
            for i, sand in enumerate(allSand):
                if sand[Y] == HEIGHT - 1:
                    # Sand is on the very bottom, so it won't move:
                    continue

                # If nothing is under this sand, move it down:
                noSandBelow = (sand[X], sand[Y] + 1) not in allSand
                noWallBelow = (sand[X], sand[Y] + 1) not in ALL_WALLS
                canFallDown = noSandBelow and noWallBelow

                if canFallDown:
                    allSand[i] = (sand[X], sand[Y] + 1)
                    sandMovedOnThisStep = True
                    bext.goto(sand[X], sand[Y])
                    print(' ', end='')
                    bext.goto(sand[X], sand[Y] + 1)
                    print(SAND, end='')
                else:
                    # Check if the sand can fall to the left:
                    noSandBelowLeft = (sand[X] - 1, sand[Y] + 1) not in allSand
                    noWallBelowLeft = (sand[X] - 1, sand[Y] + 1) not in ALL_WALLS
                    noWallToTheLeft = (sand[X] - 1, sand[Y]) not in ALL_WALLS
                    notOnLeftEdge = sand[X] > 0
                    canFallLeft  = noSandBelowLeft and noWallBelowLeft and noWallToTheLeft and notOnLeftEdge

                    # Check if the sand can fall to the right:
                    noSandBelowRight = (sand[X] + 1, sand[Y] + 1) not in allSand
                    noWallBelowRight = (sand[X] + 1, sand[Y] + 1) not in ALL_WALLS
                    noWallToTheRight = (sand[X] + 1, sand[Y]) not in ALL_WALLS
                    notOnRightEdge = sand[X] < WIDTH - 1
                    canFallRight = noSandBelowRight and noWallBelowRight and noWallToTheRight and notOnRightEdge

                    fallingDirection = None
                    if canFallLeft and not canFallRight:
                        fallingDirection = -1
                    elif not canFallLeft and canFallRight:
                        fallingDirection = 1
                    elif canFallLeft and canFallRight:
                        fallingDirection = random.choice((-1, 1))

                    # Check if the sand can "wide" fall two spaces to
                    # the left or right:
                    if random.random() <= WIDE_FALL_CHANCE:
                        noSandBelowTwoLeft = (sand[X] - 2, sand[Y] + 1) not in allSand
                        noWallBelowTwoLeft = (sand[X] - 2, sand[Y] + 1) not in ALL_WALLS
                        notOnSecondToLeftEdge = sand[X] > 1
                        canFallTwoLeft  = canFallLeft and noSandBelowTwoLeft and noWallBelowTwoLeft and notOnSecondToLeftEdge

                        noSandBelowTwoRight = (sand[X] + 2, sand[Y] + 1) not in allSand
                        noWallBelowTwoRight = (sand[X] + 2, sand[Y] + 1) not in ALL_WALLS
                        notOnSecondToRightEdge = sand[X] < WIDTH - 2
                        canFallTwoRight = canFallRight and noSandBelowTwoRight and noWallBelowTwoRight and notOnSecondToRightEdge

                        if canFallTwoLeft and canFallTwoRight:
                            fallingDirection = random.choice((-2, 2))
                        elif canFallTwoLeft and not canFallTwoRight:
                            fallingDirection = -2
                        elif not canFallTwoLeft and canFallTwoRight:
                            fallingDirection = 2

                    if fallingDirection == None:
                        # This sand can't fall, so move on.
                        continue

                    # Move the grain of sand:
                    allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                    sandMovedOnThisStep = True
                    bext.goto(sand[X], sand[Y])
                    print(' ', end='')  # Erase old sand.
                    bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                    print(SAND, end='')  # Draw new sand.

            sys.stdout.flush()  # (Required for bext-using programs.)
            time.sleep(PAUSE_LENGTH)  # Pause after this

            # If no sand has moved on this step, reset the hourglass:
            if not sandMovedOnThisStep:
                time.sleep(2)
                # Erase the sand:
                for sand in allSand:
                    bext.goto(sand[X], sand[Y])
                    print(' ', end='')
                break  # Break out of main simulation loop.
            # At this point, go back to the start of the loop.
    # At this point, go back to the start of the main program loop.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
