# Langton's Ant, by Al Sweigart al@inventwithpython.com
# More info: https://en.wikipedia.org/wiki/Langton%27s_ant

import random, time, copy
import bext

WIDTH = 79
HEIGHT = 44

NUMBER_OF_ANTS = 8
DISPLAY_AFTER_STEPS = 5
ANT_COLOR = 'red'
FILLED_COLOR = 'reset'
EMPTY_COLOR = 'black'
PAUSE_LENGTH = 0.0

# TODO
if HEIGHT % 2 == 1:
    HEIGHT -= 1

# Create a new board data structure:
board = {'width': WIDTH, 'height': HEIGHT}

# Create ant data structures:
ants = []
for i in range(NUMBER_OF_ANTS):
    ant = {'x': random.randint(0, WIDTH - 1),
           'y': random.randint(0, HEIGHT - 1),
           'direction': random.choice(['N', 'S', 'E', 'W'])}
    ants.append(ant)


# Clear the previously drawn text:
bext.fg(FILLED_COLOR)
bext.bg(EMPTY_COLOR)
bext.clear()

step = 0
try:
    while len(ants) > 0: # Keep running the simulation as long as we have ants.
        # Draw the board data structure.
        if step % DISPLAY_AFTER_STEPS == 0:
            bext.goto(0, 0)
            for y in range(0, board['height'], 2):
                for x in range(board['width']):
                    top = board.get((x, y), False)
                    bottom = board.get((x, y + 1), False)

                    antTop = False
                    antBottom = False
                    for ant in ants:
                        if ant['x'] == x and ant['y'] == y:
                            antTop = True
                        if ant['x'] == x and ant['y'] + 1 == y + 1:
                            antBottom = True

                    if antTop or antBottom:
                        bext.fg(ANT_COLOR)
                        print(chr(9608), end='') # Fill in both halves.
                        bext.fg(FILLED_COLOR)
                        continue

                    if top and bottom:
                        print(chr(9608), end='') # Fill in both halves.
                    elif top and not bottom:
                        print(chr(9600), end='') # Fill in top half.
                    elif not top and bottom:
                        print(chr(9604), end='') # Fill in bottom half.
                    elif not top and not bottom:
                        print(' ', end='') # Fill in nothing.
                print()
            print('Press Ctrl-C to quit.')


        # Run a single simulation step:
        nextBoard = copy.copy(board)

        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                # Turn clockwise:
                if ant['direction'] == 'N':
                    ant['direction'] = 'E'
                elif ant['direction'] == 'E':
                    ant['direction'] = 'S'
                elif ant['direction'] == 'S':
                    ant['direction'] = 'W'
                elif ant['direction'] == 'W':
                    ant['direction'] = 'N'
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                # Turn counter clockwise:
                if ant['direction'] == 'N':
                    ant['direction'] = 'W'
                elif ant['direction'] == 'W':
                    ant['direction'] = 'S'
                elif ant['direction'] == 'S':
                    ant['direction'] = 'E'
                elif ant['direction'] == 'E':
                    ant['direction'] = 'N'

            # Move the ant forward:
            if ant['direction'] == 'N':
                ant['y'] -= 1
            if ant['direction'] == 'S':
                ant['y'] += 1
            if ant['direction'] == 'W':
                ant['x'] -= 1
            if ant['direction'] == 'E':
                ant['x'] += 1

            # If the ant goes past the edge of the screen, wrap around to other side.
            if ant['x'] < 0:
                ant['x'] = WIDTH - 1
            elif ant['x'] >= WIDTH:
                ant['x'] = 0

            if ant['y'] < 0:
                ant['y'] = HEIGHT - 1
            elif ant['y'] >= HEIGHT:
                ant['y'] = 0

        board = nextBoard
        step += 1

        time.sleep(PAUSE_LENGTH)
except KeyboardInterrupt:
    pass # When Ctrl-C is pressed, stop looping.
