"""Tunnel Animation, by Al Sweigart al@inventwithpython.com

A tunnel animation."""

__version__ = 1
import random, time

# Set up the constants:
WIDTH = 70
PAUSE_AMOUNT = 0.05

leftWidth = 20
gapWidth = 6

print('Tunnel Animation, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    time.sleep(PAUSE_AMOUNT)

    # Adjust the left side width:
    r = random.randint(1, 4)
    if r == 1 and leftWidth > 1:
        # Decrease left side width:
        leftWidth = leftWidth - 1
    elif r == 2 and leftWidth + gapWidth < WIDTH - 1:
        # Increase left side width:
        leftWidth = leftWidth + 1
    else:
        # Do nothing; no change in left side width.
        pass

    # Adjust the gap width:
    r = random.randint(1, 4)
    if r == 1 and gapWidth > 1:
        # Decrease gap width:
        gapWidth = gapWidth - 1
    elif r == 2 and leftWidth + gapWidth < WIDTH - 1:
        # Increase gap width:
        gapWidth = gapWidth + 1
    else:
        # Do nothing; no change in gap width.
        pass
