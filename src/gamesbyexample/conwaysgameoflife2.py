"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
This version of Conway's Game of Life uses squares instead of text
characters.
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
This program MUST be run in a Terminal/Command Prompt window.
Do not resize the terminal window while this program is running.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, simulation, bext, terminal"""
__version__ = 0  # TODO - There's a weird bug on the Windows that adds unwanted scrolling.
import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
PAUSE_LENGTH = 0.25

WIDTH, HEIGHT = bext.size()
HEIGHT = (HEIGHT - 1) * 2 # Leave a row free for "Press Ctrl-C..." message.
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

TOP_BLOCK = chr(9600)     # Character 9600 is '▀'
BOTTOM_BLOCK = chr(9604)  # Character 9604 is '▄'
FULL_BLOCK = chr(9608)    # Character 9608 is '█'

def main():
    print('Conway\'s Game of Life')
    print('By Al Sweigart al@inventwithpython.com')
    print('Press Ctrl-C to quit...')
    time.sleep(3)

    # Create random cells:
    currentCells = {}
    nextCells = {}
    previousCells = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                nextCells[x, y] = True

    bext.clear()

    while True:  # Main program loop.
        previousCells = currentCells
        currentCells = nextCells

        # Print the cells:
        for y in range(0, HEIGHT, 2):  # Skip every other row.
            for x in range(WIDTH):
                prevTopHalf = previousCells.get((x, y), False)
                curTopHalf = currentCells.get((x, y), False)
                topHalfHasChanged = prevTopHalf != curTopHalf

                prevBottomHalf = previousCells.get((x, y + 1), False)
                curBottomHalf = currentCells.get((x, y + 1), False)
                bottomHalfHasChanged = prevBottomHalf != curBottomHalf
                if topHalfHasChanged or bottomHalfHasChanged:
                    bext.goto(x, y // 2)
                    if curTopHalf and curBottomHalf:
                        # Fill in both halves:
                        print(FULL_BLOCK, end='')
                    elif curTopHalf and not curBottomHalf:
                        # Fill in top half:
                        print(TOP_BLOCK, end='')
                    elif not curTopHalf and curBottomHalf:
                        # Fill in bottom half:
                        print(BOTTOM_BLOCK, end='')
                    elif not curTopHalf and not curBottomHalf:
                        # Fill in nothing:
                        print(' ', end='')

            print()  # Print a newline at the end of the row.
        print('Press Ctrl-C to quit.', end='', flush=True)

        # Calculate next cells based on current cells:
        nextCells = {}
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get neighboring coordinates:
                leftCoord   = (x - 1) % WIDTH
                rightCoord  = (x + 1) % WIDTH
                topCoord    = (y - 1) % HEIGHT
                bottomCoord = (y + 1) % HEIGHT

                # Count number of living neighbors:
                numNeighbors = 0
                if (leftCoord, topCoord) in currentCells:
                    numNeighbors += 1
                if (x, topCoord) in currentCells:
                    numNeighbors += 1
                if (rightCoord, topCoord) in currentCells:
                    numNeighbors += 1
                if (leftCoord, y) in currentCells:
                    numNeighbors += 1
                if (rightCoord, y) in currentCells:
                    numNeighbors += 1
                if (leftCoord, bottomCoord) in currentCells:
                    numNeighbors += 1
                if (x, bottomCoord) in currentCells:
                    numNeighbors += 1
                if (rightCoord, bottomCoord) in currentCells:
                    numNeighbors += 1

                # Set cell based on Conway's Game of Life rules:
                if currentCells.get((x, y), False):
                    if numNeighbors in (2, 3):
                        nextCells[x, y] = True
                else:
                    if numNeighbors == 3:
                        nextCells[x, y] = True

        time.sleep(PAUSE_LENGTH)  # Pause to reduce flickering.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
