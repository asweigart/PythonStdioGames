# Digital Clock, by Al Sweigart al@inventwithpython.com
# More info at https://en.wikipedia.org/wiki/Seven-segment_display

"""
A labeled seven-segment display:
 __A__
|     |
F     B
|__G__|
|     |
E     C
|__D__|

Each digit in a seven-segment display:
 __       __   __        __   __  __   __   __
|  |   |  __|  __| |__| |__  |__    | |__| |__|
|__|   | |__   __|    |  __| |__|   | |__|  __|

Our clock will look like this:
 __   __     __   __     __   __
|__| |__| * |__| |__| * |__| |__|
|__| |__| * |__| |__| * |__| |__|
h[0] h[1]   m[0] m[1]   s[0] s[1]
"""

# We store which segments each digit lights up:
SEGMENTS = {'0': 'ABCDEF',  '1': 'BC',    '2': 'ABDEG',  '3': 'ABCDG',
            '4': 'BCFG',    '5': 'ACDFG', '6': 'ACDEFG', '7': 'ABC',
            '8': 'ABCDEFG', '9': 'ABCDFG'}

# Setup some segment constants:
H_FILLED = '__'
H_EMPTY  = '  '
V_FILLED = '|'
V_EMPTY  = ' '

import time, os, sys

try:
    while True:
        # Clear the previously drawn text:
        if sys.platform == 'win32':
            os.system('cls') # Clears Windows terminal.
        else:
            os.system('clear') # Clears macOS/Linux terminal.

        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        h = str(currentTime.tm_hour % 12) # Use 12-hour clock, not 24.
        m = str(currentTime.tm_min)
        s = str(currentTime.tm_sec)

        # Pad these strings with zeros, if needed:
        h = h.zfill(2)
        m = m.zfill(2)
        s = s.zfill(2)

        # Figure out the A segment display:
        print(' ', end='')
        print(H_FILLED if 'A' in SEGMENTS[h[0]] else H_EMPTY, end='')
        print('   ', end='')
        print(H_FILLED if 'A' in SEGMENTS[h[1]] else H_EMPTY, end='')
        print('     ', end='')
        print(H_FILLED if 'A' in SEGMENTS[m[0]] else H_EMPTY, end='')
        print('   ', end='')
        print(H_FILLED if 'A' in SEGMENTS[m[1]] else H_EMPTY, end='')
        print('     ', end='')
        print(H_FILLED if 'A' in SEGMENTS[s[0]] else H_EMPTY, end='')
        print('   ', end='')
        print(H_FILLED if 'A' in SEGMENTS[s[1]] else H_EMPTY, end='')
        print() # Print a newline.

        # Figure out the FGB segment displays:
        print(V_FILLED if 'F' in SEGMENTS[h[0]] else V_EMPTY, end='')
        print(H_FILLED if 'G' in SEGMENTS[h[0]] else H_EMPTY, end='')
        print(V_FILLED if 'B' in SEGMENTS[h[0]] else V_EMPTY, end='')
        print(' ', end='')
        print(V_FILLED if 'F' in SEGMENTS[h[1]] else V_EMPTY, end='')
        print(H_FILLED if 'G' in SEGMENTS[h[1]] else H_EMPTY, end='')
        print(V_FILLED if 'B' in SEGMENTS[h[1]] else V_EMPTY, end='')
        print(' * ', end='')
        print(V_FILLED if 'F' in SEGMENTS[m[0]] else V_EMPTY, end='')
        print(H_FILLED if 'G' in SEGMENTS[m[0]] else H_EMPTY, end='')
        print(V_FILLED if 'B' in SEGMENTS[m[0]] else V_EMPTY, end='')
        print(' ', end='')
        print(V_FILLED if 'F' in SEGMENTS[m[1]] else V_EMPTY, end='')
        print(H_FILLED if 'G' in SEGMENTS[m[1]] else H_EMPTY, end='')
        print(V_FILLED if 'B' in SEGMENTS[m[1]] else V_EMPTY, end='')
        print(' * ', end='')
        print(V_FILLED if 'F' in SEGMENTS[s[0]] else V_EMPTY, end='')
        print(H_FILLED if 'G' in SEGMENTS[s[0]] else H_EMPTY, end='')
        print(V_FILLED if 'B' in SEGMENTS[s[0]] else V_EMPTY, end='')
        print(' ', end='')
        print(V_FILLED if 'F' in SEGMENTS[s[1]] else V_EMPTY, end='')
        print(H_FILLED if 'G' in SEGMENTS[s[1]] else H_EMPTY, end='')
        print(V_FILLED if 'B' in SEGMENTS[s[1]] else V_EMPTY, end='')
        print() # Print a newline.

        # Figure out the EDC segment displays:
        print(V_FILLED if 'E' in SEGMENTS[h[0]] else V_EMPTY, end='')
        print(H_FILLED if 'D' in SEGMENTS[h[0]] else H_EMPTY, end='')
        print(V_FILLED if 'C' in SEGMENTS[h[0]] else V_EMPTY, end='')
        print(' ', end='')
        print(V_FILLED if 'E' in SEGMENTS[h[1]] else V_EMPTY, end='')
        print(H_FILLED if 'D' in SEGMENTS[h[1]] else H_EMPTY, end='')
        print(V_FILLED if 'C' in SEGMENTS[h[1]] else V_EMPTY, end='')
        print(' * ', end='')
        print(V_FILLED if 'E' in SEGMENTS[m[0]] else V_EMPTY, end='')
        print(H_FILLED if 'D' in SEGMENTS[m[0]] else H_EMPTY, end='')
        print(V_FILLED if 'C' in SEGMENTS[m[0]] else V_EMPTY, end='')
        print(' ', end='')
        print(V_FILLED if 'E' in SEGMENTS[m[1]] else V_EMPTY, end='')
        print(H_FILLED if 'D' in SEGMENTS[m[1]] else H_EMPTY, end='')
        print(V_FILLED if 'C' in SEGMENTS[m[1]] else V_EMPTY, end='')
        print(' * ', end='')
        print(V_FILLED if 'E' in SEGMENTS[s[0]] else V_EMPTY, end='')
        print(H_FILLED if 'D' in SEGMENTS[s[0]] else H_EMPTY, end='')
        print(V_FILLED if 'C' in SEGMENTS[s[0]] else V_EMPTY, end='')
        print(' ', end='')
        print(V_FILLED if 'E' in SEGMENTS[s[1]] else V_EMPTY, end='')
        print(H_FILLED if 'D' in SEGMENTS[s[1]] else H_EMPTY, end='')
        print(V_FILLED if 'C' in SEGMENTS[s[1]] else V_EMPTY, end='')
        print() # Print a newline.

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1) # Insert a one-second pause.

except KeyboardInterrupt:
    pass
