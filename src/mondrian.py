# Mondrian Art Generator, by Al Sweigart al@inventwithpython.com
# Randomly generates Mondrian-style art to display on the terminal.

import logging
logging.basicConfig(filename='mondrian_log.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.debug('Start of program.')

import bext
import random

BLOCK = chr(9608) # Character 9608 is '█'

bext.clear()
width, height = bext.size()
width -= 1 # TODO Windows bug

# Generate horizontal and vertical lines.
col = 0
columns = [0]
while col < width - 5:
    col += random.randint(5, 10)
    columns.append(col)
columns.append(width - 1)

row = 0
rows = [0]
while row < height - 5:
    row += random.randint(3, 8)
    rows.append(row)
rows.append(height - 1)

# Create the line segments:
horizontalSegments = []
for y in rows:
    for i, x in enumerate(columns):
        if i == len(columns) - 1:
            continue
        horizontalSegments.append((x, y, columns[i + 1], y))

verticalSegments = []
for x in columns:
    for i, y in enumerate(rows):
        if i == len(rows) - 1:
            continue
        verticalSegments.append((x, y, x, rows[i + 1]))


# Delete segments randomly from the lines:
safeHorizontalSegments = set()
safeVerticalSegments = set()

logging.debug(len(horizontalSegments))
logging.debug(len(verticalSegments))
for j in range(int(width / 3)):
    while True:
        i = random.randint(0, len(horizontalSegments) - 1)
        segmentToDelete = horizontalSegments[i] # (x, y, x, y)
        #if segmentToDelete in safeVerticalSegments:
        #    continue
        x1, y, x2, _ = segmentToDelete
        aboveY = rows.index(y) - 1
        if aboveY != -1:
            safeVerticalSegments.add((x1, aboveY, x1, y))
            safeVerticalSegments.add((x2, aboveY, x2, y))
        belowY = rows.index(y) + 1
        if belowY != height:
            safeVerticalSegments.add((x1, y, x1, belowY))
            safeVerticalSegments.add((x2, y, x2, belowY))

        break
    del horizontalSegments[i]

    while False:
        i = random.randint(0, len(verticalSegments) - 1)
        segmentToDelete = verticalSegments[i] # (x, y, x, y)
        if segmentToDelete in safeVerticalSegments:
            continue
        x, y1, _, y2 = segmentToDelete
        leftX = rows.index(y) - 1
        #if leftX != -1:
        #    safeHorizontalSegments.add((x1, leftX, x1, y))
        #    safeHorizontalSegments.add((x2, leftX, x2, y))
        #rightX = rows.index(y) + 1
        #if rightX != height:
        #    safeHorizontalSegments.add((x1, y, x1, rightX))
        #    safeHorizontalSegments.add((x2, y, x2, rightX))
        break
    #del verticalSegments[i]

# Pre-populate the board with blank spaces:
board = {}
for x in range(width):
    for y in range(height):
        board[(x, y)] = 'w'


# Fill in the black lines:
for hSegment in horizontalSegments:
    y = hSegment[1]
    for x in range(hSegment[0], hSegment[2] + 1):
        board[(x, y)] = 'k'
        #logging.debug('h seg: ' + str((x,y)))

for vSegment in verticalSegments:
    x = vSegment[0]
    for y in range(vSegment[1], vSegment[3] + 1):
        board[(x, y)] = 'k'
        #logging.debug('v seg: ' + str((x,y)))


# Fill in random rectangles with red/yellow/blue colors:

for segment in safeVerticalSegments:
    x = segment[0]
    for y in range(segment[1], segment[3]):
        board[(x, y)] = 'g'


# Add the border lines:
for x in range(width):
    board[(x, 0)] = 'k'
    board[(x, width - 1)] = 'k'
for y in range(height):
    board[(0, y)] = 'k'
    board[(height - 1, y)] = 'k'





# Draw the board data structure:
for y in range(height):
    for x in range(width):
        if board[(x, y)] == 'w':
            bext.fg('white')
        elif board[(x, y)] == 'k':
            bext.fg('purple')
        elif board[(x, y)] == 'g':
            bext.fg('green')

        print(BLOCK, end='')
    print()

