"""Matrix Screensaver, by Al Sweigart al@inventwithpython.com

A "screensaver" in the style of The Matrix movie's "digital rain bead"
visual."""
__version__ = 1

import random, shutil, sys, time

# Set up the constants:
DENSITY = 20  # Density can range from 0 to 1000.
MIN_BEAD_LENGTH = 6
MAX_BEAD_LENGTH = 14

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Matrix "Rain" Screensaver')
print('Press Ctrl-C to quit...')
time.sleep(3)

try:
    drips = [0] * WIDTH
    while True:
        # setup drips
        for c in range(WIDTH):
            if drips[c] == 0:
                if random.randint(1, 1000) <= DENSITY:
                    drips[c] = random.randint(MIN_BEAD_LENGTH, MAX_BEAD_LENGTH)

            if drips[c] != 0:
                print(random.randint(0, 1), end='')
                drips[c] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
