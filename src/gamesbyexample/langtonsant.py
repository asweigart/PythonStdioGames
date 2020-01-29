"""Langton's Ant, by Al Sweigart al@inventwithpython.com

A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant"""
__version__ = 1

import random, copy, sys

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

# Setup the constants:
WIDTH, HEIGHT = 70, 20 #bext.size()
WIDTH -= 1  # Adjustment for Windows Command Prompt.
HEIGHT -= 1  # Adjustment for the quit message at the bottom.
NUMBER_OF_ANTS = 1
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

BLACK = 'black'
WHITE = 'white'

def main():
    """Run the Langton's Ant simulation."""
    bext.fg('red')
    bext.bg(WHITE)  # Set the background to white to start.
    bext.clear()

    # Create a new board data structure:
    board = {'width': WIDTH, 'height': HEIGHT}

    # Create ant data structures:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {'x': 10,#random.randint(0, WIDTH - 1),
               'y': 10,#random.randint(0, HEIGHT - 1),
               'direction': random.choice([NORTH, SOUTH, EAST, WEST])}
        ants.append(ant)

    while True: # Main program loop.
        displayBoard(board, ants)

        # Run a single simulation step for each ant:
        nextBoard = copy.copy(board)
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                # Turn clockwise:
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                # Turn counter clockwise:
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH

            # Move the ant forward:
            if ant['direction'] == NORTH:
                ant['y'] -= 1
            if ant['direction'] == SOUTH:
                ant['y'] += 1
            if ant['direction'] == WEST:
                ant['x'] -= 1
            if ant['direction'] == EAST:
                ant['x'] += 1

            # If the ant goes past the edge of the screen,
            # it should wrap around to other side.
            ant['x'] = ant['x'] % (WIDTH - 1)
            ant['y'] = ant['y'] % (HEIGHT - 1)

        board = nextBoard
        # At this point, go back to the start of the main program loop.


def displayBoard(board, ants):
    # Draw the board data structure:
    bext.goto(0, 0)
    for y in range(board['height']):
        for x in range(board['width']):
            if board.get((x, y), False):
                bext.bg(BLACK)
            else:
                bext.bg(WHITE)

            for ant in ants:
                if (x, y) == (ant['x'], ant['y']):
                    if ant['direction'] == NORTH:
                        print('^', end='')
                    elif ant['direction'] == SOUTH:
                        print('v', end='')
                    elif ant['direction'] == EAST:
                        print('>', end='')
                    elif ant['direction'] == WEST:
                        print('<', end='')
                else:
                    print(' ', end='')
        print()
    print('Press Ctrl-C to quit.')
    sys.stdout.flush()  # (Required for bext-using programs.)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # When Ctrl-C is pressed, end the program.
