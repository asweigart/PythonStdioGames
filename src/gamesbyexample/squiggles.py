"""Squiggles, by Al Sweigart al@inventwithpython.com
A program that draws a bunch of random squiggles.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic"""
__version__ = 0
import random

# Set up the constants:
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
UPDOWN    = chr(9474)  # Character 9474 is '│'
DOWNRIGHT = chr(9484)  # Character 9484 is '┌'
DOWNLEFT  = chr(9488)  # Character 9488 is '┐'
UPRIGHT   = chr(9492)  # Character 9492 is '└'
UPLEFT    = chr(9496)  # Character 9496 is '┘'
UP_DIRECTION    = 'up'
DOWN_DIRECTION  = 'down'
LEFT_DIRECTION  = 'left'
RIGHT_DIRECTION = 'right'

ALL_DIRECTIONS = [
    UP_DIRECTION,
    DOWN_DIRECTION,
    LEFT_DIRECTION,
    RIGHT_DIRECTION,
]

# (!) Try increasing the number of squiggles, or the size of the screen:
NUMBER_OF_SQUIGGLES = 15
WIDTH = 79
HEIGHT = 24

screen = {}
for i in range(NUMBER_OF_SQUIGGLES):
    # Find an unoccupied point on the screen to use as a starting space:
    foundStartingSpace = False

    # Pick a random point:
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    if (x, y) in screen:
        # This point is occupied, so try again.
        continue

    # Move once in a random direction:
    nextDirection = random.choice(ALL_DIRECTIONS)
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

    # Make sure the next space is not past the edge of the screen:
    if nextx == -1 or nextx == WIDTH:
        continue
    if nexty == -1 or nexty == HEIGHT:
        continue
    # Make sure the next space isn't already occupied:
    if (nextx, nexty) in screen:
        continue

    # Mark this first squiggle line character on the screen:
    screen[(x, y)] = squiggle
    foundStartingSpace = True

    if not foundStartingSpace:
        # If we can't find a valid random starting point (because the
        # screen is too full), quit.
        break

    # Draw the squiggle:
    while True:
        # This loop keeps drawing the squiggle line until it runs into
        # itself or the edge of the screen.
        direction = nextDirection

        # Update x and y based on the direction the squiggle is moving:
        if direction == UP_DIRECTION:
            y = y - 1
        elif direction == DOWN_DIRECTION:
            y = y + 1
        elif direction == LEFT_DIRECTION:
            x = x - 1
        elif direction == RIGHT_DIRECTION:
            x = x + 1

        # Get the possible direction the squiggle can go next:
        possibleNextDirections = []
        if (x, y - 1) not in screen and y - 1 != -1:
            possibleNextDirections.append(UP_DIRECTION)
        if (x, y + 1) not in screen and y + 1 != HEIGHT:
            possibleNextDirections.append(DOWN_DIRECTION)
        if (x - 1, y) not in screen and x - 1 != -1:
            possibleNextDirections.append(LEFT_DIRECTION)
        if (x + 1, y) not in screen and x + 1 != WIDTH:
            possibleNextDirections.append(RIGHT_DIRECTION)

        # The squiggle can't move without running into the edge of the
        # screen or another squiggle, so quit:
        if len(possibleNextDirections) == 0:
            break

        # Choose a random direction from the possible directions:
        nextDirection = random.choice(possibleNextDirections)

        # Decide on what line character to use based on the current
        # and next direction:
        if direction == RIGHT_DIRECTION:
            if nextDirection == RIGHT_DIRECTION:
                squiggle = LEFTRIGHT
            elif nextDirection == UP_DIRECTION:
                squiggle = UPLEFT
            elif nextDirection == DOWN_DIRECTION:
                squiggle = DOWNLEFT
        elif direction == LEFT_DIRECTION:
            if nextDirection == LEFT_DIRECTION:
                squiggle = LEFTRIGHT
            elif nextDirection == UP_DIRECTION:
                squiggle = UPRIGHT
            elif nextDirection == DOWN_DIRECTION:
                squiggle = DOWNRIGHT
        elif direction == UP_DIRECTION:
            if nextDirection == UP_DIRECTION:
                squiggle = UPDOWN
            elif nextDirection == LEFT_DIRECTION:
                squiggle = DOWNLEFT
            elif nextDirection == RIGHT_DIRECTION:
                squiggle = DOWNRIGHT
        elif direction == DOWN_DIRECTION:
            if nextDirection == DOWN_DIRECTION:
                squiggle = UPDOWN
            elif nextDirection == LEFT_DIRECTION:
                squiggle = UPLEFT
            elif nextDirection == RIGHT_DIRECTION:
                squiggle = UPRIGHT

        # Put this line character in the screen data structure:
        screen[(x, y)] = squiggle


# Print the screen data structure on the screen (if it's thinner than
# 100 characters):
if WIDTH <= 100:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(screen.get((x, y), ' '), end='')
        print()
else:
    print('Squiggles image is too wide to display on the screen.')


# Save the squiggle to a text file named squiggles.txt:
with open('squiggles.txt', 'w', encoding='utf-8') as file:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            file.write(screen.get((x, y), ' '))
        file.write('\n')
print('Saved to file squiggles.txt.')
