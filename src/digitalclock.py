# Digital Clock, by Al Sweigart al@inventwithpython.com
# More info at https://en.wikipedia.org/wiki/Seven-segment_display
# Requires our sevseg.py program.

import time, os, sys
import sevseg # Imports our sevseg.py program.

try:
    while True:
        # Clear the screen:
        if sys.platform == 'win32':
            os.system('cls') # Clears Windows terminal.
        else:
            os.system('clear') # Clears macOS/Linux terminal.

        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        h = str(currentTime.tm_hour % 12) # Use a 12-hour clock, not 24.
        if h == '0':
            h = '12' # 12-hour clocks show 12:00, not 00:00.
        m = str(currentTime.tm_min)
        s = str(currentTime.tm_sec)

        # Pad these strings with zeros, if needed:
        h = h.zfill(2)
        m = m.zfill(2)
        s = s.zfill(2)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(h)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(m)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(s)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1) # Insert a one-second pause.

except KeyboardInterrupt:
    pass
