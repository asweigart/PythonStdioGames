# Zigzag, by Al Sweigart al@inventwithpython.com
# A simple zig zag animation.
__version__ = 1

# Press Ctrl-C to stop the program.

import time
indentSize = 0 # How many spaces to indent.

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
