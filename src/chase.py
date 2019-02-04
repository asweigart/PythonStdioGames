# Daleks clone game, by Al Sweigart al@inventwithpython.com
# Move around the board, running away from robots. Try to get the robots to crash into each other.

import random, sys, os


import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program.')


def clearScreen():
    # Clear the previously drawn text:
    if sys.platform == 'win32':
        os.system('cls') # Clears Windows terminal.
    else:
        os.system('clear') # Clears macOS/Linux terminal.


def getNewBoardAndRobots(width, height, numRobots):
    board = {'width': width, 'height': height}

    # Add in empty spaces:
    for x in range(width):
        for y in range(height):
            board[(x, y)] = ' '

    # Add border walls.
    for x in range(width):
        board[(x, 0)] = '#' # Make top wall.
        board[(x, height - 1)] = '#' # Make bottom wall.
    for y in range(height):
        board[(0, y)] = '#' # Make left wall.
        board[(width - 1, y)] = '#' # Make right wall.

    # Add walls randomly:
    #for i in range(width * height // 8):
    #    x = random.randint(1, width - 2)
    #    y = random.randint(1, height - 2)
    #    board[(x, y)] = '#'

    # Add robots randomly:
    robots = []
    for i in range(numRobots):
        while True:
            x = random.randint(1, width - 2)
            y = random.randint(1, height - 2)
            if board[(x, y)] == ' ':
                robots.append((x, y))
                break
    return board, robots

def getStartingPlayerPosition(board, robots):
    width = board['width']
    height = board['height']
    while True:
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        if board[(x, y)] == ' ' and (x, y) not in robots:
            return (x, y)


def drawBoard(board, robots, playerPosition):
    for y in range(board['height']):
        for x in range(board['width']):
            if board[(x, y)] == '#':
                print('#', end='')
            elif board[(x, y)] == 'x':
                print('x', end='')
            elif (x, y) == playerPosition:
                print('P', end='')
            elif (x, y) in robots:
                print('r', end='')
            else:
                print(' ', end='')
        print()


def moveRobots(board, robotPositions, playerPosition):
    playerx, playery = playerPosition
    nextRobotPositions = []

    #for x, y in copyOfRobotPositions:
    while len(robotPositions) > 0:
        x, y = robotPositions[0]

        if board[(x, y) ] == 'x':
            # Robot is at a crash site, remove it.
            logging.debug('Robot walked into crash site at %s' % ((x, y),))
            del robotPositions[0]
            continue

        # Determine the direction the robot moves.
        if x < playerx:
            movex = 1
        elif x > playerx:
            movex = -1
        elif x == playerx:
            movex = 0

        if y < playery:
            movey = 1
        elif y > playery:
            movey = -1
        elif y == playery:
            movey = 0

        # Check if the robot would run into a wall, and adjust course:
        if board[(x + movex, y + movey)] == '#':
            if board[(x + movex, y)] == ' ': # See if the robot can move horizontally.
                movey = 0
            elif board[(x, y + movey)] == ' ': # See if the robot can move vertically.
                movex = 0
            else:
                movex = 0
                movey = 0

        # Check if it moves into a robot, then destroy both robots:
        if (x + movex, y + movey) in nextRobotPositions:# and (x + movex, y + movey) != (x, y):
            logging.debug('Robot crash: Deleting %s and %s' % ((x, y), (x + movex, y + movey)))
            board[(x + movex, y + movey)] = 'x'
            nextRobotPositions.remove((x + movex, y + movey))
        else:
            logging.debug('Robot moving: %s to %s' % ((x, y), (x + movex, y + movey)))
            nextRobotPositions.append((x + movex, y + movey))

        #robotPositions.remove((x, y))
        del robotPositions[0]

    logging.debug('moveRobots() is returning %s' % (nextRobotPositions))
    return nextRobotPositions


def getPlayerMove(theBoard, theRobots, playerPosition):
    pass



theBoard, theRobots = getNewBoardAndRobots(40, 20, 6)
playerPosition = getStartingPlayerPosition(theBoard, theRobots)

while True:
    #clearScreen()
    drawBoard(theBoard, theRobots, playerPosition)
    logging.debug(theRobots)
    theRobots = moveRobots(theBoard, theRobots, playerPosition)
    logging.debug(theRobots)

    #playerPosition = getPlayerMove(theBoard, theRobots, playerPosition)

    input()


