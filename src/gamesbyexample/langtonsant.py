"""Langton's Ant, by Al Sweigart al@inventwithpython.com
A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant
This and other games are available at https://nostarch.com/XX
Tags: large, simulation, bext, artistic"""
__version__ = 0
import random, copy, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
HEIGHT -= 1  # Adjustment for the quit message at the bottom.
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_ANTS = 10
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
BLACK = 'black'
WHITE = 'white'
PAUSE_AMOUNT = 0.1


def main():
    bext.fg('red')
    bext.bg(WHITE)  # Set the background to white to start.
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

    changedTiles = set()

    while True:  # Main program loop.
        displayBoard(board, ants, changedTiles)
        changedTiles = set()

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
            changedTiles.add((ant['x'], ant['y']))

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
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changedTiles.add((ant['x'], ant['y']))

        board = nextBoard


def displayBoard(board, ants, changedTiles):
    # Draw the board data structure:
    for x, y in changedTiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK)
        else:
            bext.bg(WHITE)

        antIsHere = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print('^', end='')
                elif ant['direction'] == SOUTH:
                    print('v', end='')
                elif ant['direction'] == EAST:
                    print('>', end='')
                elif ant['direction'] == WEST:
                    print('<', end='')
                break
        if not antIsHere:
            print(' ', end='')

    bext.goto(0, HEIGHT)
    bext.bg(WHITE)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush()  # (Required for bext-using programs.)
    time.sleep(PAUSE_AMOUNT)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
