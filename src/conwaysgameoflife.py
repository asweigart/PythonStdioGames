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
                if x == 0:
                    leftCoord = WIDTH - 1 # wraparound
                else:
                    leftCoord = x - 1
                if x == WIDTH - 1:
                    rightCoord = 0 # wraparound
                else:
                    rightCoord = x + 1
                if y == 0:
                    topCoord = HEIGHT - 1 # wraparound
                else:
                    topCoord = y - 1
                if y == HEIGHT - 1:
                    bottomCoord = 0 # wraparound
                else:
                    bottomCoord = y + 1

                # Get neighbors:
                topleft     = (leftCoord, topCoord) in currentCells
                top         = (x, topCoord) in currentCells
                topright    = (rightCoord, topCoord) in currentCells
                left        = (leftCoord, y) in currentCells
                right       = (rightCoord, y) in currentCells
                bottomleft  = (leftCoord, bottomCoord) in currentCells
                bottom      = (x, bottomCoord) in currentCells
                bottomright = (rightCoord, bottomCoord) in currentCells
                numNeighbors = topleft + top + topright + left + right + bottomleft + bottom + bottomright

                # Set cell based on Conway's Game of Life rules:
                if currentCells.get((x, y), False):
                    if numNeighbors in (2, 3):
                        nextCells[x, y] = True
                else:
                    if numNeighbors == 3:
                        nextCells[x, y] = True

        time.sleep(0.25) # Add a slight pause to reduce flickering.
except KeyboardInterrupt:
    pass
