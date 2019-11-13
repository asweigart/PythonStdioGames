# Forest Fire Sim, by Al Sweigart al@inventwithpython.com
# Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/

import random, time, sys

try:
    import bext
except ImportError:
    print("""This program requires the bext module, which you can install by
opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext""")
    sys.exit()

WIDTH = 79
HEIGHT = 22

INITIAL_TREE_DENSITY = 20 # Percentage of board that starts with trees.
GROW_CHANCE = 1.0         # % chance a blank spot turns into a tree.
LIGHTNING_CHANCE = 0.1    # % chance a tree is hit by lightning & burns.

NUMBER_OF_FIREWALLS = 4
FIREWALL_LENGTH = 20
WALL_CHAR = chr(9608)

PAUSE_LENGTH = 0.05


# Create a new board data structure.
board = {'width': WIDTH, 'height': HEIGHT}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if (random.randint(1, 10000) / 100) <= INITIAL_TREE_DENSITY:
            board[(x, y)] = 'A' # Start as a tree.
        else:
            board[(x, y)] = ' ' # Start as an empty space.

# Create firewalls
for i in range(NUMBER_OF_FIREWALLS):
    if random.randint(0, 1) == 0:
        # Make a horizontal firewall:
        x = random.randint(0, max(WIDTH - FIREWALL_LENGTH - 1, 0))
        y = random.randint(0, HEIGHT)
        for ix in range(FIREWALL_LENGTH):
            board[(x + ix, y)] = WALL_CHAR
    else:
        # Make a vertical firewall:
        x = random.randint(0, WIDTH)
        y = random.randint(0, max(HEIGHT - (FIREWALL_LENGTH // 2) - 1, 0))
        for iy in range(FIREWALL_LENGTH // 2):
            board[(x, y + iy)] = WALL_CHAR

bext.clear()
try:
    while True:
        # Draw the board data structure.
        bext.goto(0, 0)
        for y in range(board['height']):
            for x in range(board['width']):
                if board[(x, y)] == 'A':
                    bext.fg('green')
                    print('A', end='')
                elif board[(x, y)] == 'W':
                    bext.fg('red')
                    print('W', end='')
                else:
                    bext.fg('reset')
                    print(board[(x, y)], end='')
            print()
        bext.fg('reset') # Use the default font color.
        print('Grow chance: %s%%  Lightning chance: %s%%' % (GROW_CHANCE, LIGHTNING_CHANCE))
        print('Press Ctrl-C to quit.')


        # Run a single simulation step:
        nextBoard = {'width': board['width'], 'height': board['height']}

        for x in range(board['width']):
            for y in range(board['height']):
                if (x, y) in nextBoard:
                    # If we've already set nextBoard[(x, y)] on a previous iteration, just do nothing here.
                    continue

                if board[(x, y)] == ' ' and (random.randint(1, 10000) / 100) <= GROW_CHANCE:
                    # Grow a tree in this empty space:
                    nextBoard[(x, y)] = 'A' # The letter 'A' sort of looks like a tree.
                elif board[(x, y)] == 'A' and (random.randint(1, 10000) / 100) <= LIGHTNING_CHANCE:
                    # Lightning sets this tree on fire:
                    nextBoard[(x, y)] = 'W'
                elif board[(x, y)] == 'W':
                    # Fire spreads to neighboring trees.
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            #if (0 <= x + ix < board['width']) and (0 <= y + iy < board['height']):
                            if (x + ix, y + iy) in board:
                                if board[(x + ix, y + iy)] == 'A':
                                    nextBoard[(x + ix, y + iy)] = 'W'
                                else:
                                    nextBoard[(x + ix, y + iy)] = board[(x + ix, y + iy)]
                    nextBoard[(x, y)] = ' ' # The original tree has burned down now.
                else:
                    # Just copy the existing object.
                    nextBoard[(x, y)] = board[(x, y)]
        board = nextBoard

        time.sleep(PAUSE_LENGTH)
except KeyboardInterrupt:
    pass # When Ctrl-C is pressed, stop looping.
