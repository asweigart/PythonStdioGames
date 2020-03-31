"""Forest Fire Sim, by Al Sweigart al@inventwithpython.com

A simulation of fires spreading in a growing forest.
Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
Tags: short, simulation, bext"""
__version__ = 0
import random, time, sys

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 21

TREE = 'A'
FIRE = 'W'
EMPTY = ' '
INITIAL_TREE_DENSITY = 20 # Percentage of forest that starts with trees.
GROW_CHANCE = 1.0         # % chance a blank spot turns into a tree.
LIGHTNING_CHANCE = 0.1    # % chance a tree is hit by lightning & burns.

PAUSE_LENGTH = 0.05


def main():
    """Run the Forest Fire simulation."""
    forest = createNewForest()

    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if (forest[(x, y)] == EMPTY) and (random.randint(1, 10000) / 100 <= GROW_CHANCE):
                    # Grow a tree in this empty space:
                    nextForest[(x, y)] = TREE
                elif (forest[(x, y)] == TREE) and (random.randint(1, 10000) / 100 <= LIGHTNING_CHANCE):
                    # Lightning sets this tree on fire:
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # Fire spreads to neighboring trees:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if (x + ix, y + iy) in forest:
                                if forest[(x + ix, y + iy)] == TREE:
                                    nextForest[(x + ix, y + iy)] = FIRE
                                else:
                                    nextForest[(x + ix, y + iy)] = forest[
                                        (x + ix, y + iy)
                                    ]
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)
        # At this point, go back to the start of the main program loop.


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.randint(1, 10000) / 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            else:
                bext.fg('reset')
                print(forest[(x, y)], end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  Lightning chance: {}%'.format(GROW_CHANCE, LIGHTNING_CHANCE))
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
