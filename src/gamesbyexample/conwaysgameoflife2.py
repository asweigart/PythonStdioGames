# Conway's Game of Life (Terminal), by Al Sweigart al@inventwithpython.com
# The classic cellular automata simulation. Press Ctrl-C to stop.
# More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
__version__ = 1

# TODO - improve comments now that we have the anti-flicker features.
# TODO - note that the user shouldn't resize the window while it's running (add this comment to bouncing lines and bouncing balls programs also)
# This program MUST be run in a Terminal/Command Prompt window.

import os, random, shutil, sys, time

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

PAUSE_LENGTH = 0.25

WIDTH, HEIGHT = bext.size()
HEIGHT = (HEIGHT - 1) * 2 # Leave a row free for "Press Ctrl-C..." message.
WIDTH -= 1 # For a windows bug.

TOP_BLOCK = chr(9600) # Character 9600 is '▀'
BOTTOM_BLOCK = chr(9604) # Character 9604 is '▄'
FULL_BLOCK = chr(9608) # Character 9608 is '█'

# Create random cells:
currentCells = {}
nextCells = {}
previousCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[x, y] = True

bext.clear()
try:
    while True: # Main program loop.
        # Print the cells:
        previousCells = currentCells # Previous cells exists so we know which cells have changed, so we minimize flicker.
        currentCells = nextCells
        for y in range(0, HEIGHT, 2): # Skip every other row.
            for x in range(WIDTH):
                top = (x, y) in currentCells
                bottom = (x, y + 1) in currentCells

                if (previousCells.get((x, y), False) != currentCells.get((x, y), False)) or (previousCells.get((x, y + 1), False) != currentCells.get((x, y + 1), False)):
                    bext.goto(x, y // 2)
                    if top and bottom:
                        print(FULL_BLOCK, end='') # Fill in both halves.
                    elif top and not bottom:
                        print(TOP_BLOCK, end='') # Fill in top half.
                    elif not top and bottom:
                        print(BOTTOM_BLOCK, end='') # Fill in bottom half.
                    elif not top and not bottom:
                        print(' ', end='') # Fill in nothing.

            print('') # Print a newline at the end of the row.
        print('Press Ctrl-C to quit.', end='', flush=True)

        # Calculate next cells based on current cells:
        nextCells = {}
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get neighboring coordinates:
                leftCoord   = (x - 1) % WIDTH
                rightCoord  = (x + 1) % WIDTH
                topCoord    = (y - 1) % HEIGHT
                bottomCoord = (y + 1) % HEIGHT

                # Count number of living neighbors:
                numNeighbors = 0
                if (leftCoord, topCoord) in currentCells:
                    numNeighbors += 1
                if (x, topCoord) in currentCells:
                    numNeighbors += 1
                if (rightCoord, topCoord) in currentCells:
                    numNeighbors += 1
                if (leftCoord, y) in currentCells:
                    numNeighbors += 1
                if (rightCoord, y) in currentCells:
                    numNeighbors += 1
                if (leftCoord, bottomCoord) in currentCells:
                    numNeighbors += 1
                if (x, bottomCoord) in currentCells:
                    numNeighbors += 1
                if (rightCoord, bottomCoord) in currentCells:
                    numNeighbors += 1

                # Set cell based on Conway's Game of Life rules:
                if currentCells.get((x, y), False):
                    if numNeighbors in (2, 3):
                        nextCells[x, y] = True
                else:
                    if numNeighbors == 3:
                        nextCells[x, y] = True

        time.sleep(PAUSE_LENGTH) # Add a slight pause to reduce flickering.
        # At this point, go back to the start of the main program loop.
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.
