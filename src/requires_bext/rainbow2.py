# Rainbow 2, by Al Sweigart al@inventwithpython.com
# Shows a simple squiggle rainbow animation.

"""
This program requires the bext module, which you can install by opening
a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python3 -m pip install --user bext
"""

import time, random, sys
assert sys.version_info.major == 3, 'Run this program on Python 3.'

try:
    import bext
except:
    sys.exit('Bext is required to run this. Run `pip install bext` from the shell to install it.')

indent = 10 # How many spaces to indent.


while True:
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
        if indent > 20:
            indent = 20
    else:
        # Decrease the number of spaces:
        indent = indent - 1
        if indent < 0:
            indent = 0

    time.sleep(0.05) # Add a slight pause.
