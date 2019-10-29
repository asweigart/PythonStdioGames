# Conway's Game of Life
# By Al Sweigart al@inventwithpython.com
# More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import random, time, copy
WIDTH = 79  # The width of the cell grid.
HEIGHT = 20 # The height of the cell grid.
ALIVE = 'O' # The character representing a living cell.
DEAD = ' '  # The character representing a dead cell.

# Create a list of list for the cells:
nextCells = {}
for x in range(WIDTH): # Loop over every possible column.
    for y in range(HEIGHT): # Loop over every possible row.
        # There is a 50/50 chance of the starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE # Add a living cell.
        else:
            nextCells[(x, y)] = DEAD # Add a dead cell.

while True: # Main program loop.
    # Each iteration of this loop is a step of the simulation.

    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[(x, y)], end='') # Print the # or space.
        print() # Print a newline at the end of the row.
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y):
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if currentCells[(leftCoord, aboveCoord)] == ALIVE:
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[(x, aboveCoord)] == ALIVE:
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[(rightCoord, aboveCoord)] == ALIVE:
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[(leftCoord, y)] == ALIVE:
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[(rightCoord, y)] == ALIVE:
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[(leftCoord, belowCoord)] == ALIVE:
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[(x, belowCoord)] == ALIVE:
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[(rightCoord, belowCoord)] == ALIVE:
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[(x, y)] = ALIVE
            elif currentCells[(x, y)] == DEAD and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                nextCells[(x, y)] = DEAD
    time.sleep(1) # Add a 1 second pause to reduce flickering.
