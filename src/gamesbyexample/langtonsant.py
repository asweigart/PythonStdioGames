"""Langton's Ant, by Al Sweigart al@inventwithpython.com
A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant
This and other games are available at https://nostarch.com/XX
Tags: large, simulation, bext, artistic"""
__version__ = 0
import copy, random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1
HEIGHT -= 1  # Adjustment for the quit message at the bottom.

NUMBER_OF_ANTS = 10  # (!) Try changing this to 1 or 50.
PAUSE_AMOUNT = 0.1  # (!) Try changing this to 1.0 or 0.0.

# (!) Try changing these to make the ants look different:
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) Try changing these colors to one of 'black', 'red', 'green',
# 'yellow', 'blue', 'purple', 'cyan', or 'white'. (These are the only
# colors that the bext module supports.)
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def main():
    bext.fg(ANT_COLOR)  # The ants' color is the foreground color.
    bext.bg(WHITE_TILE)  # Set the background to white to start.
    bext.clear()

    # Create a new board data structure:
    board = {'width': WIDTH, 'height': HEIGHT}

    # Create ant data structures:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    # Keep track of which tiles have changed and need to be redrawn on
    # the screen:
    changedTiles = []

    while True:  # Main program loop.
        displayBoard(board, ants, changedTiles)
        changedTiles = []

        # nextBoard is what the board will look like on the next step in
        # the simulation. Start with a copy of the current step's board:
        nextBoard = copy.copy(board)

        # Run a single simulation step for each ant:
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
            changedTiles.append((ant['x'], ant['y']))

            # Move the ant forward in whatever direction it's facing:
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
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changedTiles.append((ant['x'], ant['y']))

        board = nextBoard


def displayBoard(board, ants, changedTiles):
    """Displays the board and ants on the screen. The changedTiles
    argument is a list of (x, y) tuples for tiles on the screen that
    have changed and need to be redrawn."""

    # Draw the board data structure:
    for x, y in changedTiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        antIsHere = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT, end='')
                break
        if not antIsHere:
            print(' ', end='')

    # Display the quit message at the bottom of the screen:
    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush()  # (Required for bext-using programs.)
    time.sleep(PAUSE_AMOUNT)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
