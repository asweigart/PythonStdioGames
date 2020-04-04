"""Mondrian Art Generator, by Al Sweigart al@inventwithpython.com
Randomly generates art in the style of Piet Mondrian.
More info at: https://en.wikipedia.org/wiki/Piet_Mondrian
Tags: large, artistic"""
__version__ = 0
import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

# Setup the screen:
width, height = bext.size()
width -= 1  # TODO Windows bug
height -= 3

while True:  # Main application loop.
    # Pre-populate the board with blank spaces:
    board = {}
    for x in range(width):
        for y in range(height):
            board[(x, y)] = WHITE

    # Generate vertical lines:
    numberOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        numberOfSegmentsToDelete += 1
        for y in range(height):
            board[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    # Generate horizontal lines:
    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        numberOfSegmentsToDelete += 1
        for x in range(width):
            board[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    numberOfRectanglesToPaint = numberOfSegmentsToDelete - 3
    numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)

    # Randomly select points and try to remove them.
    for i in range(numberOfSegmentsToDelete):
        while True:  # Keep selecting segments to try to delete.
            # Get a random start point on an existing segment:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            if board[(startx, starty)] == WHITE:
                continue

            # Find out if we're on a vertical or horizontal segment:
            if board[(startx - 1, starty)] == board[(startx + 1, starty)] == WHITE:
                orientation = 'vertical'
            elif board[(startx, starty - 1)] == board[(startx, starty + 1)] == WHITE:
                orientation = 'horizontal'
            else:
                # The start point is on an intersection,
                # so get a new random start point:
                continue

            pointsToDelete = [(startx, starty)]

            canDeleteSegment = True
            if orientation == 'vertical':
                # Go up one path from the start point, and
                # see if we can remove this segment:
                for changey in (-1, 1):
                    y = starty
                    while 0 < y < height - 1:
                        y += changey
                        if board[(startx - 1, y)] == board[(startx + 1, y)] == BLACK:
                            # We've found a four-way intersection.
                            break
                        elif ((board[(startx - 1, y)] == WHITE and
                               board[(startx + 1, y)] == BLACK) or
                              (board[(startx - 1, y)] == BLACK and
                               board[(startx + 1, y)] == WHITE)):
                            # We've found a T-intersection; we can't
                            # delete this segment:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((startx, y))

            elif orientation == 'horizontal':
                # Go up one path from the start point, and
                # see if we can remove this segment:
                for changex in (-1, 1):
                    x = startx
                    while 0 < x < width - 1:
                        x += changex
                        if board[(x, starty - 1)] == board[(x, starty + 1)] == BLACK:
                            # We've found a four-way intersection.
                            break
                        elif ((board[(x, starty - 1)] == WHITE and
                               board[(x, starty + 1)] == BLACK) or
                              (board[(x, starty - 1)] == BLACK and
                               board[(x, starty + 1)] == WHITE)):
                            # We've found a T-intersection; we can't
                            # delete this segment:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((x, starty))
            if not canDeleteSegment:
                continue  # Get a new random start point.
            break  # Move on to delete the segment.

        # If we can delete this segment, set all the points to white:
        for x, y in pointsToDelete:
            board[(x, y)] = WHITE

    # Add the border lines:
    for x in range(width):
        board[(x, 0)] = BLACK  # Top border.
        board[(x, height - 1)] = BLACK  # Bottom border.
    for y in range(height):
        board[(0, y)] = BLACK  # Left border.
        board[(width - 1, y)] = BLACK  # Right border.

    # Paint the rectangles:
    for i in range(numberOfRectanglesToPaint):
        while True:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)

            if board[(startx, starty)] != WHITE:
                continue  # Get a new random start point.
            else:
                break

        # Flood fill algorithm:
        colorToPaint = random.choice([RED, YELLOW, BLUE, BLACK])
        pointsToPaint = set([(startx, starty)])
        while len(pointsToPaint) > 0:
            x, y = pointsToPaint.pop()
            board[(x, y)] = colorToPaint
            if board[(x - 1, y)] == WHITE:
                pointsToPaint.add((x - 1, y))
            if board[(x + 1, y)] == WHITE:
                pointsToPaint.add((x + 1, y))
            if board[(x, y - 1)] == WHITE:
                pointsToPaint.add((x, y - 1))
            if board[(x, y + 1)] == WHITE:
                pointsToPaint.add((x, y + 1))

    # Draw the board data structure:
    for y in range(height):
        for x in range(width):
            bext.bg(board[(x, y)])
            print(' ', end='')

        print()

    # Prompt user to create a new one:
    try:
        input('Press Enter for another work of art, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        sys.exit()
