# Daleks clone game, by Al Sweigart al@inventwithpython.com
# Move around the board, running away from robots. Try to get the robots to crash into each other.

import logging
LOG_FILE = 'chase_log.txt' # Set to None to display logs on the screen instead.
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # Comment this line out to enable logs.
logging.debug('Start of program.')

import random, sys, os
try:
    import bext #  # Attempt to import the bext module for colorful text.
except:
    bext = None # It's no big deal if bext isn't installed.

if bext is not None:
    bext.bg('black') # Set the background color to black.

WALL = chr(9608) # Character 9608 is '█'


def fg(color):
    if bext is not None:
        bext.fg(color) # Set the foreground color, if bext is installed.


def clearScreen():
    # Clear the previously drawn text:
    if sys.platform == 'win32':
        os.system('cls') # Clears Windows terminal.
    else:
        os.system('clear') # Clears macOS/Linux terminal.


def getNewBoardAndRobots(width, height, numRobots):
    board = {'width': width, 'height': height, 'teleports': 2}

    # Create an empty board:
    for x in range(width):
        for y in range(height):
            board[(x, y)] = ' '

    # Add border walls.
    for x in range(width):
        board[(x, 0)] = WALL # Make top wall.
        board[(x, height - 1)] = WALL # Make bottom wall.
    for y in range(height):
        board[(0, y)] = WALL # Make left wall.
        board[(width - 1, y)] = WALL # Make right wall.

    # Add random walls:
    for i in range(width * height // 8):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        board[(x, y)] = WALL

    # Add robots randomly:
    robots = []
    for i in range(numRobots):
        while True: # Keep looping until we find an empty space.
            x = random.randint(1, width - 2)
            y = random.randint(1, height - 2)
            if board[(x, y)] == ' ': # Only add robots to empty spaces.
                robots.append((x, y))
                break

    logging.debug('New board: %s' % (board))
    logging.debug('New robots: %s' % (robots))
    return board, robots


def getStartingPlayerPosition(board, robots):
    width = board['width']
    height = board['height']
    while True: # Keep looping until we find an empty space.
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        if board[(x, y)] == ' ' and (x, y) not in robots:
            # Only add the player to an empty space.
            return (x, y)


def drawBoard(board, robots, playerPosition):
    clearScreen()
    # Loop over every space on the board:
    for y in range(board['height']):
        for x in range(board['width']):
            # Draw the appropriate character:
            if board[(x, y)] == WALL:
                fg('white')
                print(WALL, end='')
            elif board[(x, y)] == 'x':
                fg('yellow')
                print('x', end='')
            elif (x, y) in robots:
                fg('red')
                print('r', end='')
            elif (x, y) == playerPosition:
                fg('green')
                print('P', end='')
            else:
                print(' ', end='')
        print()


def moveRobots(board, robotPositions, playerPosition):
    playerx, playery = playerPosition
    nextRobotPositions = []

    while len(robotPositions) > 0:
        robotx, roboty = robotPositions[0]

        # Determine the direction the robot moves.
        if robotx < playerx:
            movex = 1
        elif robotx > playerx:
            movex = -1
        elif robotx == playerx:
            movex = 0

        if roboty < playery:
            movey = 1
        elif roboty > playery:
            movey = -1
        elif roboty == playery:
            movey = 0

        # Check if the robot would run into a wall, and adjust course:
        if board[(robotx + movex, roboty + movey)] == WALL:
            if board[(robotx + movex, roboty)] == ' ':
                movey = 0 # See if the robot can move horizontally.
            elif board[(robotx, roboty + movey)] == ' ':
                movex = 0 # See if the robot can move vertically.
            else:
                movex = 0
                movey = 0
        newRobotx = robotx + movex
        newRoboty = roboty + movey

        if board[(robotx, roboty) ] == 'x' or board[(newRobotx, newRoboty)] == 'x':
            # Robot is at a crash site, remove it.
            logging.debug('Robot walked into crash site at %s.' % ((x, y),))
            del robotPositions[0]
            continue

        # Check if it moves into a robot, then destroy both robots:
        if (newRobotx, newRoboty) in nextRobotPositions:
            logging.debug('Robot at %s crashed into another robot at %s.' % ((robotx, roboty), (newRobotx, newRoboty)))
            board[(newRobotx, newRoboty)] = 'x'
            nextRobotPositions.remove((newRobotx, newRobotx))
        else:
            logging.debug('Robot at %s moving to %s.' % ((robotx, roboty), (newRobotx, newRoboty)))
            nextRobotPositions.append((newRobotx, newRoboty))

        del robotPositions[0] # Remove robots from robotPositions as they move.

    logging.debug('moveRobots() is returning %s' % (nextRobotPositions))
    return nextRobotPositions


def getPlayerMove(board, robots, playerPosition):
    x, y = playerPosition

    # Find valid moves:
    q = board[(x - 1, y - 1)] == ' ' and (x - 1, y - 1) not in robots
    w = board[(x + 0, y - 1)] == ' ' and (x + 0, y - 1) not in robots
    e = board[(x + 1, y - 1)] == ' ' and (x + 1, y - 1) not in robots
    d = board[(x + 1, y + 0)] == ' ' and (x + 1, y + 0) not in robots
    c = board[(x + 1, y + 1)] == ' ' and (x + 1, y + 1) not in robots
    _x= board[(x + 0, y + 1)] == ' ' and (x + 0, y + 1) not in robots
    z = board[(x - 1, y + 1)] == ' ' and (x - 1, y + 1) not in robots
    a = board[(x - 1, y + 0)] == ' ' and (x - 1, y + 0) not in robots

    q = 'Q' if q else ' '
    w = 'W' if w else ' '
    e = 'E' if e else ' '
    d = 'D' if d else ' '
    c = 'C' if c else ' '
    _x= 'X' if _x else ' '
    z = 'Z' if z else ' '
    a = 'A' if a else ' '

    while True:
        # Get player's move:
        fg('white')
        print('(T)eleports remaining: %s' % (board['teleports']))
        print('                             (%s) (%s) (%s)' % (q, w, e))
        print('                             (%s) (S) (%s)' % (a, d))
        print('Enter your move (or "quit"): (%s) (%s) (%s)' % (z, _x, c))

        move = input().upper()
        logging.debug('Player entered move of %s.' % (move))
        if move == 'QUIT':
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # Teleport the player to a random space:
            while True: # Keep looping until we find an empty space.
                x = random.randint(1, board['width'] - 2)
                y = random.randint(1, board['height'] - 2)
                if board[(x, y)] == ' ' and (x, y) not in robots:
                    board['teleports'] -= 1
                    return (x, y)
        elif move in (q + w + e + d + c + _x + a + z + 'S').replace(' ', ''):
            # Return the new player position:
            return {'Q': (x - 1, y - 1),
                    'W': (x + 0, y - 1),
                    'E': (x + 1, y - 1),
                    'D': (x + 1, y + 0),
                    'C': (x + 1, y + 1),
                    'X': (x + 0, y + 1),
                    'Z': (x - 1, y + 1),
                    'A': (x - 1, y + 0),
                    'S': (x, y)         }[move]


# Set up a new game:
theBoard, theRobots = getNewBoardAndRobots(40, 20, 6)
playerPosition = getStartingPlayerPosition(theBoard, theRobots)
logging.debug('playerPosition is %s' % ((playerPosition,)))
while True: # Main game loop.
    drawBoard(theBoard, theRobots, playerPosition)

    if len(theRobots) == 0: # Check if the player has won.
        fg('yellow')
        print('You win!')
        logging.debug('Player won.')
        sys.exit()

    playerPosition = getPlayerMove(theBoard, theRobots, playerPosition)

    logging.debug('Robots before moving at %s.' % (theRobots))
    theRobots = moveRobots(theBoard, theRobots, playerPosition)
    logging.debug('Robots after moving at %s.' % (theRobots))

    for x, y in theRobots: # Check if the player has lost.
        if (x, y) == playerPosition:
            drawBoard(theBoard, theRobots, playerPosition)
            fg('red')
            print('You got caught by a robot!')
            logging.debug('Player got caught at %s.' % (playerPosition,))
            sys.exit()
