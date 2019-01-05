import os
import random
import sys
import time

FILLED = chr(9608)
EMPTY = ' '
PAUSE = 0.25 # How long to pause between each screen.

# Load the width and height from the command line arguments:
if len(sys.argv) == 3:
    WIDTH = sys.argv[1]
    HEIGHT = sys.argv[2]
else:
    WIDTH = 70
    HEIGHT = 20


def clear():
    # A cross-platform terminal window clearing function.
    if sys.platform == 'win32':
        os.system('cls') # Clears Windows terminal.
    else:
        os.system('clear') # Clears macOS and Linux terminal.


def getStateNumbers(width, height, screen):
    # Calculate the state numbers:
    state = ''
    for x in range(width):
        for y in range(height):
            if screen[x, y] == FILLED:
                state += '1'
            else:
                state += '0'
    return '%s %s %s' % (width, height, int(state, 2))


def getRandomScreen(width, height):
    # Create a random state:
    randomScreen = {}
    for x in range(width):
        for y in range(height):
            if random.randint(0, 1) == 0:
                randomScreen[x, y] = EMPTY
            else:
                randomScreen[x, y] = FILLED
    return randomScreen


# Load the initial state from the command line arguments:
nextScreen = {}
if len(sys.argv) == 4:
    # Load the state from the
    initialState = bin(int(sys.argv, 2)) # Convert decimal to binary number.
    initialState = initialState[2:] # Chop off the leading '0b'.
    i = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if initialState[i] == '0':
                nextScreen[x, y] = EMPTY
            else:
                nextScreen[x, y] = FILLED
else:
    nextScreen = getRandomScreen(WIDTH, HEIGHT)
initialStateNumbers = getStateNumbers(WIDTH, HEIGHT, nextScreen)

step = 0
try:
    while True: # Main program loop.
        clear()
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

        # If nextScreen and currentScreen are the same, quit.
        if nextScreen == currentScreen:
            print('Static state reached.')
            raise Exception()

        time.sleep(PAUSE) # Add a slight pause to reduce flickering.

except KeyboardInterrupt:
    # Display the state numbers:
    print('Initial State Numbers:')
    print(initialStateNumbers)
    print('Last State Numbers:')
    lastStateNumbers = getStateNumbers(WIDTH, HEIGHT, currentScreen)
    print(lastStateNumbers)

    # Attempt to copy state to clipboard with pyperclip, if available.
    try:
        import pyperclip
        pyperclip.copy(lastStateNumbers)
    except:
        pass
