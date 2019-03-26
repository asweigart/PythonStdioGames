# Hour Glass Animation, by Al Sweigart al@inventwithpython.com

import random, time, bext

WIDTH = 80
HEIGHT = 25

X = 0
Y = 1
PAUSE_LENGTH = 0.20
WIDE_FALL_CHANCE = 0.50
SAND = chr(9617) # Character 9617 is '░'
WALL = chr(9608) # Character 9608 is '█'

bext.fg('yellow')

ALL_WALLS = set([(18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0), (30, 0), (31, 0), (32, 0), (33, 0), (34, 0), (35, 0), (36, 0), (18, 1), (36, 1), (18, 2), (36, 2), (18, 3), (36, 3), (18, 4), (36, 4), (19, 5), (35, 5), (20, 6), (34, 6), (21, 7), (33, 7), (22, 8), (32, 8), (23, 9), (31, 9), (24, 10), (30, 10), (25, 11), (29, 11), (26, 12), (28, 12), (25, 13), (29, 13), (24, 14), (30, 14), (23, 15), (31, 15), (22, 16), (32, 16), (21, 17), (33, 17), (20, 18), (34, 18), (19, 19), (35, 19), (18, 20), (36, 20), (18, 21), (36, 21), (18, 22), (36, 22), (18, 23), (36, 23), (18, 24), (19, 24), (20, 24), (21, 24), (22, 24), (23, 24), (24, 24), (25, 24), (26, 24), (27, 24), (28, 24), (29, 24), (30, 24), (31, 24), (32, 24), (33, 24), (34, 24), (35, 24), (36, 24)])
INITAL_SAND = ((19, 2), (20, 2), (21, 2), (22, 2), (23, 2), (24, 2), (25, 2), (26, 2), (27, 2), (28, 2), (29, 2), (30, 2), (31, 2), (32, 2), (33, 2), (34, 2), (35, 2), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3), (27, 3), (28, 3), (29, 3), (30, 3), (31, 3), (32, 3), (33, 3), (34, 3), (35, 3), (19, 4), (20, 4), (21, 4), (22, 4), (23, 4), (24, 4), (25, 4), (26, 4), (27, 4), (28, 4), (29, 4), (30, 4), (31, 4), (32, 4), (33, 4), (34, 4), (35, 4), (20, 5), (21, 5), (22, 5), (23, 5), (24, 5), (25, 5), (26, 5), (27, 5), (28, 5), (29, 5), (30, 5), (31, 5), (32, 5), (33, 5), (34, 5), (21, 6), (22, 6), (23, 6), (24, 6), (25, 6), (26, 6), (27, 6), (28, 6), (29, 6), (30, 6), (31, 6), (32, 6), (33, 6), (22, 7), (23, 7), (24, 7), (25, 7), (26, 7), (27, 7), (28, 7), (29, 7), (30, 7), (31, 7), (32, 7), (23, 8), (24, 8), (25, 8), (26, 8), (27, 8), (28, 8), (29, 8), (30, 8), (31, 8), (24, 9), (25, 9), (26, 9), (27, 9), (28, 9), (29, 9), (30, 9), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10), (26, 11), (27, 11), (28, 11))

bext.clear()
# Draw the walls:
for wall in ALL_WALLS:
    bext.goto(wall[X], wall[Y])
    print(WALL, end='')

try:
    while True:
        allSand = list(INITAL_SAND)
        random.shuffle(allSand) # Mix up the order that the grains of sand are simulated.

        # Draw the initial sand:
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        while True: # Main simulation loop.
            # Draw the quit message:
            bext.goto(0, 0)
            print('Ctrl-C to quit.', end='')

            # Simulate all sand in the sandspace:
            #allSand.sort(key=lambda v: v[Y], reverse=True) # Sort from bottom sand up.
            random.shuffle(allSand) # Random order of grain simulation.

            sandMoved = False
            for i, sand in enumerate(allSand):
                if sand[Y] == HEIGHT - 1:
                    continue # Sand is on the very bottom, so it won't move at all.

                # If nothing is under this sand, move it down:
                noSandBelow = (sand[X], sand[Y] + 1) not in allSand
                noWallBelow = (sand[X], sand[Y] + 1) not in ALL_WALLS
                canFallDown = noSandBelow and noWallBelow

                if canFallDown:
                    allSand[i] = (sand[X], sand[Y] + 1)
                    sandMoved = True
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
                    if canFallLeft and canFallRight:
                        fallingDirection = random.choice((-1, 1))
                    elif canFallLeft and not canFallRight:
                        fallingDirection = -1
                    elif not canFallLeft and canFallRight:
                        fallingDirection = 1

                    # Check if the sand can fall two spaces to the left or right:
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

                    if fallingDirection is None:
                        continue # This sand can't fall, so move on to the next grain of sand.

                    # Move the grain of sand:
                    allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                    sandMoved = True
                    bext.goto(sand[X], sand[Y])
                    print(' ', end='')
                    bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                    print(SAND, end='')

            time.sleep(PAUSE_LENGTH)

            if not sandMoved:
                time.sleep(2)
                # Erase the sand:
                for sand in allSand:
                    bext.goto(sand[X], sand[Y])
                    print(' ', end='')
                break # Break out of main simultion loop to reset the hour glass.
except KeyboardInterrupt:
    pass
