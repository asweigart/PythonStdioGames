"""Hole, by Al Sweigart al@inventwithpython.com
An animation of a hole that goes forever into the earth.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, scrolling, artistic"""

__version__ = 0
import random, time, sys

# Set up the constants:
WIDTH = 70
PAUSE_AMOUNT = 0.05

leftWidth = 20
gapWidth = 10

print('Hole, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

    # Adjust the left side width:
    r = random.randint(1, 4)
    if r == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1  # Decrease left side width.
    elif r == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1  # Increase left side width.
    else:
        pass  # Do nothing; no change in left side width.

    # (!) Try commenting out all of the following code:
    # Adjust the gap width:
    r = random.randint(1, 4)
    if r == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1  # Decrease gap width.
    elif r == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1  # Increase gap width.
    else:
        pass  # Do nothing; no change in gap width.
