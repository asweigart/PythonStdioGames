# Floodfill, by Al Sweigart al@inventwithpython.com

# This is a basic demo of both the recursive and iterative floodfill
# algorithms. This algorithm is commonly used in "fill tools" in
# graphics programs like MS Paint or Photoshop. This algorithm is
# also used in the floodit.py game.

import sys, random

# To reproduce the same random rectangles, use the same seed:
random.seed(42)

# Constants for the size of the field:
HEIGHT = 18
WIDTH = 50

NUM_RECTANGLES = 5 # How many random rectangles are drawn.
MIN_RECT_SIZE = 3 # Smallest size of the random rectangles.
NINE_SPACES = ' ' * 9 # Used when displaying x coordinates.

# Create a blank field:
field = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        field[(x, y)] = '.'

# Create random rectangles in the field:
for i in range(NUM_RECTANGLES):
    # Create a random rectangle's topleft corner and size:
    rectLeft = random.randint(0, WIDTH - MIN_RECT_SIZE)
    rectTop = random.randint(0, HEIGHT - MIN_RECT_SIZE)
    rectWidth = random.randint(MIN_RECT_SIZE, WIDTH - rectLeft)
    rectHeight = random.randint(MIN_RECT_SIZE, HEIGHT - rectTop)

    # Select a random character for this
    rectChar = random.choice('!@#*OX')

    for x in range(rectLeft, rectLeft + rectWidth):
        field[(x, rectTop)] = rectChar # Setup the top line.
        field[(x, rectTop + rectHeight - 1)] = rectChar # Setup bottom line.

    for y in range(rectTop, rectTop + rectHeight):
        field[(rectLeft, y)] = rectChar
        # Draw right line:
        field[(rectLeft + rectWidth - 1, y)] = rectChar


def recursiveFloodFill(field, x, y, newChar, curChar=None):
    if curChar == None:
        curChar = field[(x, y)]

    # Base case; just return:
    if curChar == newChar or field[(x, y)] != curChar:
        return

    field[(x, y)] = newChar # Change the character.

    # Recursive case; change the neighboring characters:
    if y + 1 < HEIGHT and field[(x, y + 1)] == curChar:
        recursiveFloodFill(field, x, y + 1, newChar, curChar)
    if y - 1 >= 0 and field[(x, y - 1)] == curChar:
        recursiveFloodFill(field, x, y - 1, newChar, curChar)
    if x + 1 < WIDTH and field[(x + 1, y)] == curChar:
        recursiveFloodFill(field, x + 1, y, newChar, curChar)
    if x - 1 >= 0 and field[(x - 1, y)] == curChar:
        recursiveFloodFill(field, x - 1, y, newChar, curChar)

def iterativeFloodFill(field, startx, starty, newChar):
    curChar = field[(startx, starty)]

    coordinatesToChange = [(startx, starty)]

    while len(coordinatesToChange) > 0:
        x, y = coordinatesToChange.pop()

        field[(x, y)] = newChar # Change the character.

        # Change the neighboring characters:
        if y + 1 < HEIGHT and field[(x, y + 1)] == curChar:
            coordinatesToChange.append((x, y + 1))
        if y - 1 >= 0 and field[(x, y - 1)] == curChar:
            coordinatesToChange.append((x, y - 1))
        if x + 1 < WIDTH and field[(x + 1, y)] == curChar:
            coordinatesToChange.append((x + 1, y))
        if x - 1 >= 0 and field[(x - 1, y)] == curChar:
            coordinatesToChange.append((x - 1, y))

def printField(field):
    print('   ', end='')
    for i in range(WIDTH // 10):
        print(str(i) + NINE_SPACES, end='')
    print()
    print('   ' + ('0123456789' * 10)[:WIDTH])

    for y in range(HEIGHT):
        # Print each row.
        print(str(y).rjust(2) + ' ', end='')
        for x in range(WIDTH):
            # Print each column.
            print(field[(x, y)], end='')
        print()
    print()

while True:
    printField(field)
    print('Enter "[x] [y] [char]" (e.g. "3 3 #", no quotes) or QUIT to quit:')

    response = input()

    if response.upper() == 'QUIT':
        sys.exit()

    response = response.split()
    if len(response) != 3:
        print('Invalid input. Enter something like "3 3 #" (without quotes).')

    x, y, newChar = response

    # Call either the recursive or iterative flood fill algorithms:
    # (They both do the same thing.)
    recursiveFloodFill(field, int(x), int(y), newChar)
    #iterativeFloodFill(field, int(x), int(y), newChar)
