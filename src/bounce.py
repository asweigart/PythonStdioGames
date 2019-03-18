# A bouncing ball animation, by Al Sweigart al@inventwithpython.com

import bext, random, time, sys
assert sys.version_info.major == 3, 'Run this program on Python 3.'

bext.clear()
WIDTH, HEIGHT = bext.size()
WIDTH -= 1 # TODO Weird Windows bug.
NUMBER_OF_BALLS = 35
COLORS = ('red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white')
DIRECTIONS = ('upright', 'upleft', 'downright', 'downleft')
BALL_CHAR = 'O'

# Generate some balls.
balls = []
for i in range(NUMBER_OF_BALLS):
    balls.append({'color': random.choice(COLORS),
                  'x': random.randint(1, WIDTH - 2),
                  'y': random.randint(1, HEIGHT - 2),
                  'direction': random.choice(DIRECTIONS)})

while True: # Main game loop.
    oldBallPositions = []

    for ball in balls:
        # Draw our balls:
        bext.goto(ball['x'], ball['y'])
        bext.fg(ball['color'])
        print(BALL_CHAR, end='')

        oldBallPositions.append((ball['x'], ball['y']))
    time.sleep(0.1)

    for ball in balls:
        # Move our balls:
        if ball['direction'] == 'upright':
            ball['x'] += 1
            ball['y'] -= 1
        elif ball['direction'] == 'upleft':
            ball['x'] -= 1
            ball['y'] -= 1
        elif ball['direction'] == 'downright':
            ball['x'] += 1
            ball['y'] += 1
        elif ball['direction'] == 'downleft':
            ball['x'] -= 1
            ball['y'] += 1

        # See if our balls bounce off the corners:
        if ball['x'] == 0 and ball['y'] == 0:
            ball['direction'] = 'downright'
        elif ball['x'] == 0 and ball['y'] == HEIGHT - 1:
            ball['direction'] = 'upright'
        elif ball['x'] == WIDTH - 1 and ball['y'] == 0:
            ball['direction'] = 'downleft'
        elif ball['x'] == WIDTH - 1 and ball['y'] == HEIGHT - 1:
            ball['direction'] = 'upleft'

        # See if our balls bounce off the walls:
        elif ball['x'] == 0 and ball['direction'] == 'upleft':
            ball['direction'] = 'upright'
        elif ball['x'] == 0 and ball['direction'] == 'downleft':
            ball['direction'] = 'downright'

        elif ball['x'] == WIDTH - 1 and ball['direction'] == 'upright':
            ball['direction'] = 'upleft'
        elif ball['x'] == WIDTH - 1 and ball['direction'] == 'downright':
            ball['direction'] = 'downleft'

        elif ball['y'] == 0 and ball['direction'] == 'upleft':
            ball['direction'] = 'downleft'
        elif ball['y'] == 0 and ball['direction'] == 'upright':
            ball['direction'] = 'downright'

        elif ball['y'] == HEIGHT - 1 and ball['direction'] == 'downleft':
            ball['direction'] = 'upleft'
        elif ball['y'] == HEIGHT - 1 and ball['direction'] == 'downright':
            ball['direction'] = 'upright'

    for pos in oldBallPositions:
        # Erase all of the balls.
        bext.goto(pos[0], pos[1])
        print(' ', end='')
