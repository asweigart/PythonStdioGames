# Langton's Ant, by Al Sweigart al@inventwithpython.com
# A cellular automata animation. Press Ctrl-C to stop.
# More info: https://en.wikipedia.org/wiki/Langton%27s_ant
__version__ = 1

import random, copy, sys

try:
    import bext
except ImportError:
    print("""This program requires the bext module, which you can install
by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext""")
    sys.exit()


WIDTH = 79
HEIGHT = 22
NUMBER_OF_ANTS = 10

# Setup the screen:
bext.fg('yellow') # Set foreground color.
bext.bg('blue')   # Set background color.
bext.clear()

# Create a new board data structure:
board = {'width': WIDTH, 'height': HEIGHT}

# Create ant data structures:
ants = []
for i in range(NUMBER_OF_ANTS):
    ant = {'x': random.randint(0, WIDTH - 1),
           'y': random.randint(0, HEIGHT - 1),
           'direction': random.choice(['N', 'S', 'E', 'W'])}
    ants.append(ant)

try:
    while len(ants) > 0: # Keep running the simulation as long as we have ants.
        # Draw the board data structure:
        bext.goto(0, 0)
        for y in range(board['height']):
            for x in range(board['width']):
                if board.get((x, y), False):
                    print(chr(9608), end='') # Print a solid block.
                else:
                    print(' ', end='') # Print an empty space.
            print()
        print('Press Ctrl-C to quit.')

        # Run a single simulation step for each ant:
        nextBoard = copy.copy(board)
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                # Turn clockwise:
                if ant['direction'] == 'N':
                    ant['direction'] = 'E'
                elif ant['direction'] == 'E':
                    ant['direction'] = 'S'
                elif ant['direction'] == 'S':
                    ant['direction'] = 'W'
                elif ant['direction'] == 'W':
                    ant['direction'] = 'N'
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                # Turn counter clockwise:
                if ant['direction'] == 'N':
                    ant['direction'] = 'W'
                elif ant['direction'] == 'W':
                    ant['direction'] = 'S'
                elif ant['direction'] == 'S':
                    ant['direction'] = 'E'
                elif ant['direction'] == 'E':
                    ant['direction'] = 'N'

            # Move the ant forward:
            if ant['direction'] == 'N':
                ant['y'] -= 1
            if ant['direction'] == 'S':
                ant['y'] += 1
            if ant['direction'] == 'W':
                ant['x'] -= 1
            if ant['direction'] == 'E':
                ant['x'] += 1

            # If the ant goes past the edge of the screen, wrap around to other side.
            ant['x'] = ant['x'] % WIDTH - 1
            ant['y'] = ant['y'] % HEIGHT - 1

        board = nextBoard
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.
