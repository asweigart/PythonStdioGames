"""Worm animation, by Al Sweigart al@inventwithpython.com
A screensaver of multicolor worms moving around.
NOTE: Do not resize the terminal window while this program is running.
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, bext, object-oriented, simulation"""
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
PAUSE_LENGTH = 0.1

# Get the size of the terminal window:
WIDTH, HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

# Characters in the terminal are twice as tall as they are wide, so to
# make our worms look square we pretend two characters horizontally
# is one. This gives us half of the effective width of the terminal:
WIDTH //= 2

NUMBER_OF_WORMS = 12  # (!) Try changing this value.
MIN_WORM_LENGTH = 6   # (!) Try changing this value.
MAX_WORM_LENGTH = 16  # (!) Try changing this value.
ALL_COLORS = bext.ALL_COLORS
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
BLOCK = chr(9608)  # Character 9608 is '█'


def main():
    # Generate worm data structures:
    worms = []
    for i in range(NUMBER_OF_WORMS):
        worms.append(Worm())

    bext.clear()
    while True:  # Main simulation loop.
        # Draw quit message.
        bext.fg('white')
        bext.goto(0, 0)
        print('Ctrl-C to quit.', end='')

        for worm in worms:
            worm.display()

        for worm in worms:
            worm.moveRandom()

        sys.stdout.flush()
        time.sleep(PAUSE_LENGTH)



class Worm:
    def __init__(self):
        self.length = random.randint(MIN_WORM_LENGTH, MAX_WORM_LENGTH)

        coloration = random.choice(['solid', 'stripe', 'random'])
        if coloration == 'solid':
            self.colors = [random.choice(ALL_COLORS)] * self.length
        elif coloration == 'stripe':
            color1 = random.choice(ALL_COLORS)
            color2 = random.choice(ALL_COLORS)
            self.colors = []
            for i in range(self.length):
                self.colors.append((color1, color2)[i % 2])
        elif coloration == 'random':
            self.colors = []
            for i in range(self.length):
                self.colors.append(random.choice(ALL_COLORS))

        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        self.body = []
        for i in range(self.length):
            self.body.append((x, y))
            x, y = getRandomNeighbor(x, y)


    def moveNorth(self):
        headx, heady = self.body[0]
        if self.isBlocked(NORTH):
            return False
        self.body.insert(0, (headx, heady - 1))
        self._eraseLastBodySegment()
        return True


    def moveSouth(self):
        headx, heady = self.body[0]
        if self.isBlocked(SOUTH):
            return False
        self.body.insert(0, (headx, heady + 1))
        self._eraseLastBodySegment()
        return True


    def moveEast(self):
        headx, heady = self.body[0]
        if self.isBlocked(EAST):
            return False
        self.body.insert(0, (headx + 1, heady))
        self._eraseLastBodySegment()
        return True


    def moveWest(self):
        headx, heady = self.body[0]
        if self.isBlocked(WEST):
            return False
        self.body.insert(0, (headx - 1, heady))
        self._eraseLastBodySegment()
        return True


    def isBlocked(self, direction):
        headx, heady = self.body[0]
        if direction == NORTH:
            return heady == 0 or (headx, heady - 1) in self.body
        elif direction == SOUTH:
            return heady == HEIGHT - 1 or (headx, heady + 1) in self.body
        elif direction == EAST:
            return headx == WIDTH - 1 or (headx + 1, heady) in self.body
        elif direction == WEST:
            return headx == 0 or (headx - 1, heady) in self.body


    def moveRandom(self):
        if self.isBlocked(NORTH) and self.isBlocked(SOUTH) and self.isBlocked(EAST) and self.isBlocked(WEST):
            self.body.reverse()

        if self.isBlocked(NORTH) and self.isBlocked(SOUTH) and self.isBlocked(EAST) and self.isBlocked(WEST):
            return False

        hasMoved = False
        while not hasMoved:
            direction = random.choice([NORTH, SOUTH, EAST, WEST])
            if direction == NORTH:
                hasMoved = self.moveNorth()
            elif direction == SOUTH:
                hasMoved = self.moveSouth()
            elif direction == EAST:
                hasMoved = self.moveEast()
            elif direction == WEST:
                hasMoved = self.moveWest()


    def _eraseLastBodySegment(self):
        # Erase the last body segment:
        bext.goto(self.body[-1][0] * 2, self.body[-1][1])
        print('  ', end='')
        self.body.pop()  # Delete the last (x, y) tuple in self.body.


    def display(self):
        for i, (x, y) in enumerate(self.body):
            bext.goto(x * 2, y)
            bext.fg(self.colors[i])
            print(BLOCK + BLOCK, end='')


def getRandomNeighbor(x, y):
    while True:
        direction = random.choice((NORTH, SOUTH, EAST, WEST))
        if direction == NORTH and y != 0:
            return (x, y - 1)
        elif direction == SOUTH and y != HEIGHT - 1:
            return (x, y + 1)
        elif direction == EAST and x != WIDTH - 1:
            return (x + 1, y)
        elif direction == WEST and x != 0:
            return (x - 1, y)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
