# Hour Glass Animation, by Al Sweigart al@inventwithpython.com
# https://asciinema.org/a/6515

import random, time, os, sys

WIDTH = 80
HEIGHT = 25

X = 0
Y = 1
PAUSE_LENGTH = 0.2
SAND = chr(9617) # Character 9617 is '░'

sources = [{'x': WIDTH // 2, 'y': 0, 'frequency': random.randint(2, 6), 'next': 1},
           {'x': 10, 'y': 0, 'frequency': random.randint(2, 6), 'next': 1},
           {'x': 30, 'y': 0, 'frequency': random.randint(2, 6), 'next': 1}]
sandspace = set() # Contains (x, y) tuples for each piece of sand.

while True:
    # Clear the previously drawn text:
    if sys.platform == 'win32':
        os.system('cls') # Clears Windows terminal.
    else:
        os.system('clear') # Clears macOS/Linux terminal.

    # Generate sand from each source.
    for source in sources:
        if source['next'] <= 0 and (source['x'], source['y']) not in sandspace:
            sandspace.add((source['x'], source['y']))
            source['next'] = source['frequency']
        source['next'] -= 1

    # Simulate all sand in the sandspace.
    allSand = list(sandspace)
    allSand.sort(key=lambda v: v[Y], reverse=True)

    for i, sand in enumerate(allSand):
        if sand[Y] == HEIGHT - 1:
            continue # Sand is on the very bottom, so it won't move at all.

        # If nothing is under this sand, move it down:
        if (sand[X], sand[Y] + 1) not in allSand:
            allSand[i] = (sand[X], sand[Y] + 1)
        else:
            canFallLeft  = ((sand[X] - 1, sand[Y] + 1) not in allSand) and (sand[X] > 0)
            canFallRight = ((sand[X] + 1, sand[Y] + 1) not in allSand) and (sand[X] < WIDTH - 1)

            if canFallLeft and canFallRight:
                allSand[i] = (sand[X] + random.choice((-1, 1)), sand[Y] + 1)
            elif canFallLeft and not canFallRight:
                allSand[i] = (sand[X] - 1, sand[Y] + 1)
            elif not canFallLeft and canFallRight:
                allSand[i] = (sand[X] + 1, sand[Y] + 1)

    # Draw the sand space on the screen:
    sandspace = set(allSand)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in sandspace:
                print(SAND, end='')
            else:
                print(' ', end='')
        print()

    time.sleep(PAUSE_LENGTH)


