"""Digital Clock, by Al Sweigart al@inventwithpython.com

Display a digital clock of the current time with a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires our sevseg.py program.
Tags: short"""
__version__ = 0

# This program MUST be run in a Terminal/Command Prompt window.

import time, os, sys
import sevseg  # Imports our sevseg.py program.


def main():
    """Run the digital clock program."""
    while True:  # Main program loop.
        # Clear the screen:
        if sys.platform == 'win32':
            os.system('cls')  # Clears Windows terminal.
        else:
            os.system('clear')  # Clears macOS/Linux terminal.

        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        # % 12 so we use a 12-hour clock, not 24:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'  # 12-hour clocks show 12:00, not 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Pad these strings with zeros, if needed:
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
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit.')

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
            # At this point, go back to the start of the loop.
        # At this point, go back to the start of the main program loop.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
