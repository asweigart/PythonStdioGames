# Maze Maker by Al Sweigart al@inventwithpython.com

import random

print('Maze Maker')
print()
while True:
    WIDTH = input('Enter width (must be odd and greater than 2): ')
    if WIDTH.isdecimal():
        WIDTH = int(WIDTH)
        if WIDTH % 2 == 1 and WIDTH > 2:
            break
while True:
    HEIGHT = input('Enter height (must be odd and greater than 2): ')
    if HEIGHT.isdecimal():
        HEIGHT = int(HEIGHT)
        if HEIGHT % 2 == 1 and HEIGHT > 2:
            break
while True:
    SEED = input('Enter seed (must be a positive integer): ')
    if SEED.isdecimal():
        SEED = int(SEED)
        if SEED >= 0:
            break

random.seed(SEED)

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

# Create the filled-in maze to start:
maze = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL

# Add the start and end positions:
maze[(1, 0)] = START
maze[(WIDTH - 2, HEIGHT - 1)] = EXIT

# Create the maze:
print('Generating maze...')
pathFromStart = [(1, 1)]
hasVisited = [(1, 1)]

while len(pathFromStart) > 0:
    x, y = pathFromStart[-1]
    maze[(x, y)] = EMPTY

    unvisitedNeighbors = []
    # Check the north neighbor:
    if y > 1 and (x, y - 2) not in hasVisited:
        unvisitedNeighbors.append(NORTH)
    # Check the south neighbor:
    if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
        unvisitedNeighbors.append(SOUTH)
    # Check the west neighbor:
    if x > 1 and (x - 2, y) not in hasVisited:
        unvisitedNeighbors.append(WEST)
    # Check the east neighbor:
    if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
        unvisitedNeighbors.append(EAST)

    if len(unvisitedNeighbors) > 0:
        nextIntersection = random.choice(unvisitedNeighbors)
        if nextIntersection == NORTH:
            pathFromStart.append((x, y - 2))
            hasVisited.append((x, y - 2))
            maze[(x, y - 1)] = EMPTY
        elif nextIntersection == SOUTH:
            pathFromStart.append((x, y + 2))
            hasVisited.append((x, y + 2))
            maze[(x, y + 1)] = EMPTY
        elif nextIntersection == WEST:
            pathFromStart.append((x - 2, y))
            hasVisited.append((x - 2, y))
            maze[(x - 1, y)] = EMPTY
        elif nextIntersection == EAST:
            pathFromStart.append((x + 2, y))
            hasVisited.append((x + 2, y))
            maze[(x + 1, y)] = EMPTY
    else:
        pathFromStart.pop()

# Display the maze and save it to a text file.
filename = 'maze%sx%ss%s.txt' % (WIDTH, HEIGHT, SEED)
mazeFile = open(filename, 'w')

for y in range(HEIGHT):
    for x in range(WIDTH):
        print(maze[(x, y)], end='')
        mazeFile.write(maze[(x, y)])
    print() # Print a newline after printing the row.
    mazeFile.write('\n')
mazeFile.close()

print('Saved to %s.' % (filename))
