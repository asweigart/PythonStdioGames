"""Diamond, by Al Sweigart al@inventwithpython.com

Draws diamonds of various sizes."""
__version__ = 1

# Setup the constants:
LEFTRIGHT = chr(9472) # Character 9472 is '─'
UPDOWN    = chr(9474) # Character 9474 is '│'
DOWNRIGHT = chr(9484) # Character 9484 is '┌'
DOWNLEFT  = chr(9488) # Character 9488 is '┐'
UPRIGHT   = chr(9492) # Character 9492 is '└'
UPLEFT    = chr(9496) # Character 9496 is '┘'
UP_DIRECTION    = 'up'
DOWN_DIRECTION  = 'down'
LEFT_DIRECTION  = 'left'
RIGHT_DIRECTION = 'right'

import random

WIDTH = 79
HEIGHT = 24

grid = {}

while True:
    # get starting space
    foundStartingSpace = False
    for i in range(1000):
        #breakpoint()
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        if (x, y) in grid:
            continue

        nextDirection = random.choice([UP_DIRECTION, DOWN_DIRECTION, LEFT_DIRECTION, RIGHT_DIRECTION])
        nextx = x
        nexty = y
        if nextDirection == UP_DIRECTION:
            squiggle = random.choice([UPDOWN, UPLEFT, UPRIGHT])
            nexty -= 1
        elif nextDirection == DOWN_DIRECTION:
            squiggle = random.choice([UPDOWN, DOWNLEFT, DOWNRIGHT])
            nexty += 1
        elif nextDirection == LEFT_DIRECTION:
            squiggle = random.choice([LEFTRIGHT, UPLEFT, DOWNLEFT])
            nextx -= 1
        elif nextDirection == RIGHT_DIRECTION:
            squiggle = random.choice([LEFTRIGHT, UPRIGHT, DOWNRIGHT])
            nextx += 1

        if nextx == -1 or nextx == WIDTH or nexty == -1 or nexty == HEIGHT or (nextx, nexty) in grid:
            continue

        grid[(x, y)] = squiggle
        foundStartingSpace = True
        break

    if not foundStartingSpace:
        break

    # fill in grid
    while True:
        direction = nextDirection

        # update x and y based on direction
        if direction == UP_DIRECTION:
            y = y - 1
        elif direction == DOWN_DIRECTION:
            y = y + 1
        elif direction == LEFT_DIRECTION:
            x = x - 1
        elif direction == RIGHT_DIRECTION:
            x = x + 1

        # get possible new direction
        possibleNextDirections = []
        if (x, y - 1) not in grid and y - 1 != -1:
            possibleNextDirections.append(UP_DIRECTION)
        if (x, y + 1) not in grid and y + 1 != HEIGHT:
            possibleNextDirections.append(DOWN_DIRECTION)
        if (x - 1, y) not in grid and x - 1 != -1:
            possibleNextDirections.append(LEFT_DIRECTION)
        if (x + 1, y) not in grid and x + 1 != WIDTH:
            possibleNextDirections.append(RIGHT_DIRECTION)

        if len(possibleNextDirections) == 0:
            break

        nextDirection = random.choice(possibleNextDirections)

        if direction == RIGHT_DIRECTION:
            if nextDirection == RIGHT_DIRECTION:
                squiggle = LEFTRIGHT
            elif nextDirection == UP_DIRECTION:
                squiggle = UPLEFT
            elif nextDirection == DOWN_DIRECTION:
                squiggle = DOWNLEFT
        if direction == LEFT_DIRECTION:
            if nextDirection == LEFT_DIRECTION:
                squiggle = LEFTRIGHT
            elif nextDirection == UP_DIRECTION:
                squiggle = UPRIGHT
            elif nextDirection == DOWN_DIRECTION:
                squiggle = DOWNRIGHT
        if direction == UP_DIRECTION:
            if nextDirection == UP_DIRECTION:
                squiggle = UPDOWN
            elif nextDirection == LEFT_DIRECTION:
                squiggle = DOWNLEFT
            elif nextDirection == RIGHT_DIRECTION:
                squiggle = DOWNRIGHT
        if direction == DOWN_DIRECTION:
            if nextDirection == DOWN_DIRECTION:
                squiggle = UPDOWN
            elif nextDirection == LEFT_DIRECTION:
                squiggle = UPLEFT
            elif nextDirection == RIGHT_DIRECTION:
                squiggle = UPRIGHT

        # mark the space
        grid[(x, y)] = squiggle


# display the grid
for yy in range(HEIGHT):
    for xx in range(WIDTH):
        print(grid.get((xx, yy), ' '), end='')
    print()

