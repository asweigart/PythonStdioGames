# Etch a Sketch, by Al Sweigart al@inventwithpython.com

import sys

# Set up some constants
UP_DOWN_CHAR    = chr(9474) # The '│' string.
LEFT_RIGHT_CHAR = chr(9472) # The '─' string.
DOWN_RIGHT_CHAR = chr(9484) # The '┌' string.
DOWN_LEFT_CHAR  = chr(9488) # The '┐' string.
UP_RIGHT_CHAR   = chr(9492) # The '└' string.
UP_LEFT_CHAR    = chr(9496) # The '┘' string.

UP_DOWN_RIGHT_CHAR   = chr(9500) # The '├' string.
UP_DOWN_LEFT_CHAR    = chr(9508) # The '┤' string.
DOWN_LEFT_RIGHT_CHAR = chr(9516) # The '┬' string.
UP_LEFT_RIGHT_CHAR   = chr(9524) # The '┴' string.

CROSS_CHAR = chr(9532) # The '┼' string.
BLOCK_CHAR = chr(9608) # The '█' string.

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 20


screen = {} # Keys will be (x, y) tuples, value is a set of WASD letters that should be drawn for this cell.
cursorx = 0
cursory = 0

def getScreenString(screenData):
    screenStr = ''

    for rowNum in range(SCREEN_HEIGHT):
        for columnNum in range(SCREEN_WIDTH):
            cell = screen.get((columnNum, rowNum), ' ')
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
        screenStr += '\n' # Print a newline at the end of each row.
    return screenStr

while True: # Main application loop.

    # Draw the screen:
    print(getScreenString(screen))

    print('Enter WASD keys to move, C to clear, F to save to file, Q to quit.')
    response = input().upper()

    for command in response:
        if command == 'C':
            screen = {}
        elif command == 'Q':
            sys.exit()
        elif command == 'F':
            try:
                print('Enter filename to save to:')
                response = input()
                file = open(response, 'w', encoding='utf-8')
                file.write(getScreenString(screen))
                file.close()
            except:
                print('ERROR: Could not save file.')
        elif command in ('W', 'A', 'S', 'D'):
            # For the first move, we draw in the other direction as well. # TODO fix this comment
            if screen == {}:
                if command in ('W', 'S'):
                    screen[(cursorx, cursory)] = set(['W', 'S'])
                elif command in ('A', 'D'):
                    screen[(cursorx, cursory)] = set(['A', 'D'])

            screen[(cursorx, cursory)].add(command)

            # Update x and y.
            if command == 'W':
                cursory = cursory - 1
            elif command == 'S':
                cursory = cursory + 1
            elif command == 'A':
                cursorx = cursorx - 1
            elif command == 'D':
                cursorx = cursorx + 1

            # Make sure x and y doesn't go beyond the border:
            if cursorx < 0:
                cursorx = 0
            elif cursorx == SCREEN_WIDTH:
                cursorx = SCREEN_WIDTH - 1
            if cursory < 0:
                cursory = 0
            elif cursory == SCREEN_HEIGHT:
                cursory = SCREEN_HEIGHT - 1

            if (cursorx, cursory) not in screen:
                screen[(cursorx, cursory)] = set()
            if command == 'W':
                screen[(cursorx, cursory)].add('S')
            elif command == 'S':
                screen[(cursorx, cursory)].add('W')
            elif command == 'A':
                screen[(cursorx, cursory)].add('D')
            elif command == 'D':
                screen[(cursorx, cursory)].add('A')






