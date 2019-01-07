import os
import random
import sys
import time

# Because the terminal characters are twice as tall as they are wide,
# we'll split each character into a possible "top" and "bottom" halves.
BOTH = chr(9608)
TOP = chr(9600)
BOTTOM = chr(9604)
EMPTY = ' '
PAUSE = 0.25 # How long to pause between each screen.

WIDTH = 70
HEIGHT = 40


# Create a random screen:
nextScreen = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextScreen[x, y] = False
        else:
            nextScreen[x, y] = True

step = 0
currentScreen = {}
try:
    while True: # Main program loop.
        # Clear the previously drawn text.
        if sys.platform == 'win32':
            os.system('cls') # Clears Windows terminal.
        else:
            os.system('clear') # Clears macOS and Linux terminal.

        currentScreen = nextScreen
        nextScreen = {}

        # Print the screen:
        for y in range(0, HEIGHT, 2): # Skip every other row.
            for x in range(WIDTH):
                top = currentScreen[x, y]
                bottom = y != HEIGHT - 1 and currentScreen[x, y + 1]

                if top and bottom:
                    print(BOTH, end='', flush=False)
                elif top and not bottom:
                    print(TOP, end='', flush=False)
                elif not top and bottom:
                    print(BOTTOM, end='', flush=False)
                elif not top and not bottom:
                    print(EMPTY, end='', flush=False)
            print('', flush=False) # Print a newline at the end of the row.
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
                topleft     = currentScreen[leftCoord, topCoord]
                top         = currentScreen[x, topCoord]
                topright    = currentScreen[rightCoord, topCoord]
                left        = currentScreen[leftCoord, y]
                right       = currentScreen[rightCoord, y]
                bottomleft  = currentScreen[leftCoord, bottomCoord]
                bottom      = currentScreen[x, bottomCoord]
                bottomright = currentScreen[rightCoord, bottomCoord]
                numNeighbors = topleft + top + topright + left + right + bottomleft + bottom + bottomright

                if currentScreen[x, y]:
                    if numNeighbors in (2, 3):
                        nextScreen[x, y] = True
                    else:
                        nextScreen[x, y] = False
                else:
                    if numNeighbors == 3:
                        nextScreen[x, y] = True
                    else:
                        nextScreen[x, y] = False

        # If nextScreen and currentScreen are the same, quit.
        if nextScreen == currentScreen:
            print('Static state reached.')
            raise KeyboardInterrupt()

        time.sleep(PAUSE) # Add a slight pause to reduce flickering.

except KeyboardInterrupt:
    pass