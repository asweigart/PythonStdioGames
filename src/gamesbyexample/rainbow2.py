"""Rainbow 2, by Al Sweigart al@inventwithpython.com
Shows a simple squiggle rainbow animation. Press Ctrl-C to stop.
This and other games are available at https://nostarch.com/XX
Tags: tiny, artistic, bext, beginner, scrolling"""
__version__ = 0
import time, random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
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
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
