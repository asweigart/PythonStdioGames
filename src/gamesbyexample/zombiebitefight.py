# Zombie Bite Fight, by Al Sweigart al@inventwithpython.com

# TODO - add more comments and explanation.


import random, time

# Setup constants:
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
LEFT = 'left'
RIGHT = 'right'
FORWARD = 'forward'
STAY = 'stay'


class Zombie:
    def __init__(self, char):
        if len(char) != 1:
            raise Exception('The char argument must be a one-character string.')
        self.char = char
        self.direction = random.choice([NORTH, SOUTH, EAST, WEST])
        self._x = None
        self._y = None

    def getAction(self):
        # Returns one of RIGHT, LEFT, FORWARD, STAY.
        return STAY


class WanderingZombie(Zombie):
    def getAction(self):
        return random.choice([RIGHT, LEFT, FORWARD])


class TurningZombie(Zombie):
    def getAction(self):
        return RIGHT


class Board:
    def __init__(self, width, height, zombies):
        self.width = width
        self.height = height
        self.zombies = zombies
        random.shuffle(self.zombies)

        numberOfZombies = len(zombies)
        numberOfSpaces = self.width * self.height
        if numberOfZombies >= numberOfSpaces:
            raise Exception('Too many zombies for this size board.')

        # Place the zombie objects on the board:
        for zombie in zombies:
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
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
        # Loop over every possible space on this board:
        for y in range(self.height):
            for x in range(self.width):
                zombieAtXY = self.getZombieAt(x, y)
                if zombieAtXY:
                    # Display the zombie's text character:
                    print(zombieAtXY.char, end='')
                    #if zombieAtXY.direction == NORTH:
                    #    print('^', end='')
                    #if zombieAtXY.direction == SOUTH:
                    #    print('v', end='')
                    #if zombieAtXY.direction == EAST:
                    #    print('>', end='')
                    #if zombieAtXY.direction == WEST:
                    #    print('<', end='')
                else:
                    # Display an empty space:
                    print(' ', end='')
            print() # Print a newline.

        count = {}
        for zombie in self.zombies:
            count.setdefault(zombie.__class__.__name__, 0)
            count[zombie.__class__.__name__] += 1
        for zombieType in sorted(count.keys()):
            print(zombieType + ': ' + str(count[zombieType]) + ' ', end='')
        print()

    def runSimulation(self):
        while True:
            self.runSimulationStep()


    def runSimulationStep(self):
        random.shuffle(self.zombies)
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
                        # Move north.
                        zombie._y -= 1

                elif zombie.direction == SOUTH:
                    onBottomRow = zombie._y == self.height - 1
                    zombieToTheSouth = self.getZombieAt(zombie._x, zombie._y + 1)
                    if not onBottomRow and zombieToTheSouth == None:
                        # Move south.
                        zombie._y += 1

                elif zombie.direction == EAST:
                    onRightColumn = zombie._x == self.width - 1
                    zombieToTheEast = self.getZombieAt(zombie._x + 1, zombie._y)
                    if not onRightColumn and zombieToTheEast == None:
                        # Move east.
                        zombie._x += 1

                elif zombie.direction == WEST:
                    onLeftColumn = zombie._x == 0
                    zombieToTheWest = self.getZombieAt(zombie._x - 1, zombie._y)
                    if not onLeftColumn and zombieToTheWest == None:
                        # Move west.
                        zombie._x -= 1

            elif action == STAY:
                pass # Do nothing because the zombie is staying still.

            # Have the zombie bite the zombie in front of it:
            if zombie.direction == NORTH:
                zombieToTheNorth = self.getZombieAt(zombie._x, zombie._y - 1)
                if zombieToTheNorth != None and zombieToTheNorth.__class__ != zombie.__class__:
                    self.zombies.remove(zombieToTheNorth)
                    newZombie = zombie.__class__(zombie.char)
                    newZombie._x = zombie._x
                    newZombie._y = zombie._y - 1
                    self.zombies.append(newZombie)

                zombieToTheSouth = self.getZombieAt(zombie._x, zombie._y + 1)
                if zombieToTheSouth != None and zombieToTheSouth.__class__ != zombie.__class__:
                    self.zombies.remove(zombieToTheSouth)
                    newZombie = zombie.__class__(zombie.char)
                    newZombie._x = zombie._x
                    newZombie._y = zombie._y + 1
                    self.zombies.append(newZombie)

                zombieToTheEast = self.getZombieAt(zombie._x + 1, zombie._y)
                if zombieToTheEast != None and zombieToTheEast.__class__ != zombie.__class__:
                    self.zombies.remove(zombieToTheEast)
                    newZombie = zombie.__class__(zombie.char)
                    newZombie._x = zombie._x + 1
                    newZombie._y = zombie._y
                    self.zombies.append(newZombie)

                zombieToTheWest = self.getZombieAt(zombie._x - 1, zombie._y)
                if zombieToTheWest != None and zombieToTheWest.__class__ != zombie.__class__:
                    self.zombies.remove(zombieToTheWest)
                    newZombie = zombie.__class__(zombie.char)
                    newZombie._x = zombie._x - 1
                    newZombie._y = zombie._y
                    self.zombies.append(newZombie)

        self.display()
        time.sleep(0.25)
        #print('\n' * 40) # Erase the screen.
        import os
        os.system('cls')


zombies = []
for i in range(60):
    zombies.append(WanderingZombie('w'))
    zombies.append(TurningZombie('t'))

board = Board(72, 16, zombies)

board.runSimulation()
