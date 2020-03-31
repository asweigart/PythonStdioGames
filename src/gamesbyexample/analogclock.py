"""Analog Clock, by Al Sweigart al@inventwithpython.com

An analog clock animation. Press Ctrl-C to stop.
Tags: large, artistic, bext"""
__version__ = 0
import time, math, sys

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

# Set up the constants:
HOUR_HAND_CHAR = '@'
MINUTE_HAND_CHAR = '*'
SECOND_HAND_CHAR = '.'
HOUR_HAND_LENGTH = 4
MINUTE_HAND_LENGTH = 6
SECOND_HAND_LENGTH = 8
CENTERX, CENTERY = 10, 10
COMPLETE_ARC = 2 * math.pi
OFFSET_90_DEGREES = -0.5 * math.pi

CLOCKFACE = """       ##12###
     ##       ##
    11          1
   #             #
  #               #
 10                2
 #                  #
#                   #
#                   #
#                   #
9                   3
#                   #
#                   #
#                   #
 8                 4
 #                 #
  #               #
   #             #
    7           5
     ##       ##
       ###6###"""


def main():
    """Runs the Analog Clock program."""
    bext.clear()
    # Draw the circle of the clock:
    for y, row in enumerate(CLOCKFACE.splitlines()):
        for x, char in enumerate(row):
            if char != ' ':
                bext.goto(x, y)
                print(char)

    while True:  # Main program loop.
        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        h = currentTime.tm_hour % 12  # Use 12-hour clock, not 24.
        m = currentTime.tm_min
        s = currentTime.tm_sec

        # Draw the second hand:
        secHandDirection = COMPLETE_ARC * (s / 60) + OFFSET_90_DEGREES
        secHandXPos = math.cos(secHandDirection)
        secHandYPos = math.sin(secHandDirection)
        secHandX = int(secHandXPos * SECOND_HAND_LENGTH + CENTERX)
        secHandY = int(secHandYPos * SECOND_HAND_LENGTH + CENTERY)
        secHandPoints = line(CENTERX, CENTERY, secHandX, secHandY)
        for x, y in secHandPoints:
            bext.goto(x, y)
            print(SECOND_HAND_CHAR, end='')

        # Draw the minute hand:
        minHandDirection = COMPLETE_ARC * (m / 60) + OFFSET_90_DEGREES
        minHandXPos = math.cos(minHandDirection)
        minHandYPos = math.sin(minHandDirection)
        minHandX = int(minHandXPos * MINUTE_HAND_LENGTH + CENTERX)
        minHandY = int(minHandYPos * MINUTE_HAND_LENGTH + CENTERY)
        minHandPoints = line(CENTERX, CENTERY, minHandX, minHandY)
        for x, y in minHandPoints:
            bext.goto(x, y)
            print(MINUTE_HAND_CHAR, end='')

        # Draw the hour hand:
        hourHandDirection = COMPLETE_ARC * (h / 12) + OFFSET_90_DEGREES
        hourHandXPos = math.cos(hourHandDirection)
        hourHandYPos = math.sin(hourHandDirection)
        hourHandX = int(hourHandXPos * HOUR_HAND_LENGTH + CENTERX)
        hourHandY = int(hourHandYPos * HOUR_HAND_LENGTH + CENTERY)
        hourHandPoints = line(CENTERX, CENTERY, hourHandX, hourHandY)
        for x, y in hourHandPoints:
            bext.goto(x, y)
            print(HOUR_HAND_CHAR, end='')

        sys.stdout.flush()  # (Required for bext-using programs.)

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

        # Erase the clock hands:
        for x, y in secHandPoints:
            bext.goto(x, y)
            print(' ', end='')
        for x, y in minHandPoints:
            bext.goto(x, y)
            print(' ', end='')
        for x, y in hourHandPoints:
            bext.goto(x, y)
            print(' ', end='')
    # At this point, go back to the start of the main program loop.


def line(x1, y1, x2, y2):
    """Returns a list of points in a line between the given points.

    Uses the Bresenham line algorithm. More info at:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    points = []
    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    isReversed = x1 > x2

    if isReversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y2
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error <= 0:
                y -= ystep
                error += deltax
    else:
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if isSteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
    return points


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
