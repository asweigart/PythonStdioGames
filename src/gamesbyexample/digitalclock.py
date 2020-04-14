"""Digital Clock, by Al Sweigart al@inventwithpython.com
Displays a digital clock of the current time with a seven-segment
display. Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This and other games are available at https://nostarch.com/XX
Tags: short, artistic"""
__version__ = 0
# This program MUST be run in a Terminal/Command Prompt window.

import sys, time
import sevseg  # Imports our sevseg.py program.


def main():
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

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


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Digital Clock, by Al Sweigart al@inventwithpython.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.
