# Zigzag, by Al Sweigart al@inventwithpython.com
# A simple zig zag animation. Press Ctrl-C to stop.
__version__ = 1

import time, sys
indentSize = 0 # How many spaces to indent.

try:
    while True: # The main program loop.
        # Zig to the right 20 times:
        for i in range(20):
            indentSize = indentSize + 1
            indentation = ' ' * indentSize
            print(' ' * indentSize + '********')
            time.sleep(0.05) # Pause for 50 milliseconds.

        # Zag to the left 20 times:
        for i in range(20):
            indentSize = indentSize - 1
            indentation = ' ' * indentSize
            print(indentation + '********')
            time.sleep(0.05) # Pause for 50 milliseconds.
    # At this point, go back to the start of the main program loop.
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.