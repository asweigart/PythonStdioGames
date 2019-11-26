# Conway's Game of Life (Terminal), by Al Sweigart al@inventwithpython.com
# The classic cellular automata simulation. Press Ctrl-C to stop.
# More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
__version__ = 1

# This program MUST be run in a Terminal/Command Prompt window.

import os, random, shutil, sys, time

WIDTH, HEIGHT = shutil.get_terminal_size()
HEIGHT = (HEIGHT - 1) * 2 # Leave a row free for "Press Ctrl-C..." message.

# Create random cells:
currentCells = {}
nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[x, y] = True

try:
    while True: # Main program loop.
        # Clear the previously drawn text:
        if sys.platform == 'win32':
            os.system('cls') # Clears Windows terminal.
        else:
            os.system('clear') # Clears macOS/Linux terminal.

        # Print the cells:
        currentCells = nextCells
        for y in range(0, HEIGHT, 2): # Skip every other row.
            for x in range(WIDTH):
                top = (x, y) in currentCells
                bottom = (x, y + 1) in currentCells

                if top and bottom:
                    print(chr(9608), end='') # Fill in both halves.
                elif top and not bottom:
                    print(chr(9600), end='') # Fill in top half.
                elif not top and bottom:
                    print(chr(9604), end='') # Fill in bottom half.
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

        time.sleep(0.25) # Add a slight pause to reduce flickering.
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.
