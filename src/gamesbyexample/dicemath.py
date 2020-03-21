"""Dice Math, by Al Sweigart al@inventwithpython.com

TODO"""

# TODO - this program needs more polish and refactoring.

import random, time

# Set up the constants:
QUIZ_DURATION = 30 # 30 seconds
DICE_WIDTH = 9
DICE_HEIGHT = 5
SCREEN_WIDTH = 79
SCREEN_HEIGHT = 24
MIN_DICE = 2
MAX_DICE = 5

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print("""Dice Math, by Al Sweigart al@inventwithpython.com

TODO blah blah 30 seconds """)

correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:  # Main game loop.
    # Come up with the dice to display:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        diceFaces.append(die[0])
        sumAnswer += die[1]

    # Place dice on canvas:
    topLeftDiceCorners = []
    for i in range(len(diceFaces)):
        while True:  # Keep looping until we find a non-overlapping place for the die.
            x = random.randint(0, SCREEN_WIDTH - 1 - DICE_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - 1 - DICE_HEIGHT - 3) # -3 so we have room to enter the sum

            overlaps = False
            for prevDie in topLeftDiceCorners:
                topLeftX = x
                topLeftY = y
                topRightX = x + DICE_WIDTH
                topRightY = y
                bottomLeftX = x
                bottomLeftY = y + DICE_HEIGHT
                bottomRightX = x + DICE_WIDTH
                bottomRightY = y + DICE_HEIGHT

                for cornerx, cornery in ((topLeftX, topLeftY), (topRightX, topRightY), (bottomLeftX, bottomLeftY), (bottomRightX, bottomRightY)):
                    if (prevDie[0] <= cornerx < (prevDie[0] + DICE_WIDTH)) and (prevDie[1] <= cornery < (prevDie[1] + DICE_HEIGHT)):
                        overlaps = True
            if not overlaps:
                break
        topLeftDiceCorners.append((x, y))

    # Draw on canvas:
    canvas = {}  # Keys are (x, y) tuples of ints, values are one-char strings.
    for i, dieCorner in enumerate(topLeftDiceCorners):
        for ix in range(DICE_WIDTH):
            for iy in range(DICE_HEIGHT):
                # TODO add comment explaining this:
                canvas[(dieCorner[0] + ix, dieCorner[1] + iy)] = diceFaces[i][iy][ix]

    # Display canvas on the screen:
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            print(canvas.get((x, y), ' '), end='')
        print()  # Print a newline.

    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1

print('Correct:  ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score:    ', (correctAnswers * 3) - incorrectAnswers)
