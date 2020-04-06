"""Dice Math, by Al Sweigart al@inventwithpython.com
A flash card addition game where you sum the total on random dice rolls.
Tags: large, game, math"""
__version__ = 0

import random, time

# Set up the constants:
DICE_WIDTH = 9
DICE_HEIGHT = 5
SCREEN_WIDTH = 79
SCREEN_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom.

# The duration is in seconds:
QUIZ_DURATION = 30  # (!) Try changing this to 10 or 60.
MIN_DICE = 2  # (!) Try changing this to 1 or 5.
MAX_DICE = 5  # (!) Try changing this to 14.

# The program hangs if all of the dice can't fit on the screen:
assert MAX_DICE <= 14

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

print('''Dice Math, by Al Sweigart al@inventwithpython.com

Add up the sums of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get 3 points for each
correct answer and lose 1 point for each incorrect answer.
'''.format(QUIZ_DURATION))
input('Press Enter to begin...')

# Keep track of how many dice rolls were added correctly and incorrectly:
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

    # Contains (x, y) tuples of the top-left corner of each die.
    topLeftDiceCorners = []

    # Figure out where dice should go:
    for i in range(len(diceFaces)):
        while True:
            # Find a random place on the canvas to put the die:
            x = random.randint(0, SCREEN_WIDTH - 1 - DICE_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - 1 - DICE_HEIGHT)

            # Check if this die overlaps with previous dice.
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

                # Check each corner of this die to see if it is inside
                # of the area the previous die:
                for cornerx, cornery in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDie[0] <= cornerx and
                        cornerx < (prevDie[0] + DICE_WIDTH) and
                        prevDie[1] <= cornery and
                        cornery < (prevDie[1] + DICE_HEIGHT)):
                            overlaps = True
            if not overlaps:
                # It doesn't overlap, so we can put it here:
                topLeftDiceCorners.append((x, y))
                break

    # Draw the dice on the canvas:

    # Keys are (x, y) tuples of ints, values the character at that
    # position on the canvas:
    canvas = {}
    # Loop over each die:
    for i, dieCorner in enumerate(topLeftDiceCorners):
        # Loop over each character in the die's face:
        dieFace = diceFaces[i]
        for ix in range(DICE_WIDTH):
            for iy in range(DICE_HEIGHT):
                # Copy this character to the correct place on the canvas:
                canvasX = dieCorner[0] + ix
                canvasY = dieCorner[1] + iy
                canvas[(canvasX, canvasY)] = dieFace[iy][ix]

    # Display the canvas on the screen:
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            print(canvas.get((x, y), ' '), end='')
        print()  # Print a newline.

    # Let the player enter their answer:
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        incorrectAnswers += 1

# Display the final score:
print('Correct:  ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score:    ', (correctAnswers * 3) - incorrectAnswers)
