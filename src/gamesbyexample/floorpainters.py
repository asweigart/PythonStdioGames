"""Floor Painters animation, by Al Sweigart al@inventwithpython.com
A screensaver of several different floor painters painting over each
other's work.
NOTE: Do not resize the terminal window while this program is running.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, simulation, bext"""
__version__ = 0
import random, shutil, sys, time
try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
PAUSE_LENGTH = 0.05 # (!) Try changing this to 0.0 or 1.0.

# (!) Try uncommenting the other possible THE_PAINTERS settings.
THE_PAINTERS = ['red', 'blue', 'green']
#THE_PAINTERS = ['red', 'blue']
#THE_PAINTERS = ['red', 'blue', 'blue', 'blue']
#THE_PAINTERS = ['random']
#THE_PAINTERS = ['random'] * 4
#THE_PAINTERS = ['random'] * 30
#THE_PAINTERS = ['red'] * 10 + ['blue'] * 10

# The colors we can use are limited to the ones that Bext supports:
ALL_COLORS = bext.ALL_COLORS

# Get the size of the terminal window:
WIDTH, HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

# Characters in the terminal are twice as tall as they are wide, so to
# make our painters look square we pretend two characters horizontally
# is one. This gives us half of the effective width of the terminal:
WIDTH //= 2

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
BLOCK = chr(9608)  # Character 9608 is '█'


def main():
    theFloor = getNewFloor()

    # Generate painters:
    painters = []
    for color in THE_PAINTERS:
        painters.append(Painter(color, theFloor))

    bext.fg('black')
    bext.clear()
    while True:  # Main simulation loop.
        # Draw quit message.
        bext.bg('white')
        bext.goto(0, 0)
        print('Ctrl-C to quit.', end='')

        for painter in painters:
            painter.move()

        sys.stdout.flush()
        time.sleep(PAUSE_LENGTH)


def getNewFloor():
    """Return a dictionary to represent the color of the "floor". The
    keys are (x, y) integer tuples and the values are color strings
    such as 'red' or 'black'."""
    floor = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            floor[(x, y)] = 'black'
    return floor


class Painter:
    def __init__(self, color, floor):
        if color == 'random':
            color = random.choice(ALL_COLORS)

        self.color = color
        self.x = random.randint(0, WIDTH - 1)
        self.y = random.randint(0, HEIGHT - 1)
        self.floor = floor


    def move(self):
        """Move the painter, while painting the floor behind them."""
        possibleMoves = [NORTH, SOUTH, EAST, WEST]
        # Remove any moves that would move off of the floor:
        if self.x == 0:
            possibleMoves.remove(WEST)
        if self.x == WIDTH - 1:
            possibleMoves.remove(EAST)
        if self.y == 0:
            possibleMoves.remove(NORTH)
        if self.y == HEIGHT - 1:
            possibleMoves.remove(SOUTH)

        # Remove any moves that go to a space already painted:
        if (NORTH in possibleMoves and
            self.floor[(self.x, self.y - 1)] == self.color):
                possibleMoves.remove(NORTH)
        if (SOUTH in possibleMoves
            and self.floor[(self.x, self.y + 1)] == self.color):
                possibleMoves.remove(SOUTH)
        if (WEST in possibleMoves
            and self.floor[(self.x - 1, self.y)] == self.color):
                possibleMoves.remove(WEST)
        if (EAST in possibleMoves
            and self.floor[(self.x + 1, self.y)] == self.color):
                possibleMoves.remove(EAST)

        # But if every space is already painted, move anywhere that
        # isn't off of the floor:
        if possibleMoves == []:
            if self.x != 0:
                possibleMoves.append(WEST)
            if self.x != WIDTH - 1:
                possibleMoves.append(EAST)
            if self.y != 0:
                possibleMoves.append(NORTH)
            if self.y != HEIGHT - 1:
                possibleMoves.append(SOUTH)

        move = random.choice(possibleMoves)
        bext.bg(self.color)

        # Paint the floor at the old location:
        bext.goto(self.x * 2, self.y)
        print('  ', end='')
        self.floor[(self.x, self.y)] = self.color

        # Move the painter:
        if move == NORTH:
            self.y -= 1
        elif move == SOUTH:
            self.y += 1
        elif move == WEST:
            self.x -= 1
        elif move == EAST:
            self.x += 1

        # Paint the floor at the new location:
        bext.goto(self.x * 2, self.y)
        print('::', end='')
        self.floor[(self.x, self.y)] = self.color


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
