"""Matrix Screensaver, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's "digital rain"
visual.
Tags: tiny, beginner, scrolling, artistic"""
__version__ = 0
import random, shutil, sys, time

# Set up the constants:
DENSITY = 2.0  # Density can range from 0.0 to 100.0.
MIN_BEAD_LENGTH = 6
MAX_BEAD_LENGTH = 14
PAUSE = 0.1

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Matrix Screensaver, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(3)

try:
    # When the counter is 0, no bead of "digital rain" is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Set up the counter for each column:
        for i in range(WIDTH):
            if columns[i] == 0:
                if (random.randint(1, 10000) / 100) <= DENSITY:
                    # Restart the bead on this column.
                    columns[i] = random.randint(MIN_BEAD_LENGTH,
                                                MAX_BEAD_LENGTH)

            if columns[i] != 0:
                print(random.randint(0, 1), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
