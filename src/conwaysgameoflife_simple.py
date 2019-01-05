import os
import random
import sys
import time

FILLED = chr(9608)
EMPTY = ' '
PAUSE = 0.25 # How long to pause between each screen.
WIDTH = 70
HEIGHT = 20

# Create a random screen:
nextScreen = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextScreen[x, y] = EMPTY
        else:
            nextScreen[x, y] = FILLED

step = 0
try:
    while True: # Main program loop.
        if sys.platform == 'win32':
            os.system('cls') # Clears Windows terminal.
        else:
            os.system('clear') # Clears macOS and Linux terminal.

        currentScreen = nextScreen
        nextScreen = {}

        # Print the screen:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentScreen[x, y], end='', flush=False)
            print('', flush=False)
        print('Step:', step)
        step += 1
        print('Press Ctrl-C or Ctrl-D to quit.')

        # Calculate next screen based on current screen:
        for x in range(WIDTH):
            for y in range(HEIGHT):

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

                # Determine neighbors:
                topleft     = currentScreen[leftCoord, topCoord]     == FILLED
                top         = currentScreen[x, topCoord]             == FILLED
                topright    = currentScreen[rightCoord, topCoord]    == FILLED
                left        = currentScreen[leftCoord, y]            == FILLED
                right       = currentScreen[rightCoord, y]           == FILLED
                bottomleft  = currentScreen[leftCoord, bottomCoord]  == FILLED
                bottom      = currentScreen[x, bottomCoord]          == FILLED
                bottomright = currentScreen[rightCoord, bottomCoord] == FILLED
                numNeighbors = topleft + top + topright + left + right + bottomleft + bottom + bottomright

                if currentScreen[x, y] == FILLED:
                    if numNeighbors in (2, 3):
                        nextScreen[x, y] = FILLED
                    else:
                        nextScreen[x, y] = EMPTY
                else:
                    if numNeighbors == 3:
                        nextScreen[x, y] = FILLED
                    else:
                        nextScreen[x, y] = EMPTY

        time.sleep(PAUSE) # Add a slight pause to reduce flickering.

except KeyboardInterrupt:
    pass # Just quit.
