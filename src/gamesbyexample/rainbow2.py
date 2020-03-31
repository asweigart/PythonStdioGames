"""Rainbow 2, by Al Sweigart al@inventwithpython.com

Shows a simple squiggle rainbow animation. Press Ctrl-C to stop.
Tags: tiny, scrolling, artistic, bext"""
__version__ = 0
import time, random, sys

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

print('Rainbow 2, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 10  # How many spaces to indent.

try:
    while True:  # Main program loop.
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if random.randint(0, 1) == 0:
            # Increase the number of spaces:
            indent = indent + 1
            if indent > 60:
                indent = 60
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent < 0:
                indent = 0

        time.sleep(0.02)  # Add a slight pause.
        # At this point, go back to the start of the main program loop.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
