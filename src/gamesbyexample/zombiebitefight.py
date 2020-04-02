"""Zombie Bite Fight, by Al Sweigart al@inventwithpython.com

Tags: extra-large, simulation, bext"""

# TODO - add more comments and explanation.

# TODO - bite should be a separate action!!!!
__version__ = 0
import random, time, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()


# Set up the constants:
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

LEFT = 'left'
RIGHT = 'right'
FORWARD = 'forward'
STAY = 'stay'
BITE = 'bite'

WIDTH = 78
HEIGHT = 22

PAUSE_LENGTH = 0.0

FACE_UP = chr(9650) # Character 9650 is '▲'.
FACE_DOWN = chr(9660) # Character 9660 is '▼'.
FACE_LEFT = chr(9668) # Character 9668 is '◄'.
FACE_RIGHT = chr(9658) # Character 9658 is '►'.

class Zombie:
    def __init__(self, color):
        if color not in ('red', 'green', 'blue', 'yellow', 'cyan', 'purple', 'white', 'black'):
            raise Exception('color arg must be one of: red green blue yellow cyan purple white black')
        self.__class__.color = color
        self.direction = random.choice([NORTH, SOUTH, EAST, WEST])
        self._x = None
        self._y = None

    def getAction(self):
        # Returns one of RIGHT, LEFT, FORWARD, STAY.
        return STAY


class WanderingZombie(Zombie):
    def __init__(self, color):
        super().__init__(color)
        self.biteNow = random.choice([True, False])

    def getAction(self):
        self.biteNow = not self.biteNow
        if self.biteNow:
            return BITE
        else:
            return random.choice([RIGHT, LEFT, FORWARD])


class TurningZombie(Zombie):
    def __init__(self, color):
        super().__init__(color)
        self.biteNow = random.choice([True, False])

    def getAction(self):
        self.biteNow = not self.biteNow
        if self.biteNow:
            return BITE
        else:
            return RIGHT


class StillZombie(Zombie):
    def getAction(self):
        return BITE


