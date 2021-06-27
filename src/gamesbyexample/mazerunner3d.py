"""Maze 3D, by Al Sweigart al@inventwithpython.com
Move around a maze and try to escape... in 3D!
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: extra-large, artistic, maze, game"""
__version__ = 0
import copy, sys, os

# Set up the constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)  # Character 9617 is '░'
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'


def wallStrToWallDict(wallStr):
    """Takes a string representation of a wall drawing (like those in
    ALL_OPEN or CLOSED) and returns a representation in a dictionary
    with (x, y) tuples as keys and single-character strings of the
    character to draw at that x, y location."""
    wallDict = {}
    height = 0
    width = 0
    for y, line in enumerate(wallStr.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wallDict[(x, y)] = character
    wallDict['height'] = height + 1
    wallDict['width'] = width + 1
    return wallDict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

# The way we create the strings to display is by converting the pictures
# in these multiline strings to dictionaries using wallStrToWallDict().
# Then we compose the wall for the player's location and direction by
# "pasting" the wall dictionaries in CLOSED on top of the wall dictionary
# in ALL_OPEN.

ALL_OPEN = wallStrToWallDict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())
# The strip() call is used to remove the newline
# at the start of this multiline string.

CLOSED = {}
CLOSED['A'] = wallStrToWallDict(r'''
_____
.....
.....
.....
_____'''.strip()) # Paste to 6, 4.

CLOSED['B'] = wallStrToWallDict(r'''
.\.
..\
...
...
...
../
./.'''.strip()) # Paste to 4, 3.

CLOSED['C'] = wallStrToWallDict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip()) # Paste to 3, 1.

CLOSED['D'] = wallStrToWallDict(r'''
./.
/..
...
...
...
\..
.\.'''.strip()) # Paste to 10, 3.

CLOSED['E'] = wallStrToWallDict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip()) # Paste to 0, 0.

CLOSED['F'] = wallStrToWallDict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip()) # Paste to 12, 0.

def displayWallDict(wallDict):
    """Display a wall dictionary, as returned by wallStrToWallDict(), on
    the screen."""
    print(BLOCK * (wallDict['width'] + 2))
    for y in range(wallDict['height']):
        print(BLOCK, end='')
        for x in range(wallDict['width']):
            wall = wallDict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print(BLOCK)  # Print block with a newline.
    print(BLOCK * (wallDict['width'] + 2))


def pasteWallDict(srcWallDict, dstWallDict, left, top):
    """Copy the wall representation dictionary in srcWallDict on top of
    the one in dstWallDict, offset to the position given by left, top."""
    dstWallDict = copy.copy(dstWallDict)
    for x in range(srcWallDict['width']):
        for y in range(srcWallDict['height']):
            dstWallDict[(x + left, y + top)] = srcWallDict[(x, y)]
    return dstWallDict


def makeWallDict(maze, playerx, playery, playerDirection, exitx, exity):
    """From the player's position and direction in the maze (which has
    an exit at exitx, exity), create the wall representation dictionary
    by pasting wall dictionaries on top of ALL_OPEN, then return it."""

    # The A-F "sections" (which are relative to the player's direction)
    # determine which walls in the maze we check to see if we need to
    # paste them over the wall representation dictionary we're creating.

    if playerDirection == NORTH:
        # Map of the sections, relative  A
        # to the player @:              BCD (Player facing north)
        #                               E@F
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if playerDirection == SOUTH:
        # Map of the sections, relative F@E
        # to the player @:              DCB (Player facing south)
        #                                A
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if playerDirection == EAST:
        # Map of the sections, relative EB
        # to the player @:              @CA (Player facing east)
        #                               FD
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if playerDirection == WEST:
        # Map of the sections, relative  DF
        # to the player @:              AC@ (Player facing west)
        #                                BE
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, xOff, yOff in offsets:
        section[sec] = maze.get((playerx + xOff, playery + yOff), WALL)
        if (playerx + xOff, playery + yOff) == (exitx, exity):
            section[sec] = EXIT

    wallDict = copy.copy(ALL_OPEN)
    PASTE_CLOSED_TO = {'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
                       'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wallDict = pasteWallDict(CLOSED[sec], wallDict,
                PASTE_CLOSED_TO[sec][0], PASTE_CLOSED_TO[sec][1])

    # Draw the EXIT sign if needed:
    if section['C'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 7, 9)
    if section['E'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 0, 11)
    if section['F'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 13, 11)

    return wallDict


print('Maze Runner 3D, by Al Sweigart al@inventwithpython.com')
print('(Maze files are generated by mazemakerrec.py)')

# Get the maze file's filename from the user:
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')

    # List all the maze files in the current folder:
    if filename.upper() == 'LIST':
        print('Maze files found in', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze')
            and fileInCurrentFolder.endswith('.txt')):
                print('  ', fileInCurrentFolder)
        continue

    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('There is no file named', filename)

# Load the maze from a file:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
px = None
py = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            px, py = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert px != None and py != None, 'No start point in file.'
assert exitx != None and exity != None, 'No exit point in file.'
pDir = NORTH


while True:  # Main game loop.
    displayWallDict(makeWallDict(maze, px, py, pDir, exitx, exity))

    while True: # Get user move.
        print('Location ({}, {})  Direction: {}'.format(px, py, pDir))
        print('                   (W)')
        print('Enter direction: (A) (D)  or QUIT.')
        move = input('> ').upper()

        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if (move not in ['F', 'L', 'R', 'W', 'A', 'D']
            and not move.startswith('T')):
            print('Please enter one of F, L, or R (or W, A, D).')
            continue

        # Move the player according to their intended move:
        if move == 'F' or move == 'W':
            if pDir == NORTH and maze[(px, py - 1)] == EMPTY:
                py -= 1
                break
            if pDir == SOUTH and maze[(px, py + 1)] == EMPTY:
                py += 1
                break
            if pDir == EAST and maze[(px + 1, py)] == EMPTY:
                px += 1
                break
            if pDir == WEST and maze[(px - 1, py)] == EMPTY:
                px -= 1
                break
        elif move == 'L' or move == 'A':
            pDir = {NORTH: WEST, WEST: SOUTH,
                    SOUTH: EAST, EAST: NORTH}[pDir]
            break
        elif move == 'R' or move == 'D':
            pDir = {NORTH: EAST, EAST: SOUTH,
                    SOUTH: WEST, WEST: NORTH}[pDir]
            break
        elif move.startswith('T'):  # Cheat code: 'T x,y'
            px, py = move.split()[1].split(',')
            px = int(px)
            py = int(py)
            break
        else:
            print('You cannot move in that direction.')

    if (px, py) == (exitx, exity):
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
