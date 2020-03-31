"""Countdown, by Al Sweigart al@inventwithpython.com

Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires our sevseg.py program.
Tags: short"""
__version__ = 0
# This program MUST be run in a Terminal/Command Prompt window.

import time, os, sys
import sevseg  # Imports our sevseg.py program.

if len(sys.argv) > 1:
    secondsLeft = int(sys.argv[1])
else:
    secondsLeft = 300  # Change this to whatever value you like.

if secondsLeft > 359999:
    # secondsLeft can't be 100 hours or more:
    secondsLeft = 359999

try:
    while True:  # Main game loop.
        # Clear the screen:
        if sys.platform == 'win32':
            os.system('cls')  # Clears Windows terminal.
        else:
            os.system('clear')  # Clears macOS/Linux terminal.

        # Get the hours/minutes/seconds from secondsLeft:
        # For example: 7265 is 2 hours, 1 minute, 5 seconds.
        # So 7265 // 3600 is 2 hours:
        hours = str(secondsLeft // 3600)
        # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
        minutes = str((secondsLeft % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds = str(secondsLeft % 60)

        # Pad these strings to two digits with zeros, if needed:
        hours = hours.zfill(2)
        minutes = minutes.zfill(2)
        seconds = seconds.zfill(2)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()  # Print a newline.

        if secondsLeft == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.

        secondsLeft -= 1
        # At this point, go back to the start of the main program loop.

except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.)
