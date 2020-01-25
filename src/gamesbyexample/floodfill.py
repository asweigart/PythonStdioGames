"""Flood Fill, by Al Sweigart al@inventwithpython.com

An example of a "flood fill" algorithm.
This is a basic demo of both the recursive and iterative floodfill
algorithms. This algorithm is commonly used in "fill tools" in
graphics programs like MS Paint or Photoshop. This algorithm is
also used in the floodit.py game."""
__version__ = 1

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

    # Select a random character for this rectangle:
    rectChar = random.choice('!@#*OX')

    # Setup the rectangle to the field data structure:
    for x in range(rectLeft, rectLeft + rectWidth):
        field[(x, rectTop)] = rectChar # Setup the top line.
        field[(x, rectTop + rectHeight - 1)] = rectChar # Setup bottom line.

    for y in range(rectTop, rectTop + rectHeight):
        field[(rectLeft, y)] = rectChar
        # Draw right line:
        field[(rectLeft + rectWidth - 1, y)] = rectChar


def recursiveFloodFill(field, x, y, newChar, curChar=None):
    if curChar == None:
        # If the current character isn't given, use the char at field[(x, y)].
        curChar = field[(x, y)]

    # Base case; just return:
    if curChar == newChar or field[(x, y)] != curChar:
        return

    field[(x, y)] = newChar # Change the character.

    # Recursive case; change the neighboring characters:
    if y + 1 < HEIGHT and field[(x, y + 1)] == curChar:
        # Call recursiveFloodFill() on the southern neighbor:
        recursiveFloodFill(field, x, y + 1, newChar, curChar)
    if y - 1 >= 0 and field[(x, y - 1)] == curChar:
        # Call recursiveFloodFill() on the northern neighbor:
        recursiveFloodFill(field, x, y - 1, newChar, curChar)
    if x + 1 < WIDTH and field[(x + 1, y)] == curChar:
        # Call recursiveFloodFill() on the eastern neighbor:
        recursiveFloodFill(field, x + 1, y, newChar, curChar)
    if x - 1 >= 0 and field[(x - 1, y)] == curChar:
        # Call recursiveFloodFill() on the western neighbor:
        recursiveFloodFill(field, x - 1, y, newChar, curChar)


def iterativeFloodFill(field, startx, starty, newChar):
    curChar = field[(startx, starty)]

    coordinatesToChange = [(startx, starty)]

    while len(coordinatesToChange) > 0:
        x, y = coordinatesToChange.pop()
        field[(x, y)] = newChar # Change the character.

        # Change the neighboring characters:
        if y + 1 < HEIGHT and field[(x, y + 1)] == curChar:
            # Change the character for the southern neighbor:
            coordinatesToChange.append((x, y + 1))
        if y - 1 >= 0 and field[(x, y - 1)] == curChar:
            # Change the character for the northern neighbor:
            coordinatesToChange.append((x, y - 1))
        if x + 1 < WIDTH and field[(x + 1, y)] == curChar:
            # Change the character for the eastern neighbor:
            coordinatesToChange.append((x + 1, y))
        if x - 1 >= 0 and field[(x - 1, y)] == curChar:
            # Change the character for the western neighbor:
            coordinatesToChange.append((x - 1, y))


def printField(field):
    # Display the field data structure on the screen:

    # Display the x coordinates along the top:
    print('   ', end='')
    for i in range(WIDTH // 10):
        print(str(i) + NINE_SPACES, end='')
    print()
    print('   ' + ('0123456789' * 10)[:WIDTH])

    # Print the characters in the field:
    for y in range(HEIGHT):
        # Print each row, including the y coordinates on the left side:
        print(str(y).rjust(2) + ' ', end='')
        for x in range(WIDTH):
            # Print each character:
            print(field[(x, y)], end='')
        print() # Print a newline at the end of the row.


print('''FLOODFILL
By Al Sweigart al@inventwithpython.com

This demo shows the floodfill algorithm. Pick a point and a new
character to change TODO''') # TODO use inkspill's algorithm to make blotches

while True: # Main program loop.
    printField(field)
    print('Enter "[x] [y] [char]" (e.g. "3 3 #", no quotes) or QUIT to quit:')
    response = input()

    # Check if user wanted to quit:
    if response.upper() == 'QUIT':
        sys.exit()

    try:
        x, y, newChar = response.split()
    except:
        print('Invalid input. Enter something like "3 3 #" (without quotes).')
        continue

    # (!) Call either the recursive or iterative flood fill algorithms:
    # (They both do the same thing.)
    recursiveFloodFill(field, int(x), int(y), newChar)
    #iterativeFloodFill(field, int(x), int(y), newChar)

    # At this point, go back to the start of the main program loop.