# Analog Clock, by Al Sweigart al@inventwithpython.com

import time, math, bext

HOURS_RADIUS = 4
MINUTES_RADIUS = 6
SECONDS_RADIUS = 8
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


def line(x1, y1, x2, y2):
    """Returns a list of  all of the points in a line
    between `x1`, `y1` and `x2`, `y2`. Uses the Bresenham line algorithm.
    More info at https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    points = []
    isSteep = abs(y2-y1) > abs(x2-x1)
    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    isReversed = x1 > x2

    if isReversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

        deltax = x2 - x1
        deltay = abs(y2-y1)
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
        deltay = abs(y2-y1)
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

try:
    bext.clear()
    while True: # Main program loop.


        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        h = currentTime.tm_hour % 12 # Use 12-hour clock, not 24.
        m = currentTime.tm_min
        s = currentTime.tm_sec

        # Draw the circle of the clock:
        for y, row in enumerate(CLOCKFACE.splitlines()):
            for x, char in enumerate(row):
                if char != ' ':
                    bext.goto(x, y)
                    print(char)

        # Draw the second hand:
        secondHandX = int(math.cos(COMPLETE_ARC * (s / 60) + OFFSET_90_DEGREES) * SECONDS_RADIUS + CENTERX)
        secondHandY = int(math.sin(COMPLETE_ARC * (s / 60) + OFFSET_90_DEGREES) * SECONDS_RADIUS + CENTERY)
        secondHandPoints = line(CENTERX, CENTERY, secondHandX, secondHandY)
        for x, y in secondHandPoints:
            bext.goto(x, y)
            print('.', end='')

        # Draw the minute hand:
        minuteHandX = int(math.cos(COMPLETE_ARC * (m / 60) + OFFSET_90_DEGREES) * MINUTES_RADIUS + CENTERX)
        minuteHandY = int(math.sin(COMPLETE_ARC * (m / 60) + OFFSET_90_DEGREES) * MINUTES_RADIUS + CENTERY)
        minuteHandPoints = line(CENTERX, CENTERY, minuteHandX, minuteHandY)
        for x, y in minuteHandPoints:
            bext.goto(x, y)
            print('*', end='')

        # Draw the hour hand:
        hourHandX = int(math.cos(COMPLETE_ARC * (h / 12) + OFFSET_90_DEGREES) * HOURS_RADIUS + CENTERX)
        hourHandY = int(math.sin(COMPLETE_ARC * (h / 12) + OFFSET_90_DEGREES) * HOURS_RADIUS + CENTERY)
        hourHandPoints = line(CENTERX, CENTERY, hourHandX, hourHandY)
        for x, y in hourHandPoints:
            bext.goto(x, y)
            print('@', end='')

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

        # Erase the clock hands:
        for x, y in secondHandPoints:
            bext.goto(x, y)
            print(' ', end='')
        for x, y in minuteHandPoints:
            bext.goto(x, y)
            print(' ', end='')
        for x, y in hourHandPoints:
            bext.goto(x, y)
            print(' ', end='')
except KeyboardInterrupt:
    pass

