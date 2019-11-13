# Sand Fall (Bext Version), by Al Sweigart al@inventwithpython.com
# A falling sand animation.
# Inspired by https://asciinema.org/a/6515
# This program MUST be run in a Terminal/Command Prompt window.

import random, time, sys

try:
    import bext
except ImportError:
    print("""This program requires the bext module, which you can install by
opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext""")
    sys.exit()

WIDTH = 80
HEIGHT = 25

X = 0
Y = 1
PAUSE_LENGTH = 0.0
SAND = chr(9617) # Character 9617 is '░'

sources = [{'x': WIDTH // 2, 'y': 0, 'frequency': random.randint(2, 6), 'next': 1},
           {'x': 10, 'y': 0, 'frequency': random.randint(2, 6), 'next': 1},
           {'x': 30, 'y': 0, 'frequency': random.randint(2, 6), 'next': 1}]

bext.fg('yellow')
bext.clear()

allSand = []
while True:
    # Generate sand from each source.
    for source in sources:
        if source['next'] <= 0 and (source['x'], source['y']) not in allSand:
            allSand.append((source['x'], source['y']))
            bext.goto(source['x'], source['y'])
            print(SAND, end='')

            source['next'] = source['frequency']
        source['next'] -= 1

    # Simulate all sand in the sandspace.
    allSand.sort(key=lambda v: v[Y], reverse=True)

    for i, sand in enumerate(allSand):
        if sand[Y] == HEIGHT - 1:
            continue # Sand is on the very bottom, so it won't move at all.

        # If nothing is under this sand, move it down:
        if (sand[X], sand[Y] + 1) not in allSand:
            allSand[i] = (sand[X], sand[Y] + 1)
            bext.goto(sand[X], sand[Y])
            print(' ', end='')
            bext.goto(sand[X], sand[Y] + 1)
            print(SAND, end='')
        else:
            canFallLeft  = ((sand[X] - 1, sand[Y] + 1) not in allSand) and (sand[X] > 0)
            canFallRight = ((sand[X] + 1, sand[Y] + 1) not in allSand) and (sand[X] < WIDTH - 1)

            if canFallLeft and canFallRight:
                fallingDirection = random.choice((-1, 1))
            elif canFallLeft and not canFallRight:
                fallingDirection = -1
            elif not canFallLeft and canFallRight:
                fallingDirection = 1
            else:
                continue

            allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
            bext.goto(sand[X], sand[Y])
            print(' ', end='')
            bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
            print(SAND, end='')

    # Draw the sand space on the screen:
    time.sleep(PAUSE_LENGTH)


