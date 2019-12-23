# Bouncing Lines, by Al Sweigart al@inventwithpython.com
# A bouncing line animation. Press Ctrl-C to stop.
__version__ = 1

import sys, random, time

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can
install by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()


bext.clear()
WIDTH, HEIGHT = bext.size()
WIDTH -= 1 # Reduce width by 1 because of a weird Windows behavior.
NUMBER_OF_POINTS = 4
COLORS = ('red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white')
DIRECTIONS = ('upright', 'upleft', 'downright', 'downleft')
LINE_CHAR = '#'

def main():
    # Generate some points.
    points = []
    for i in range(NUMBER_OF_POINTS):
        points.append({'x': random.randint(1, WIDTH - 2),
                       'y': random.randint(1, HEIGHT - 2),
                       'direction': random.choice(DIRECTIONS)})

    while True: # Main program loop.
        oldpointPositions = []

        if random.randint(1, 50) == 1:
            bext.fg('random')

        for i, point in enumerate(points):
            # Draw our lines:
            if i == len(points) - 1:
                # The last point connects to the first point.
                pointA = point
                pointB = points[0]
            else:
                pointA = point
                pointB = points[i + 1]

            for x, y in line(pointA['x'], pointA['y'], pointB['x'], pointB['y']):
                bext.goto(x, y)
                print(LINE_CHAR, end='')

                oldpointPositions.append((x, y))
        sys.stdout.flush() # (Required for bext-using programs.)
        time.sleep(0.1)

        for point in points:
            # Move our points:
            if point['direction'] == 'upright':
                point['x'] += 1
                point['y'] -= 1
            elif point['direction'] == 'upleft':
                point['x'] -= 1
                point['y'] -= 1
            elif point['direction'] == 'downright':
                point['x'] += 1
                point['y'] += 1
            elif point['direction'] == 'downleft':
                point['x'] -= 1
                point['y'] += 1

            # See if our points bounce off the corners:
            if point['x'] == 0 and point['y'] == 0:
                point['direction'] = 'downright'
            elif point['x'] == 0 and point['y'] == HEIGHT - 1:
                point['direction'] = 'upright'
            elif point['x'] == WIDTH - 1 and point['y'] == 0:
                point['direction'] = 'downleft'
            elif point['x'] == WIDTH - 1 and point['y'] == HEIGHT - 1:
                point['direction'] = 'upleft'

            # See if our points bounce off the walls:
            elif point['x'] == 0 and point['direction'] == 'upleft':
                point['direction'] = 'upright'
            elif point['x'] == 0 and point['direction'] == 'downleft':
                point['direction'] = 'downright'

            elif point['x'] == WIDTH - 1 and point['direction'] == 'upright':
                point['direction'] = 'upleft'
            elif point['x'] == WIDTH - 1 and point['direction'] == 'downright':
                point['direction'] = 'downleft'

            elif point['y'] == 0 and point['direction'] == 'upleft':
                point['direction'] = 'downleft'
            elif point['y'] == 0 and point['direction'] == 'upright':
                point['direction'] = 'downright'

            elif point['y'] == HEIGHT - 1 and point['direction'] == 'downleft':
                point['direction'] = 'upleft'
            elif point['y'] == HEIGHT - 1 and point['direction'] == 'downright':
                point['direction'] = 'upright'

        for pos in oldpointPositions:
            # Erase all of the points.
            bext.goto(pos[0], pos[1])
            print(' ', end='')
        # At this point, go back to the start of the main program loop.


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
    main()
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.