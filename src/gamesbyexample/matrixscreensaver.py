"""Matrix Screensaver, by Al Sweigart al@inventwithpython.com

A "screensaver" in the style of The Matrix movie's "rain" visual."""
__version__ = 1

import random, shutil, sys, time

columns, rows = shutil.get_terminal_size()
columns -= 1 # Windows bug.

DENSITY = 20  # Range from 0 to 1000.
MIN_LENGTH = 6
MAX_LENGTH = 14

print('Matrix "Rain" Screensaver')
print('Press Ctrl-C to quit...')
time.sleep(3)

try:
    drips = [0] * columns
    while True:
        # setup drips
        for c in range(columns):
            if drips[c] == 0:
                if random.randint(1, 1000) <= DENSITY:
                    drips[c] = random.randint(MIN_LENGTH, MAX_LENGTH)

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
