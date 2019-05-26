import sys, random

random.seed(42)

# TODO - switch to dictionary for the main data structure

# Create the image (make sure it's rectangular!)
#im = [list('..................................................'),
#      list('....######################........................'),
#      list('....#....................#........................'),
#      list('....#....................#........................'),
#      list('....#....................#.......**************...'),
#      list('....#....................#.......*............*...'),
#      list('....#....................#.......*............*...'),
#      list('....#.......@@@@@@@@@@@@@@@@.....*............*...'),
#      list('....#.......@............#.@.....**************...'),
#      list('....########@#############.@......................'),
#      list('............@..............@.........++...........'),
#      list('............@..............@.........+.+..........'),
#      list('............@..............@.........+..+.........'),
#      list('............@..............@.........+...+........'),
#      list('............@@@@@@@@@@@@@@@@.........+....+.......'),
#      list('......................................+....+......'),
#      list('.......................................+...+......'),
#      list('........................................+..+......'),
#      list('.........................................+.+......'),
#      list('..........................................++......')]

#HEIGHT = len(im)
#WIDTH = len(im[0])

HEIGHT = 20
WIDTH = 50
im = []
for i in range(HEIGHT):
    im.append(list('.' * WIDTH))

# Create random rectangles:
for i in range(5):
    rectLeft = random.randint(0, WIDTH - 3)
    rectTop = random.randint(0, HEIGHT - 3)
    rectWidth = random.randint(3, WIDTH - rectLeft)
    rectHeight = random.randint(3, HEIGHT - rectTop)

    rectChar = random.choice('!@#*OX')
    for x in range(rectLeft, rectLeft + rectWidth):
        # Draw top line:
        im[rectTop][x] = rectChar
        # Draw bottom line:
        im[rectTop + rectHeight - 1][x] = rectChar

    for y in range(rectTop, rectTop + rectHeight):
        # Draw left line:
        im[y][rectLeft] = rectChar
        # Draw right line:
        im[y][rectLeft + rectWidth - 1] = rectChar


for row in im:
    assert len(row) == len(im[0]), 'Image is not rectangular!'

def recursiveFloodFill(image, x, y, newChar, oldChar=None):
    if oldChar == None:
        # If oldChar isn't passed, assume it's the character at x, y.
        oldChar = image[y][x]
    if oldChar == newChar or image[y][x] != oldChar:
        # BASE CASE
        return

    image[y][x] = newChar # Change the character.

    # Change the neighboring characters.
    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        # RECURSIVE CASE
        recursiveFloodFill(image, x, y + 1, newChar, oldChar)
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        # RECURSIVE CASE
        recursiveFloodFill(image, x, y - 1, newChar, oldChar)
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        # RECURSIVE CASE
        recursiveFloodFill(image, x + 1, y, newChar, oldChar)
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        # RECURSIVE CASE
        recursiveFloodFill(image, x - 1, y, newChar, oldChar)

def iterativeFloodFill(image, startx, starty, newChar):
    oldChar = image[starty][startx]

    coordinatesToChange = [(startx, starty)]

    while len(coordinatesToChange) > 0:
        x, y = coordinatesToChange.pop()

        image[y][x] = newChar # Change the character.

        # Change the neighboring characters.
        if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
            coordinatesToChange.append((x, y + 1))
        if y - 1 >= 0 and image[y - 1][x] == oldChar:
            coordinatesToChange.append((x, y - 1))
        if x + 1 < WIDTH and image[y][x + 1] == oldChar:
            coordinatesToChange.append((x + 1, y))
        if x - 1 >= 0 and image[y][x - 1] == oldChar:
            coordinatesToChange.append((x - 1, y))

def printImage(image):
    print('   ', end='')
    for i in range(WIDTH // 10):
        print(str(i) + '         ', end='')
    print()
    print('   ' + ('0123456789' * 10)[:WIDTH])

    for y in range(HEIGHT):
        # Print each row.
        print(str(y).rjust(2) + ' ', end='')
        for x in range(WIDTH):
            # Print each column.
            print(image[y][x], end='')
        print()
    print()

while True:
    printImage(im)
    # TODO - fix wording here and also add input validation
    print('Enter x coordinate, y coordinate, and new character separated by spaces (or Ctrl-C to quit):')
    try:
        x, y, newChar = input().split()
    except KeyboardInterrupt:
        sys.exit()

    recursiveFloodFill(im, int(x), int(y), newChar)
    #iterativeFloodFill(im, int(x), int(y), newChar)
