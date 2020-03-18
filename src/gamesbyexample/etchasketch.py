"""Etch a Sketch, by Al Sweigart al@inventwithpython.com

An art program that draws a continuous line around the screen using the
WASD keys.

For example, you can draw Hilbert Curve fractal with:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

Or an even larger Hilbert Curve fractal with:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD
"""
__version__ = 1

import sys

# Set up the constants:
UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 20

"""The keys for screen will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn."""
screen = {}
cursorx = 0
cursory = 0


def getScreenString(screenData, cx, cy):
    """Returns a multiline string of the line drawn in screenData."""
    screenStr = ''

    """screenData is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point."""
    for rowNum in range(SCREEN_HEIGHT):
        for columnNum in range(SCREEN_WIDTH):
            if columnNum == cx and rowNum == cy:
                screenStr += '#'
                continue

            # Add the line character for this point to screenStr.
            cell = screenData.get((columnNum, rowNum), ' ')
            if cell == set(['W', 'S']):
                screenStr += UP_DOWN_CHAR
            elif cell == set(['A', 'D']):
                screenStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                screenStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                screenStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                screenStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                screenStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                screenStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                screenStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                screenStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                screenStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                screenStr += CROSS_CHAR
            else:
                screenStr += ' '
        screenStr += '\n'  # Add a newline at the end of each row.
    return screenStr


while True:  # Main program loop.
    # Draw the lines based on the data in screen:
    print(getScreenString(screen, cursorx, cursory))

    print('WASD keys to move, H for help, C to clear, F to save, or QUIT.')
    response = input().upper()

    if response == 'QUIT':
        sys.exit()  # Quit the program.
    elif response == 'H':
        print('Enter W, A, S, and D keys to move the cursor and draw a')
        print('line behind it as it moves. For example, enter ddd to')
        print('draw a line going right or sssdddwwwaa to draw a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        print('Press Enter to return to the program...')
        input()
        continue
    elif response == 'C':
        screen = {}  # Erase the screen data.
    elif response == 'F':
        # Save the screen string to a text file:
        try:
            print('Enter filename to save to:')
            filename = input()

            # Make sure the filename ends with .txt:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(getScreenString(screen, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue  # Ignore this letter and continue to the next one.

        # The first line we add needs to form a full line:
        if screen == {}:
            if command in ('W', 'S'):
                # Make the first line a horizontal one:
                screen[(cursorx, cursory)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                # Make the first line a vertical one:
                screen[(cursorx, cursory)] = set(['A', 'D'])

        screen[(cursorx, cursory)].add(command)

        # Update x and y:
        if command == 'W':
            cursory = cursory - 1
        elif command == 'S':
            cursory = cursory + 1
        elif command == 'A':
            cursorx = cursorx - 1
        elif command == 'D':
            cursorx = cursorx + 1

        # Make sure x and y doesn't go beyond the screen border:
        if cursorx < 0:  # Check if x is past the left border...
            cursorx = 0
        elif cursorx == SCREEN_WIDTH:  # ...or the right border.
            cursorx = SCREEN_WIDTH - 1
        if cursory < 0:  # Check if y i past the top border...
            cursory = 0
        elif cursory == SCREEN_HEIGHT:  # ...or the bottom border.
            cursory = SCREEN_HEIGHT - 1

        # If there's no set for (cursorx, cursory), add an empty set:
        if (cursorx, cursory) not in screen:
            screen[(cursorx, cursory)] = set()

        # Add the direction string to this xy point's set:
        if command == 'W':
            screen[(cursorx, cursory)].add('S')
        elif command == 'S':
            screen[(cursorx, cursory)].add('W')
        elif command == 'A':
            screen[(cursorx, cursory)].add('D')
        elif command == 'D':
            screen[(cursorx, cursory)].add('A')
