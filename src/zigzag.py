# Zigzag, by Al Sweigart al@inventwithpython.com
# Shows a simple zig zag animation.

# Press Ctrl-C to stop the program.

import time
indent = 0 # How many spaces to indent.

while True: # The main program loop.
    # Zig to the right 20 times:
    for i in range(20):
        indent = indent + 1
        print(' ' * indent + '********')
        time.sleep(0.05) # Pause for 50 milliseconds.

    # Zag to the left 20 times:
    for i in range(20):
        indent = indent - 1
        print(' ' * indent + '********')
        time.sleep(0.05) # Pause for 50 milliseconds.