class Board:
    def __init__(self, zombies):
        self.zombies = zombies
        random.shuffle(self.zombies)

        numberOfZombies = len(zombies)
        numberOfSpaces = WIDTH * HEIGHT
        if numberOfZombies >= numberOfSpaces:
            raise Exception('Too many zombies for this size board.')

        # Place the zombie objects on the board:
        for zombie in zombies:
            while True:
                x = random.randint(0, WIDTH - 1)
                y = random.randint(0, HEIGHT - 1)
                zombieAtXY = self.getZombieAt(x, y)

                if zombieAtXY == None:
                    zombie._x = x
                    zombie._y = y
                    break


    def getZombieAt(self, x, y):
        for zombie in self.zombies:
            if zombie._x == x and zombie._y == y:
                return zombie
        return None


    def display(self):
        for zombie in self.zombies:
            bext.goto(zombie._x, zombie._y)
            bext.fg(zombie.color)
            # Display the zombie's text character:
            if zombie.direction == NORTH:
                print(FACE_UP, end='')
            elif zombie.direction == SOUTH:
                print(FACE_DOWN, end='')
            elif zombie.direction == EAST:
                print(FACE_RIGHT, end='')
            elif zombie.direction == WEST:
                print(FACE_LEFT, end='')

        # Display a count of each kind of zombie:
        # TODO - potential bug - erase full first
        bext.goto(0, HEIGHT)
        count = {}
        for zombie in self.zombies:
            count.setdefault(zombie.__class__, 0)
            count[zombie.__class__] += 1
        for zombieType in sorted(count.keys(), key=lambda x: x.__name__):
            bext.fg(zombieType.color)
            print(zombieType.__name__ + ': ' + str(count[zombieType]) + ' ', end='')
        print('', flush=True)

    def runSimulation(self):
        try:
            while True:
                self.runSimulationStep()
        except KeyboardInterrupt:
            sys.exit()


    def runSimulationStep(self):
        random.shuffle(self.zombies)
        bittenZombies = []
        newZombies = []
        for zombie in self.zombies:
            action = zombie.getAction()
            if action == RIGHT:
                if zombie.direction == NORTH:
                    zombie.direction = EAST
                elif zombie.direction == SOUTH:
                    zombie.direction = WEST
                elif zombie.direction == EAST:
                    zombie.direction = SOUTH
                elif zombie.direction == WEST:
                    zombie.direction = NORTH
            elif action == LEFT:
                if zombie.direction == NORTH:
                    zombie.direction = WEST
                elif zombie.direction == SOUTH:
                    zombie.direction = EAST
                elif zombie.direction == EAST:
                    zombie.direction = NORTH
                elif zombie.direction == WEST:
                    zombie.direction = SOUTH
            elif action == FORWARD:
                if zombie.direction == NORTH:
                    onTopRow = zombie._y == 0
                    zombieToTheNorth = self.getZombieAt(zombie._x, zombie._y - 1)
                    if not onTopRow and zombieToTheNorth == None:
                        bext.goto(zombie._x, zombie._y)
                        print(' ', end='')
                        # Move north.
                        zombie._y -= 1

                elif zombie.direction == SOUTH:
                    onBottomRow = zombie._y == HEIGHT - 1
                    zombieToTheSouth = self.getZombieAt(zombie._x, zombie._y + 1)
                    if not onBottomRow and zombieToTheSouth == None:
                        bext.goto(zombie._x, zombie._y)
                        print(' ', end='')
                        # Move south.
                        zombie._y += 1

                elif zombie.direction == EAST:
                    onRightColumn = zombie._x == WIDTH - 1
                    zombieToTheEast = self.getZombieAt(zombie._x + 1, zombie._y)
                    if not onRightColumn and zombieToTheEast == None:
                        bext.goto(zombie._x, zombie._y)
                        print(' ', end='')
                        # Move east.
                        zombie._x += 1

                elif zombie.direction == WEST:
                    onLeftColumn = zombie._x == 0
                    zombieToTheWest = self.getZombieAt(zombie._x - 1, zombie._y)
                    if not onLeftColumn and zombieToTheWest == None:
                        bext.goto(zombie._x, zombie._y)
                        print(' ', end='')
                        # Move west.
                        zombie._x -= 1

            elif action == STAY:
                pass # Do nothing because the zombie is staying still.

            # Have the zombie bite the zombie in front of it:
            if zombie.direction == NORTH:
                zombieInFront = self.getZombieAt(zombie._x, zombie._y - 1)
            elif zombie.direction == SOUTH:
                zombieInFront = self.getZombieAt(zombie._x, zombie._y + 1)
            elif zombie.direction == EAST:
                zombieInFront = self.getZombieAt(zombie._x + 1, zombie._y)
            elif zombie.direction == WEST:
                zombieInFront = self.getZombieAt(zombie._x - 1, zombie._y)

            if zombieInFront != None and zombieInFront.__class__ != zombie.__class__:
                bittenZombieIndex = self.zombies.index(zombieInFront)
                newZombie = zombie.__class__(zombie.color)
                newZombie._x = zombieInFront._x
                newZombie._y = zombieInFront._y
                newZombie.direction = zombieInFront.direction
                self.zombies[bittenZombieIndex] = newZombie


        self.display()
        time.sleep(PAUSE_LENGTH)


zombies = []
for i in range(40):
    # Colors must be one of 'red', 'green', 'blue', 'yellow', 'cyan',
    # 'purple', 'white', or 'black'
    zombies.append(TurningZombie('green'))
    zombies.append(StillZombie('yellow'))
    zombies.append(WanderingZombie('blue'))

board = Board(zombies)


print('''Zombie Bite Fight, by Al Sweigart al@inventwithpython.com

In this zombie simulation, you program zombies to roam around biting
each other, converting them into their type of zombie.

The types of zombies set up for this simulation are:
TODO

Press Enter to begin...''')
input()
bext.clear()
board.runSimulation()

